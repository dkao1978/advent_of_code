import fileinput

from collections import defaultdict
from functools import reduce
from operator import mul
from puzzle_helper import value_at_pos


def find_basin(row, col, basin: list[int], map: list, seen: dict) -> list[int]:

    curr = map[row][col]
    if curr == 9:
        return basin
    if seen[row][col] == 0:
        seen[row][col] = 1
        basin.append(map[row][col])
    else:
        return basin
    # Left
    if (left := value_at_pos(row - 1, col, map)) is not None and curr <= left:
        basin = find_basin(row - 1, col, basin, map, seen)
    # Right
    if (right := value_at_pos(row + 1, col, map)) is not None and curr <= right:
        basin = find_basin(row + 1, col, basin, map, seen)
    # Up
    if (up := value_at_pos(row, col - 1, map)) is not None and curr <= up:
        basin = find_basin(row, col - 1, basin, map, seen)
    # Down
    if (down := value_at_pos(row, col + 1, map)) is not None and curr <= down:
        basin = find_basin(row, col + 1, basin, map, seen)

    return basin


if __name__ == "__main__":
    inp = [x.strip() for x in fileinput.input()]
    inp = [[int(y) for y in x] for x in inp]

    low_points = []
    height = len(inp)
    seen = defaultdict(lambda: defaultdict(int))
    basins = []
    for row in range(len(inp)):
        for col in range(len(inp[row])):
            width = len(inp[row])
            curr = inp[row][col]
            surroundings = []
            surroundings.append(value_at_pos(row - 1, col, inp))
            surroundings.append(value_at_pos(row + 1, col, inp))
            surroundings.append(value_at_pos(row, col - 1, inp))
            surroundings.append(value_at_pos(row, col + 1, inp))
            is_lowest = all(
                [True if (x is None or x > curr) else False for x in surroundings]
            )
            if is_lowest:
                basin = []
                basin = find_basin(row, col, basin, inp, seen)
                basins.append(basin)
                low_points.append(inp[row][col])
    print(len(low_points) + sum(low_points))
    largest_basins = sorted(basins, key=lambda x: len(x), reverse=True)[:3]
    print(reduce(mul, [len(x) for x in largest_basins]))
