from pathlib import Path
from dataclasses import dataclass
from copy import deepcopy

UNSOLVED = 0
ROWS = 9
COLUMNS = 9
@dataclass
class Sudoku:
    board: list[list[int]]

    def open(self):
        open_fields = []
        for row in range(ROWS):
            for col in range(COLUMNS):
                if self.board[row][col] == UNSOLVED:
                    open_fields.append((row, col))
        return open_fields

    def solve(self):
        open_fields = self.open()
        if open_fields:
            first = open_fields[0]
            for candidate in range(1, 9 + 1):
                board_copy = deepcopy(self.board)
                board_copy[first[0]][first[1]] = candidate
                s = Sudoku(board_copy)
                if s.valid():
                    possible_solved = s.solve()
                    if possible_solved:
                        return possible_solved
        else:
            if self.valid():
                return self
    def valid(self):
        def v(line):
            number_in_row = [int(r) for r in line if r != UNSOLVED]
            if len(number_in_row) == len(set(number_in_row)):
                return True
            else:
                return False

        for row in self.board:
            if not v(row):
                return False

        # columns
        for c in range(9):
            column = [self.board[row][c] for row in range(9)]
            if not v(column):
                return False

        # boxes
        for h_box in range(3):
            for v_box in range(3):
                box = []
                for x in range(h_box*3, h_box*3 + 3):
                    for y in range(v_box * 3, v_box * 3 + 3):
                        box.append(self.board[x][y])
                if not v(box):
                    return False
        return True


    def print(self):
        rows = []
        rows.append("-" * (9 + 10))
        for r in range(ROWS):
            row = ["| "]
            for c in range(COLUMNS):
                row.append(str(self.board[r][c]))
                if (c + 1) % 3 == 0:
                    row.append(" | ")

            rows.append("".join(row))
            if (r + 1) % 3 == 0:
                rows.append("-" * (9 + 10))
        return "\n".join(rows)

def main():
    text = Path('hard.txt').read_text()
    s = []
    for t in text.split('\n'):
        l = [d if d != '_' else UNSOLVED for d in list(t)]
        assert len(l) == 9, l
        s.append(l)
    sudoku = Sudoku(s)
    solved = sudoku.solve()
    if solved:
        print(solved.print())
    else:
        print("not solved")


if __name__ == '__main__':
    main()