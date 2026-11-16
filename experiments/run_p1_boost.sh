#!/bin/bash
# Takes over the P1 stages (pair and framing trials, then confidence trials) of run_remaining.sh for the
# five chain victims, with a higher request concurrency. Same commands, same seeds, same outputs; only
# the share of the request window changes. See DECISIONS.md, entry of Mon 16 Nov, 02:35.
cd "$(dirname "$0")/.." || exit 1
PY=.venv/bin/python
L=results/logs
N=20
C=${P1_CONC:-24}
VICTIMS="deepseek-v4-flash qwen3.8-27b gemma-4-31b-it glm-5.3-flash glm-5.2"
HARD=$(date -j -f "%Y-%m-%d %H:%M" "2026-11-16 10:11" +%s)

log() { echo "$(date '+%m-%d %H:%M:%S') $*" >> "$L/cut_driver.log"; }

stage() {
  local name=$1 rc=1 i; shift
  for i in 1 2 3; do
    if [ "$(date +%s)" -ge "$HARD" ]; then log "SKIP  $name (past cutoff)"; return 1; fi
    log "START $name (boost, attempt $i)"
    "$@" >> "$L/cut_$name.log" 2>&1; rc=$?
    log "END   $name rc=$rc"
    [ $rc -eq 0 ] && return 0
    sleep 60
  done
  log "FAIL  $name after 3 attempts"; return $rc
}

p1() { local v=$1
  stage "p1_$v"   $PY -m experiments.p1_self_trust --run main --victims "$v" --parts pairs --designs pair,framing --concurrency $C
  stage "conf_$v" $PY -m experiments.p1_self_trust --run main --victims "$v" --parts conf --limit $N --concurrency $C
}

log "P1BOOST start; concurrency $C per key"
for v in $VICTIMS; do p1 "$v" & done
wait
log "P1BOOST done"
