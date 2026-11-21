# Machina CAD De-ID

Private hackathon workspace for a reproducible engineering-file de-identification pipeline.

## Status

This is a development scaffold. No real files are de-identified yet. The CLI only checks that the package is installed. Do not submit its output as a processed corpus.

## Setup

Use Python 3.11 or newer and a case-sensitive filesystem for corpus processing.

```bash
git clone https://github.com/Preetham-p06/CAD.git
cd CAD
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m machina --help
```

On Windows, activate with `.venv\Scripts\Activate.ps1` in PowerShell.

Keep all actual data in a separate directory, such as `../machina-data/`, with `input/`, `private/`, `work/`, `output/`, and `submissions/` children. Raw input is immutable. Never commit corpus files, mappings, credentials, or private logs. Ignore rules are a backstop, not a privacy guarantee.

## Two-person workflow

- Pipeline owner: inventory, registry, planning, runner, validation, packaging, integration and submissions. Start from `pipeline-core`.
- Format owner: handlers, native CAD feasibility, embedded content and reference preservation. Start from `format-handlers`.
- Both: agree on interfaces before implementation; inspect representative output together.

```bash
git fetch origin
git switch --track origin/pipeline-core
# Partner instead uses origin/format-handlers.
```

Push small commits and open pull requests into `main`. Review each other's changes. Do not commit directly to someone else's working branch. Read `AGENTS.md` before using a coding agent and follow `docs/PLAN.md`.

## Submission layout

Prepare attempts outside this repository:

```text
attempt-N/
  corpus/
  code/
  README.txt
```

Include complete source and pinned dependency versions in `code/`. Keep mappings, raw input, credentials and private run logs out. Keep uploaded attempts immutable. Use the organizer-provided uploader and your team's Builders folder.

No open-source license is selected; agree on licensing before distributing the code.
