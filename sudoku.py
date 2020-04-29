INPUT_SIMPLE = [
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

INPUT_HARD = [
    [0, 3, 0, 0, 0, 0, 6, 0, 0],
    [0, 0, 8, 4, 0, 3, 0, 0, 0],
    [9, 2, 0, 0, 0, 0, 5, 0, 0],
    [1, 0, 0, 8, 2, 0, 0, 0, 0],
    [0, 0, 2, 0, 7, 0, 3, 0, 0],
    [0, 0, 0, 0, 3, 4, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 7, 0, 0, 0, 0, 5, 0],
]

INPUT_HARD2 = [
    [0, 6, 0, 0, 9, 0, 0, 0, 4],
    [0, 8, 0, 0, 0, 4, 0, 0, 0],
    [0, 0, 5, 0, 0, 0, 0, 0, 3],
    [0, 0, 7, 4, 6, 0, 0, 3, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 7],
    [0, 5, 0, 0, 0, 1, 4, 8, 0],
    [2, 0, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 3, 0, 0, 0, 6, 0],
    [1, 0, 0, 0, 8, 0, 0, 5, 0],
]


def solve_sudoku(sudoku):
    if is_sudoku_solved(sudoku):
        print_sudoku(sudoku)
        return True

    row_for_candidate, column_for_candidate = next_empty_cell(sudoku)
    if row_for_candidate == -1:
        print_sudoku(sudoku)
        return True

    candidates = calculate_candidates(column_for_candidate, row_for_candidate, sudoku)

    for candidate in candidates:
        sudoku[row_for_candidate][column_for_candidate] = candidate
        if solve_sudoku(sudoku):
            return True
        sudoku[row_for_candidate][column_for_candidate] = 0

    return False


def is_sudoku_solved(sudoku):
    # rows
    for row in sudoku:
        if not is_house_finished(row):
            return False

    # columns
    for column in range(9):
        values = [sudoku[row][column] for row in range(9)]
        if not is_house_finished(values):
            return False
    # houses
    for house in range(9):
        if not is_house_finished(get_house_values(house, sudoku)):
            return False

    return True


def is_house_finished(house):
    return len(house) == 9 and set(range(1, 10)) == set(house)


def get_house_values(house, sudoku):
    result = set()
    x_top_left_house_cell = house // 3 * 3
    y_top_left_house_cell = 3 * (house % 3)
    for row in range(x_top_left_house_cell, x_top_left_house_cell + 3):
        for column in range(y_top_left_house_cell, y_top_left_house_cell + 3):
            result.add(sudoku[row][column])
    return result


def get_values_in_surrounding_house(x, y, sudoku):
    house = 3 * (x // 3) + y // 3
    return get_house_values(house, sudoku)


def next_empty_cell(sudoku):
    for row in range(0, 9):
        for column in range(0, 9):
            if sudoku[row][column] == 0:
                return row, column
    return -1, -1


def calculate_candidates(column_for_candidate, row_for_candidate, sudoku):
    candidates = set(range(1, 10))
    # block in row
    candidates = candidates - set(sudoku[row_for_candidate])
    # blocked in column
    candidates = candidates - {sudoku[r][column_for_candidate] for r in range(9)}
    # blocked in house
    candidates = candidates - get_values_in_surrounding_house(
        row_for_candidate, column_for_candidate, sudoku
    )
    return candidates


def print_sudoku(sudoku):
    def print_line(a):
        return (a + 1) % 3 == 0 and a < 8

    for row_number, row in enumerate(sudoku):
        n = []
        for column_number, number in enumerate(row):
            n.append(str(number) if number else ".")
            if print_line(column_number):
                n.append("|")
        print(" ".join(n))

        if print_line(row_number):
            print("-" * (9 * 2 + 3))
    print()


if __name__ == "__main__":
    sudoku_to_solve = INPUT_SIMPLE
    print_sudoku(sudoku_to_solve)
    solve_sudoku(sudoku_to_solve)
