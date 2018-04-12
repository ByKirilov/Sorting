import comparators
import unittest
from unittest import TestCase


class TestComparators(TestCase):
    def test_lexicographical_order_key(self):
        col = ['a', 'h', 'f', 'bb', 'xxx', 'qqqq']
        sorted_col = sorted(col, key=comparators.lexicographical_order_key)

        self.assertEqual(['a', 'bb', 'f', 'h', 'qqqq', 'xxx'], sorted_col)

        col = [2, 4, 1, 15, 5, 3, 2]
        sorted_col = sorted(col, key=comparators.lexicographical_order_key)

        self.assertEqual([1, 2, 2, 3, 4, 5, 15], sorted_col)

    def test_length_order_key(self):
        col = ['a', 'h', 'f', 'bb', 'xxx', 'qqqq']
        sorted_col = sorted(col, key=comparators.length_order_key)

        self.assertEqual(['a', 'h', 'f', 'bb', 'xxx', 'qqqq'], sorted_col)

        col = [2, 24, 1513, 500, 333, 42]
        sorted_col = sorted(col, key=comparators.length_order_key)

        self.assertEqual([2, 24, 42, 500, 333, 1513], sorted_col)


if __name__ == '__main__':
    unittest.main()
