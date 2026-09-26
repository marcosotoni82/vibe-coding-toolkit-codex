"""Install project-local guidance only; default is a read-only preview."""
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def install(destination, apply=False):
    dest = Path(destination).expanduser().resolve()
    if dest == ROOT or ROOT in dest.parents or dest in ROOT.parents:
        raise ValueError('Destination must be separate from the toolkit checkout')
    if not dest.is_dir():
        raise ValueError('Destination must be an existing project directory')
    skill = ROOT / 'codex/skills/vibe-codex'
    entries = [(ROOT / 'codex/templates/AGENTS.md.template', dest / 'AGENTS.md')]
    entries += [(p, dest / '.agents/skills/vibe-codex' / p.relative_to(skill))
                for p in sorted(skill.rglob('*')) if p.is_file()]
    # Preflight the complete plan, including symlink ancestors, before writing.
    for src, target in entries:
        chain = [target, *target.parents]
        for part in chain:
            if part == dest:
                break
            if part.is_symlink():
                raise ValueError(f'Symlink destination refused: {part}')
            if part.exists() and part != target and not part.is_dir():
                raise ValueError(f'Parent is not a directory: {part}')
        if target.exists() and (not target.is_file() or target.read_bytes() != src.read_bytes()):
            raise ValueError(f'Existing different file; merge manually: {target}')
    pending = [(a,b) for a,b in entries if not b.exists()]
    if apply:
        for src, target in pending:
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open('xb') as stream:
                stream.write(src.read_bytes())
    return len(pending)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('destination')
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    try:
        count = install(args.destination, args.apply)
    except (ValueError, OSError) as exc:
        parser.exit(1, f'{exc}\n')
    print(f'{"Created" if args.apply else "Would create"} {count} files; no dependencies or global settings changed.')
