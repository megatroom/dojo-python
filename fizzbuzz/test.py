import unittest
from fizzbuzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):

    def test_with_1(self):
        self.assertEqual(fizz_buzz(1), [1])

    def test_with_5(self):
        self.assertEqual(fizz_buzz(5), [1, 2, 'Fizz', 4, 'Buzz'])

    def test_with_15(self):
        result = fizz_buzz(15)
        self.assertEqual(result[14], 'FizzBuzz')


if __name__ == '__main__':
    unittest.main()
