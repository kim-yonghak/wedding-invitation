"""Build plain HTML with absolute, crawler-readable Open Graph image URLs."""
import html
import os
import re
import shutil
from pathlib import Path
from urllib.parse import urlsplit

root = Path(__file__).resolve().parent.parent
base = os.environ.get('SITE_URL', '').strip().rstrip('/')
parsed = urlsplit(base)
if parsed.scheme != 'https' or not parsed.hostname or parsed.query or parsed.fragment or parsed.username:
    raise SystemExit('SITE_URL must be an absolute HTTPS site address without query or fragment.')
out = root / '_site'
out.mkdir(exist_ok=True)
source = (root / 'index.html').read_text(encoding='utf-8')
for attribute, key, value in [('property', 'og:url', base+'/'), ('property', 'og:image', base+'/assets/share-preview.png'), ('name', 'twitter:image', base+'/assets/share-preview.png')]:
    pattern = rf'(<meta {attribute}="{re.escape(key)}" content=")[^"]*(">)'
    source, count = re.subn(pattern, lambda m: m[1]+html.escape(value, quote=True)+m[2], source)
    if count != 1:
        raise SystemExit(f'Expected exactly one {key} tag, got {count}')
(out / 'index.html').write_text(source, encoding='utf-8')
shutil.copytree(root / 'assets', out / 'assets', dirs_exist_ok=True)
(out / '.nojekyll').touch()
print('Ready:', out)
