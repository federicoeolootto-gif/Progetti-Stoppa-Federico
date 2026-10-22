# Public Portfolio Audit — 22 October 2026 (recruiter edition v3)

## What was reviewed

This release builds on the previously screened public-only portfolio. The main README and 13 project descriptions were rewritten for recruiter readability; an independently implemented, synthetic Support Operations report, a reproduction guide, link/secret-pattern preflight checker, unit tests and a minimal GitHub Actions workflow were added. Original project archives **are not part of this release**.

## Source and provenance boundaries

| Project | Content available publicly | Withheld / qualifier |
|---|---|---|
| Support Analytics | Fictional support-ticket records, SQL schema and queries, Python KPI report, Power BI design notes | Best Tool data, confidential `.qvw` files, private client data and actual employer KPI results |
| Climate ML | Original group work is described; unrelated synthetic Python ML illustration | Original survey data, data cleaning notebooks, original research estimates and unreviewed coauthor outputs |
| FantaGiungla | New artificial auction-event-processing code + tests | Original code, Airtable access, private room data, participants, tokens, real ML model |
| Nova | Independent offline provider fallback example + tests | Electron source, API configuration and real transcripts |
| PaperLens | Technical description plus upstream source attribution | Source archive, `.env` files, Git history, unconfirmed upstream diff |
| Other academic work | Descriptive methodology notes and a separate synthetic spatial algorithm | Licensable or research-restricted data, unverified code, coauthor materials |

No public demo is represented as the identical production code from the original project. Neither synthetic ML errors nor synthetic ticket statistics measure real research or business impact.

## Code and documentation verification

- 12 Python unittest cases passed in the available environment, including reporting invariants and a source-pattern/link check.
- 2 Node.js tests passed for offline mocked-provider fallback.
- Python support-ticket report executed: 60 fabricated cases; 48 closed; 12 open; 54 observed first-view timestamps.
- Markdown relative links and common secret/private-identifier patterns checked using `scripts/check_public_release.py`.
- PostgreSQL SQL and GitHub Actions CI workflow have **not** been executed end-to-end within GitHub / a running PostgreSQL installation. CI will run upon publication on GitHub if actions are enabled and permissions permit it.
- Security scans are heuristic and cannot guarantee absence of every undiscovered secret or establish licenses. Review future files anew.

## Security and distribution

- No raw `.zip`, `.env`, `.git`, `.qvw`, PDF, Excel, notebook caches, vendor page captures, user correspondence or live credentials are included.
- No actual employer records or original restricted research datasets are redistributed.
- PaperLens was developed from a separate [MIT-licensed upstream](https://github.com/hridaya14/PaperLens); authorship is attributed and no source copy is shipped.
- Files intended for upload are text-only sample code, documentation, tests, a synthetic CSV and GitHub Actions workflow.
- Review the GitHub commit history separately before asserting full historical safety; this audit concerns this **specific new release's files**.

## Reproduce and inspect

Start at [README.md](README.md), follow [run guide](docs/RUN_DEMOS.md) and inspect [evidence map](docs/PROJECT_EVIDENCE.md). For personal data concerns see [SECURITY.md](SECURITY.md).
