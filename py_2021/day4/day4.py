import re
import sys


def check_win(board, row, col):
    col = []
    for col_idx in range(len(board[row])):
        col.append(board[col_idx][row])
    return sum(col) == -5 or sum(board[row]) == -5

def to_int(x):
    return list(map(int, re.findall("(\d+)", x)))


if __name__ == "__main__":
    filename = sys.argv[1]
    inp = open(filename).read().strip()
    numbers, *boards = inp.split("\n\n")

    boards = [x.split("\n") for x in boards]
    boards = [[to_int(x) for x in y] for y in boards]
    numbers = to_int(numbers)

    won = []
    board_width = len(boards[0][0])
    for number in numbers:
        board_indexes = set(range(len(boards))) - set(won)
        for b_idx in board_indexes:
            for col in range(board_width):
                for row in range(len(boards[b_idx])):
                    if boards[b_idx][row][col] == number:
                        boards[b_idx][row][col] = -1
                        if check_win(boards[b_idx], row, col):
                            won.append(b_idx)
                            total = 0
                            for row in boards[b_idx]:
                                row_sum = sum([x for x in row if x != -1])
                                total += row_sum
                            print(b_idx, total * number)




