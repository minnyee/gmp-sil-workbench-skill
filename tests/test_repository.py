"""Exercise broken links and installed-skill portability with isolated files."""

import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "tools" / "check_repository.py"
SPEC = importlib.util.spec_from_file_location("check_repository", SCRIPT)
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


class RepositoryChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.skill = self.root / "skills" / "gmp-sil-workbench"
        self.skill.mkdir(parents=True)
        self.entry = self.skill / "SKILL.md"
        self.header = "---\nname: gmp-sil-workbench\ndescription: Example skill\n---\n"
        self.entry.write_text(self.header, encoding="utf-8")

    def test_installed_reference_and_public_upstream_are_valid(self):
        (self.skill / "reference.md").write_text("# Reference\n", encoding="utf-8")
        self.entry.write_text(
            self.header + "[Local](reference.md) [Upstream](https://example.org/source)\n",
            encoding="utf-8",
        )
        self.assertEqual(CHECK.scan(self.root), [])

    def test_broken_reference_is_reported(self):
        self.entry.write_text(self.header + "[Missing](missing.md)\n", encoding="utf-8")
        self.assertTrue(any("missing link target" in item for item in CHECK.scan(self.root)))

    def test_skill_cannot_require_repository_readme(self):
        (self.root / "README.md").write_text("# Repository\n", encoding="utf-8")
        self.entry.write_text(self.header + "[Readme](../../README.md)\n", encoding="utf-8")
        self.assertTrue(any("repository-only" in item for item in CHECK.scan(self.root)))

    def test_file_uri_is_nonportable(self):
        self.entry.write_text(self.header + "[Local](file:///tmp/example.md)\n", encoding="utf-8")
        self.assertTrue(any("nonportable" in item for item in CHECK.scan(self.root)))

    def test_relative_escape_is_reported(self):
        self.entry.write_text(self.header + "[Outside](../../../outside.md)\n", encoding="utf-8")
        self.assertTrue(any("escapes repository" in item for item in CHECK.scan(self.root)))

    def test_path_with_spaces_is_supported(self):
        (self.skill / "my reference.md").write_text("# Reference\n", encoding="utf-8")
        self.entry.write_text(self.header + "[Local](<my reference.md>)\n", encoding="utf-8")
        self.assertEqual(CHECK.scan(self.root), [])

    def test_metadata_is_required(self):
        self.entry.write_text("# Incomplete\n", encoding="utf-8")
        self.assertTrue(any("frontmatter" in item for item in CHECK.scan(self.root)))


if __name__ == "__main__":
    unittest.main()
