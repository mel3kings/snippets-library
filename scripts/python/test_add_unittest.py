import unittest
from add import add


class TestSum(unittest.TestCase):

    def test_Adding(self):
        x = add(3, 4)
        self.assertEqual(x, 7, "should be 7")

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 3)), 6, "Should be 6")


if __name__ == '__main__':
    unittest.main()
