"""Verify vendored upstream assets against the recorded snapshot."""
import hashlib
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / 'codex/upstream-integrity.json').read_text())
errors = [name for name, digest in manifest.items()
          if not (ROOT/name).is_file() or hashlib.sha256((ROOT/name).read_bytes()).hexdigest() != digest]
if errors:
    raise SystemExit('Changed or missing upstream assets: ' + ', '.join(errors))
print(f'Integrity OK: {len(manifest)} assets')
