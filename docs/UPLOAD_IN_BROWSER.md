# Upload the updated portfolio using only GitHub.com

The files in the **root of this release folder** should replace their matching counterparts **in the root of the GitHub repository**. Do not upload the enclosing `Progetti_Stoppa_Federico_PUBLIC_RECRUITER_v3/` directory as an additional level.

1. Unzip the release archive locally; this does **not** require GitHub Desktop.
2. Open the public repository on GitHub.com and stay in the root directory (you should see `projects/`, `tests/`, `README.md`).
3. Choose **Add file → Upload files**. Select/drag the **contents** of the unzipped folder. Where GitHub offers replacement of existing paths, verify the path before committing.
4. Before confirming the commit, make sure `README.md`, `projects/`, `tests/`, `docs/`, `scripts/` and `.github/workflows/` are all at the root; the old README must be replaced, not kept alongside a nested duplicate.
5. Commit with a clear message such as `Improve recruiter portfolio and add verified demos`.
6. Check the home page renders the new opening title; check `projects/01-support-analytics/SAMPLE_RESULTS.md` and the **Actions** tab for CI results. If GitHub doesn't accept all directories through the browser uploader, use the browser editor at `github.dev` for the remaining files.

No private repository, personal data or live API key is needed. If using a manual multi-commit upload, the repository is temporarily inconsistent until all paths are updated: verify the final state after finishing.
