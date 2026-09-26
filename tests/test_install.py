import importlib.util
from pathlib import Path
import tempfile
import unittest
spec = importlib.util.spec_from_file_location('installer', Path(__file__).resolve().parents[1]/'scripts/install.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)

class InstallerTests(unittest.TestCase):
    def test_preview_apply_and_idempotency(self):
        with tempfile.TemporaryDirectory() as directory:
            dest = Path(directory)
            n = installer.install(dest)
            self.assertGreater(n, 10)
            self.assertEqual(list(dest.iterdir()), [])
            self.assertEqual(installer.install(dest, True), n)
            self.assertTrue((dest/'.agents/skills/vibe-codex/SKILL.md').is_file())
            self.assertEqual(installer.install(dest, True), 0)

    def test_conflict_preserves_all_files(self):
        with tempfile.TemporaryDirectory() as directory:
            dest = Path(directory)
            (dest/'AGENTS.md').write_text('Existing project rules')
            with self.assertRaises(ValueError): installer.install(dest, True)
            self.assertEqual((dest/'AGENTS.md').read_text(), 'Existing project rules')
            self.assertFalse((dest/'.agents').exists())

    def test_late_conflict_prevents_early_write(self):
        with tempfile.TemporaryDirectory() as directory:
            dest = Path(directory)
            skill = dest/'.agents/skills/vibe-codex'
            skill.mkdir(parents=True)
            (skill/'SKILL.md').write_text('Custom skill')
            with self.assertRaises(ValueError): installer.install(dest, True)
            self.assertFalse((dest/'AGENTS.md').exists())

    def test_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as directory, tempfile.TemporaryDirectory() as other:
            dest = Path(directory)
            (dest/'.agents').symlink_to(other, target_is_directory=True)
            with self.assertRaises(ValueError): installer.install(dest, True)
            self.assertEqual(list(Path(other).iterdir()), [])
            self.assertFalse((dest/'AGENTS.md').exists())

    def test_self_install_rejected(self):
        with self.assertRaises(ValueError): installer.install(installer.ROOT, True)

if __name__ == '__main__': unittest.main()
