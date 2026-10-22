"""Conservative offline checks of a recruiter-facing, deliberately synthetic repository.

This is NOT a guarantee that a file is safe, licensed or free of secrets.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKIP = {'.git', '__pycache__', '.pytest_cache', '.venv', 'node_modules'}
DENIED_SUFFIXES = {'.env', '.pem', '.p12', '.pfx', '.key', '.zip', '.7z', '.bak', '.db', '.sqlite', '.qvw', '.dta', '.sav', '.xlsx', '.pdf', '.ipynb'}
PATTERNS = {
    'private key header': re.compile(r'-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----'),
    'GitHub token': re.compile(r'\bgh[pousr]_[A-Za-z0-9_]{20,}\b'),
    'AWS access key': re.compile(r'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b'),
    'Bearer authorization': re.compile(r'(?i)Authorization\s*:\s*Bearer\s+[A-Za-z0-9_.-]{20,}'),
    'private email': re.compile(r'\b[A-Za-z0-9.+_-]+@(?:gmail|hotmail|outlook|yahoo|libero|studenti\.unipd)\.[A-Za-z.]{2,}\b', re.I),
    'Windows home directory': re.compile(r'(?i)[A-Z]:\\Users\\[^\\\s"\']{2,}'),
}
MAX_FILE_BYTES = 2_000_000


def audit(root=ROOT):
    issues = []
    md = []
    for file in root.rglob('*'):
        if not file.is_file() or any(part in SKIP for part in file.relative_to(root).parts):
            continue
        rel = file.relative_to(root)
        if file.name.startswith('.env') or file.suffix.lower() in DENIED_SUFFIXES:
            issues.append(f'Unreviewed file type: {rel}')
            continue
        if file.stat().st_size > MAX_FILE_BYTES:
            issues.append(f'Oversized file: {rel}')
            continue
        try:
            content = file.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            issues.append(f'Unexpected binary file: {rel}')
            continue
        for label, regex in PATTERNS.items():
            if regex.search(content):
                issues.append(f'{label} pattern found in: {rel}')
        if file.suffix == '.md': md.append((file, content))
    for file, content in md:
        # Verify local links; no HTTP requests and no Markdown inline parser needed.
        for target in re.findall(r'\]\(([^)]+)\)', content):
            target = target.split('#')[0].strip()
            if not target or target.startswith(('https://', 'http://', 'mailto:', '#')):
                continue
            if not (file.parent / target).exists():
                issues.append(f'Broken local link from {file.relative_to(root)} to {target}')
    return issues


if __name__ == '__main__':
    errors = audit()
    if errors:
        print('PUBLIC AUDIT NEEDS REVIEW:')
        for err in errors: print('-', err)
        sys.exit(1)
    print('Public demo file patterns and local Markdown links: OK (not a security certification)')
