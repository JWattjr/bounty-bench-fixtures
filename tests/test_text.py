import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from bountybench_text import parse_duration, title_case, truncate_words


class TextHelperTests(unittest.TestCase):
    def test_short_text_is_unchanged(self):
        self.assertEqual(truncate_words("one two", 5), "one two")

    def test_single_unit_duration(self):
        self.assertEqual(parse_duration("45m"), 2700)

    def test_plain_words_are_capitalized(self):
        self.assertEqual(title_case("hello world"), "Hello World")


if __name__ == "__main__":
    unittest.main()
