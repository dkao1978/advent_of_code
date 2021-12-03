import fileinput
from itertools import combinations

if __name__ == "__main__":

    input = [x.strip() for x in fileinput.input()]
    input = [int(x) for x in input if x.isnumeric()]

    # part 1
    for x in input:
        if (remaining := 2020-x) in input:
            break
    print(x * remaining)

    # part 2
    for x, y in combinations(input, 2):
        if (z := 2020 - x - y) in input:
            print(x * y * z)
            break



