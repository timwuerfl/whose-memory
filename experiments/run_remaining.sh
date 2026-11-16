#!/bin/bash
# Remaining main-run stages after the 40-hour sleep, in the order fixed in DECISIONS.md
# ("Sun 15 Nov, 23:30"). Every stage is resumable (response cache); rerunning this script is safe.
#
#   bash experiments/run_remaining.sh            # core stages, then the stretch list
#
# Environment: HARD_S / STRETCH_S = seconds from start after which no core / stretch stage is started.
cd "$(dirname "$0")/.." || exit 1
PY=.venv/bin/python
L=results/logs
N=20                                   # seeds per family (50-69) -> 60 episodes per victim
EPS=60
CHAIN="deepseek-v4-flash qwen3.8-27b gemma-4-31b-it glm-5.3-flash glm-5.2"
P1V="$CHAIN qwen3.5-397b"
START=$(date +%s)
HARD=$((START + ${HARD_S:-38400}))      # 10 h 40 min
STRETCH=$((START + ${STRETCH_S:-33600})) # 9 h 20 min

log() { echo "$(date '+%m-%d %H:%M:%S') $*" >> "$L/cut_driver.log"; }

# stage <name> <cutoff epoch> <command...>: up to 3 attempts, output appended to results/logs/cut_<name>.log
stage() {
  local name=$1 cutoff=$2 rc=1 i; shift 2
  for i in 1 2 3; do
    if [ "$(date +%s)" -ge "$cutoff" ]; then log "SKIP  $name (past cutoff)"; return 1; fi
    log "START $name (attempt $i)"
    "$@" >> "$L/cut_$name.log" 2>&1; rc=$?
    log "END   $name rc=$rc"
    [ $rc -eq 0 ] && return 0
    sleep 60
  done
  log "FAIL  $name after 3 attempts"
  return $rc
}

chain() {
  local v=$1
  stage "forge_$v"  $HARD $PY -m experiments.hosted_gen --run main --stages forge --victims "$v" --limit $N
  stage "detect_$v" $HARD $PY -m experiments.hosted_detect --run main --victims "$v" --per-family $N --parts v,c,r
  stage "p4core_$v" $HARD $PY -m experiments.p4_gate --run main --victims "$v" --limit $EPS --conditions none,G1
  stage "p4tags_$v" $HARD $PY -m experiments.p4_gate --run main --victims "$v" --limit $EPS --conditions G2u,G2s,G1+G2s
}

p1() {
  local v=$1
  stage "p1_$v"   $HARD $PY -m experiments.p1_self_trust --run main --victims "$v" --parts pairs --designs pair,framing --concurrency 3
  stage "conf_$v" $HARD $PY -m experiments.p1_self_trust --run main --victims "$v" --parts conf --limit $N --concurrency 3
}

log "DRIVER start; hard cutoff $(date -r $HARD '+%m-%d %H:%M'), stretch cutoff $(date -r $STRETCH '+%m-%d %H:%M')"
for v in $P1V;   do p1 "$v" & done
for v in $CHAIN; do chain "$v" & done
wait
log "CORE done"

# ---- stretch list (DECISIONS.md item 6), strictly in this order
stage "negs_all" $STRETCH $PY -m experiments.hosted_detect --run main --per-family $N --parts negs
for v in $CHAIN; do
  stage "p4extra_$v" $STRETCH $PY -m experiments.p4_gate --run main --victims "$v" --limit $EPS --conditions no_memory,G2s_insider &
done
wait
stage "afc_all" $STRETCH $PY -m experiments.hosted_detect --run main --per-family $N --parts afc
for v in $P1V; do
  stage "p1rest_$v" $STRETCH $PY -m experiments.p1_self_trust --run main --victims "$v" --parts pairs --concurrency 3 &
done
wait
for v in $P1V; do
  stage "confrest_$v" $STRETCH $PY -m experiments.p1_self_trust --run main --victims "$v" --parts conf --concurrency 3 &
done
wait
log "DRIVER done"
