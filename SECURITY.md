# Security, privacy, attribution and permitted release

This is a **public recruiter portfolio**. Do not add real credentials, access tokens, authorization headers, personal addresses, phone numbers, private email, recorded interviews, student documents, client information, unlicensed course data or real auction-room events. `.gitignore` is not an adequate security control on its own.

## Public material

The repository contains explanatory material and independently created **synthetic technical demonstrations**, each with a limited, labelled scope. The original application source and research datasets are not distributed. Underlying project authors, coauthors, employer data owners and open-source developers retain their respective rights. In particular, [PaperLens upstream](https://github.com/hridaya14/PaperLens) is a third-party MIT-licensed project: this portfolio does not claim sole authorship.

## Before future public uploads

1. Work from a clean source tree. Do not upload personal source archives or their Git histories.
2. Replace all sensitive records with artificial data. Check `.env*`, backups, screenshots, notebook outputs, local paths, HTTP logs and metadata.
3. Confirm contributor permissions, third-party licensing and publication timing for research.
4. Run `python scripts/check_public_release.py` and all unit tests. It scans known patterns but is **not a complete security audit**.
5. Examine the staged Git diff and final public contents. Git retains files in historical commits even after later removal.
6. Rotate any credential that has ever been exposed: simply deleting it from a newer commit cannot undo access.

Please use GitHub's standard repository tools to report a concern. The portfolio does not publish an email address for security reports.
