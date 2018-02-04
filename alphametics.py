import re
import unittest
import itertools

LETTER = re.compile(r'[A-Z]')


def solve(equiation):
    letters = set(LETTER.findall(equiation))
    letters_not_zero = set(w[0] for w in set(re.findall(r'([A-Z]+)', equiation, re.MULTILINE)))

    for purmutation in itertools.permutations(range(10), len(letters)):
        letters_with_values = dict(zip(letters, purmutation))

        def letter_is_zero_but_should_not_be():
            for letter, value_of_letter in letters_with_values.items():
                if letter in letters_not_zero and value_of_letter == 0:
                    return True
            return False

        if letter_is_zero_but_should_not_be():
            continue

        equiation_with_replaced_letters = equiation
        for letter, value_of_letter in letters_with_values.items():
            equiation_with_replaced_letters = equiation_with_replaced_letters.replace(letter, str(value_of_letter))

        try:
            if eval(equiation_with_replaced_letters):
                return letters_with_values
        except SyntaxError:
            pass

    return {}


class TestAlphametics(unittest.TestCase):
    def test_puzzle_with_three_letters(self):
        self.assertEqual(solve("I + BB == ILL"), {"I": 1, "B": 9, "L": 0})

    def test_solution_must_have_unique_value_for_each_letter(self):
        self.assertEqual(solve("A == B"), {})

    def test_leading_zero_solution_is_invalid(self):
        self.assertEqual(solve("ACA + DD == BD"), {})

    def test_puzzle_with_four_letters(self):
        self.assertEqual(
            solve("AS + A == MOM"), {"A": 9, "S": 2, "M": 1, "O": 0})

    def test_puzzle_with_six_letters(self):
        self.assertEqual(
            solve("NO + NO + TOO == LATE"),
            {"N": 7,
             "O": 4,
             "T": 9,
             "L": 1,
             "A": 0,
             "E": 2})

    def test_puzzle_with_seven_letters(self):
        self.assertEqual(
            solve("HE + SEES + THE == LIGHT"),
            {"E": 4,
             "G": 2,
             "H": 5,
             "I": 0,
             "L": 1,
             "S": 9,
             "T": 7})

    @unittest.skip("")
    def test_puzzle_with_eight_letters(self):
        self.assertEqual(
            solve("SEND + MORE == MONEY"),
            {"S": 9,
             "E": 5,
             "N": 6,
             "D": 7,
             "M": 1,
             "O": 0,
             "R": 8,
             "Y": 2})

    @unittest.skip("")
    def test_puzzle_with_ten_letters(self):
        self.assertEqual(
            solve("AND + A + STRONG + OFFENSE + AS + A + GOOD == DEFENSE"),
            {"A": 5,
             "D": 3,
             "E": 4,
             "F": 7,
             "G": 8,
             "N": 0,
             "O": 2,
             "R": 1,
             "S": 6,
             "T": 9})


if __name__ == '__main__':
    unittest.main()
