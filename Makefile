# Analysis and paper build. On this Mac run make with
#   DEVELOPER_DIR=/Library/Developer/CommandLineTools make <target>
# (the Xcode licence is not accepted, see DECISIONS.md). RUN=pilot for development data.
PY      ?= .venv/bin/python
RUN     ?= main
TECTONIC := $(shell test -x cache/bin/tectonic && echo cache/bin/tectonic || command -v tectonic)
export MPLCONFIGDIR := $(CURDIR)/cache/matplotlib

.PHONY: test analysis figures paper check

test:
	$(PY) -m pytest -q

analysis:
	$(PY) -m analysis.reproduce --run $(RUN)

figures:
	$(PY) -m analysis.figures --run $(RUN)

paper: analysis
	@test -n "$(TECTONIC)" || (echo "tectonic not found (cache/bin/tectonic or PATH)"; exit 1)
	TECTONIC_CACHE_DIR=cache/tectonic $(TECTONIC) -X compile paper/main.tex --outdir paper

check:
	$(PY) -m analysis.check_numbers paper/main.tex --numbers paper/numbers.tex
