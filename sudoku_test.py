import pytest
import sudoku


@pytest.fixture()
def simple_sudoku():

    return [
        [0, 0, 8, 0, 5, 0, 0, 3, 1],
        [0, 1, 0, 9, 0, 0, 4, 2, 0],
        [5, 3, 0, 2, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 2],
        [0, 0, 1, 0, 0, 0, 9, 0, 0],
        [2, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 6, 0, 5, 4],
        [0, 7, 2, 0, 0, 1, 0, 6, 0],
        [6, 9, 0, 0, 4, 0, 1, 0, 0],
    ]


@pytest.fixture()
def simple_sudoku_solved():

    return [
        [9, 2, 8, 6, 5, 4, 7, 3, 1],
        [7, 1, 6, 9, 3, 8, 4, 2, 5],
        [5, 3, 4, 2, 1, 7, 8, 9, 6],
        [8, 5, 9, 4, 7, 3, 6, 1, 2],
        [3, 6, 1, 8, 2, 5, 9, 4, 7],
        [2, 4, 7, 1, 6, 9, 5, 8, 3],
        [1, 8, 3, 7, 9, 6, 2, 5, 4],
        [4, 7, 2, 5, 8, 1, 3, 6, 9],
        [6, 9, 5, 3, 4, 2, 1, 7, 8],
    ]


@pytest.mark.parametrize(
    "given, expected",
    [
        [[0] * 9, False],
        [[1], False],
        [[1, 1, 1, 1, 1, 1, 1, 1, 1], False],
        [[1, 2, 3, 4, 5, 6, 7, 8, 9], True],
        [[0, 2, 3, 4, 5, 6, 7, 8, 9], False],
    ],
)
def test_foo(given, expected):
    assert sudoku.is_house_finished(given) == expected


def test_column_is_finished(simple_sudoku):
    assert not sudoku.is_sudoku_solved(simple_sudoku)


def test_house_values(simple_sudoku):
    assert sudoku.get_house_values(0, simple_sudoku) == {
        0,
        0,
        8,
        0,
        1,
        0,
        5,
        3,
        0,
    }
    assert sudoku.get_house_values(8, simple_sudoku) == {
        0,
        5,
        4,
        0,
        6,
        0,
        1,
        0,
        0,
    }


def test_next_empty_cell(simple_sudoku):
    assert (0, 0) == sudoku.next_empty_cell(simple_sudoku)
    simple_sudoku[0][0] = 1
    assert (0, 1) == sudoku.next_empty_cell(simple_sudoku)
    simple_sudoku[0][1] = 2
    assert (0, 3) == sudoku.next_empty_cell(simple_sudoku)


def test_next_empty_solved(simple_sudoku_solved):
    assert (-1, -1) == sudoku.next_empty_cell(simple_sudoku_solved)


def test_solve_sudoku(simple_sudoku, simple_sudoku_solved):
    assert sudoku.solve_sudoku(simple_sudoku)
    assert simple_sudoku == simple_sudoku_solved
