# PaperLens — Research Document AI Workflow (Open-Source Adaptation)

**Provenance:** The base PaperLens application is third-party, MIT-licensed open-source software. Attribution: [upstream project](https://github.com/hridaya14/PaperLens) (original project, copyright and license remain with original authors). This entry describes experimentation, configuration and extensions of that project, NOT sole authorship of its full stack.

**Observed workflow:** Docker Compose, Python/FastAPI backend, Next.js/TypeScript interface, PostgreSQL, Redis, OpenSearch, document parsing and retrieval, external AI/embedding services. Historical scripts include checks for service readiness, complete document indexing, structured 10-branch mind-map generation and long retrieval-augmented answers. The existence of scripts is not proof the checks passed in a reproducible environment.

**Why code is intentionally withheld:** supplied archives contain multiple environment files, backups, original Git history and local paths. A later source release requires precise attribution, an upstream diff, clearance of every embedded secret, removal of old history and validated setup instructions. **No source ZIP, `.env`, deployment configuration or document uploads are published here.**
