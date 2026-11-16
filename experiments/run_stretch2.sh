#!/bin/bash
# Stretch stages after the driver's matched negatives and extra gate conditions (see DECISIONS.md,
# entry of Mon 16 Nov, 08:15): 2AFC for the five chain victims, then the secondary P1 designs on the
# items of seeds 50-69 for all six P1 victims. Must be started with network access to the API host.
cd "$(dirname "$0")/.." || exit 1
PY=.venv/bin/python
L=results/logs
N=20
P1V="deepseek-v4-flash qwen3.8-27b gemma-4-31b-it glm-5.3-flash glm-5.2 qwen3.5-397b"
NOSTART=$(date -j -f "%Y-%m-%d %H:%M:%S" "2026-11-16 09:55:00" +%s)   # no new API stage after this
HARD=$(date -j -f "%Y-%m-%d %H:%M:%S" "2026-11-16 10:11:00" +%s)

log() { echo "$(date '+%m-%d %H:%M:%S') $*" >> "$L/cut_driver.log"; }

stage() {   # stage <name> <cutoff epoch> <command...>
  local name=$1 cutoff=$2 rc=1 i; shift 2
  for i in 1 2 3; do
    if [ "$(date +%s)" -ge "$cutoff" ]; then log "SKIP  $name (past cutoff)"; return 1; fi
    log "START $name (stretch2, attempt $i)"
    "$@" >> "$L/cut_$name.log" 2>&1; rc=$?
    log "END   $name rc=$rc"
    [ $rc -eq 0 ] && return 0
    sleep 60
  done
  log "FAIL  $name after 3 attempts"; return $rc
}

p1lim() { local v=$1 d
  # secondary designs on seeds 50-69, one design at a time so that a design is complete for all six
  # victims before the next one starts to compete (order given by the analysis: stale, single, forced,
  # turn); pair and framing are already complete
  for d in stale single forced turn; do
    stage "p1lim_${d}_$v" $NOSTART env MEMLAB_KEY_INFLIGHT=18 $PY -m experiments.p1_self_trust --run main --victims "$v" --parts pairs --designs $d --limit $N --concurrency 3
  done
  # a limited run writes a 60-item tidy file; this run has nothing left to request and rewrites the
  # tidy file from the raw rows of all 120 items
  stage "p1tidy_$v" $HARD $PY -m experiments.p1_self_trust --run main --victims "$v" --parts pairs --designs pair,framing --concurrency 3
}

log "STRETCH2 start"
stage "afc_all" $NOSTART env MEMLAB_KEY_INFLIGHT=18 $PY -m experiments.hosted_detect --run main --per-family $N --parts afc
for v in $P1V; do p1lim "$v" & done
wait
log "STRETCH2 done"
