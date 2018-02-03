import unittest
import re


def get_fizz_buzz(inp):
    def get(number, op, addition):
        return addition if op(number) else ""

    result = get(inp, lambda n: n % 3 == 0, "Fizz")
    result += get(inp, lambda n: n % 5 == 0, "Buzz")

    return result if result else str(inp)


class FizzBuzzTest(unittest.TestCase):
    def test_1is1(self):
        self.assertEqual("1", get_fizz_buzz(1))

    def test_2is2(self):
        self.assertEqual("2", get_fizz_buzz(2))

    def test_3isFizz(self):
        self.assertEqual("Fizz", get_fizz_buzz(3))

    def test_5isBuzz(self):
        self.assertEqual("Buzz", get_fizz_buzz(5))

    def test_9isFizz(self):
        self.assertEqual("Fizz", get_fizz_buzz(9))

    def test_10isBuzz(self):
        self.assertEqual("Buzz", get_fizz_buzz(10))

    def test_15isFizzBuzz(self):
        self.assertEqual("FizzBuzz", get_fizz_buzz(15))
