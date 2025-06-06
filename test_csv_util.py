import unittest
from csv_util import CSVUtility
import numbers

class TestCSVUtility(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.util = CSVUtility("sample.csv")

    def test_read(self):
        self.assertEqual(len(self.util.df.columns), 4)

    def test_filter_rows(self):
        result = self.util.filter_rows("Quantity", ">", 10)
        self.assertTrue((result["Quantity"] > 10).all())

    def test_sort_rows(self):
        result = self.util.sort_rows("Price")
        self.assertTrue(result["Price"].is_monotonic_increasing)

    def test_aggregate_column(self):
        total = self.util.aggregate_column("Quantity", "sum")
        self.assertIsInstance(total, numbers.Number)

    def test_palindrome(self):
        count = self.util.count_palindromes("Product")
        self.assertGreaterEqual(count, 1)

if __name__ == '__main__':
    unittest.main()