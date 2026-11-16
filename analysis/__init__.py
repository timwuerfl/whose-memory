"""Statistical analysis, figures, tables and paper numbers for "Whose Memory Is This?".

Entry point: ``python -m analysis.reproduce [--run main]``. Every module reads only
``results/processed/<run>/`` (and ``results/spend_ledger.csv``) and writes to ``results/analysis/<run>/`` and
``paper/``; no module sends a model request.
"""
