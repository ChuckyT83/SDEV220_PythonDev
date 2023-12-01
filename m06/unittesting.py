import unittest
import unicodeStrings as us

class TestUnit(unittest.TestCase):
    def setup(self):
        pass
    def tearDown(self):
        pass
    def test_lookup(self):
        data = us.get_by_name("a")
        self.assertEqual("a", data[0])

    def test_name(self):
        data = us.get_by_name("a")
        self.assertEqual('LATIN SMALL LETTER A', data[1])

if __name__ == "__main__":
    unittest.main()