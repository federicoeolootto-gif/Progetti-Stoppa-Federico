# Public Release Audit — 22 October 2026

## Scope

The **exact content of this package** was reviewed for obvious secret patterns, personal identifiers, repository metadata, licensed exports, unreleased datasets and misleading claims. Source material included the originally supplied Nova and PaperLens archives, notebook source/outputs, selected reports and the previous public demonstration package. Original archives are **not included**.

## Material excluded by design

| Source area | Reason for exclusion |
|---|---|
| PaperLens source ZIP | Environment/backup files, possible credential assignments, local paths, embedded upstream and Git history. Original open-source authorship is credited; source diff not validated. |
| Nova application ZIP | Full application and included rollback backup remain unreviewed for redistribution, safe operational use and third-party bundling; only new offline demonstration included. |
| FantaGiungla/Airtable | No live tokens, invites, participants, private auction events or vendor scraping code. Synthetic event processor only. |
| Climate ML | Group research dataset, notebook outputs and absolute local paths excluded. Synthetic ML is a separate tutorial, not the study's training script. |
| Employer QlikView | No original dashboards, QVW files or private customer data. Only fabricated records and unrelated SQL demonstration. |
| Research assistant data task | Original instructions, distributed dataset and hiring correspondence excluded; standalone fictional spatial technique demo. |
| Pirelli, Bonn, thesis and coursework | Full raw notebooks, licensed financial data, IPUMS microdata, coauthor material and unpublished thesis research excluded; descriptive notes only. |

## Claims and functionality

- `FantaGiungla`: model development underway; no accuracy claim.
- `Nova`: original system integration with external APIs; public fallback example is offline and mocked.
- `PaperLens`: upstream adaptation, not entirely original application or a verified production release.
- `Power BI`: tutorial/instructions only; no finished `.pbix` is claimed.
- `Synthetic SQL`: intended for PostgreSQL syntax; actual PostgreSQL execution requires a PostgreSQL installation. CSV/data tests run without PostgreSQL.
- `Climate ML`: demo uses fictional data; cannot reproduce the source project's estimated effects.

## Verification procedure

Run `python -m unittest discover -s tests -v` and `node --test projects/04-nova/mock_provider.test.cjs`. In the audit environment: 9 Python unit tests and 2 Node.js tests passed (public examples). Separately, 63 offline Node.js tests in the original Nova v13.7 archive passed; these were not full Windows, external API or production deployment validation. PostgreSQL SQL scripts were not executed against a live PostgreSQL server. Neither makes a network request.

This is **defense-in-depth**, not a formal proof of absence of secrets: any subsequent repository commit or revised artifact must be scanned anew. Never publish raw private ZIP archives.
