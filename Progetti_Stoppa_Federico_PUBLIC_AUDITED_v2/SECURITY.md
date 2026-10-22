# Security, privacy and provenance policy

This is a **public** collection. Never submit credentials or private materials, even temporarily: Git retains previous versions.

## Specifically excluded

- Original `.env` files, API tokens, access keys, SSH keys, session cookies, authorization headers, database passwords, credential backups, browser storage and Git metadata from source archives.
- Names or identifiers of private auction participants, addresses, contact details, private emails, CVs, client records, employer QlikView documents, unpublished coauthor manuscripts and licensed microdata.
- Raw ZIP backups, raw notebook outputs, unreviewed AI/LLM transcripts, internal logs and private local paths.
- Third-party application sources without independently established redistribution rights. PaperLens is an open-source **adaptation** with attribution, not an original software platform authored from scratch.

## What is included

Only independently authored, small **synthetic code demonstrations**, synthetic ticket records, test cases and descriptive case-study notes. The source applications remain separate and unmodified. Simulated samples cannot be treated as evidence of production-scale performance or accuracy.

## Release procedure

1. Start from a clean folder with fresh Git history, not a private development clone.
2. Exclude secrets at source, verify configuration/fixtures are fictitious, inspect generated notebooks and file metadata.
3. Scan the **exact upload directory**; run tests; inspect every file type and all Git changes.
4. Verify licenses and contributor permissions before releasing actual project source.
5. If an exposed credential has ever been live, revoke/rotate it with the provider: removing it from a later commit is not enough.

To report a security concern, contact the repository owner using GitHub's standard profile tools; no personal email is published here.
