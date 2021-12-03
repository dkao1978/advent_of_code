import fileinput



if __name__ == "__main__":

    input = [list(x.strip()) for x in fileinput.input()]

    # part 1
    row_len = len(input[0])
    count = 0
    col, row = 0,0
    while row < len(input):
        count += input[row][col] == "#"
        col += 3
        row += 1
        col %= row_len
    print(count)


    # part 2
    row_deltas = [(1,1), (3,1),  (5,1), (7,1), (1,2)]
    total = 1
    row_len = len(input[0])
    for dc, dr in row_deltas:
        count = 0
        col, row = 0,0
        while row < len(input):
            count += input[row][col] == "#"
            col += dc
            row += dr
            col %= row_len
        total *= count
    print(total)

