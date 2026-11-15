import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from bountybench_slugify import normalize_slug


class NormalizeSlugTests(unittest.TestCase):
    def test_collapses_repeated_hyphens(self):
        self.assertEqual(normalize_slug("red---green"), "red-green")

    def test_trims_hyphens_at_both_ends(self):
        self.assertEqual(normalize_slug("---Blue---"), "blue")

    def test_normalizes_spaces_and_punctuation(self):
        self.assertEqual(normalize_slug("  Hello, world!  "), "hello-world")


if __name__ == "__main__":
    unittest.main()
