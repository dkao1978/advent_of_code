import fileinput
from collections import defaultdict

if __name__ == "__main__":

    # part 1
    vec_map = defaultdict(int)
    for line in fileinput.input():
        coord = line.strip().split(" -> ")
        start, end = [[int(y) for y in x.split(",")] for x in coord]

        if start[0] != end[0] and start[1] != end[1]:
            continue

        if start[0] == end[0]:
            x_range = [start[0]] * (abs(start[1] - end[1]) + 1)
        elif start[0] < end[0]:
            x_range = list(range(start[0], end[0] + 1))
        else:
            x_range = list(reversed(range(end[0], start[0] + 1)))

        if start[1] == end[1]:
            y_range = [start[1]] * (abs(start[0] - end[0]) + 1)
        elif start[1] < end[1]:
            y_range = list(range(start[1], end[1] + 1))
        else:
            y_range = list(reversed(range(end[1], start[1] + 1)))

        for x,y in list(zip(x_range, y_range)):
            vec_map[f"{x,y}"] += 1

    print(len([x for x in vec_map.items() if x[1] > 1]))

    # part 2
    vec_map = defaultdict(int)
    for line in fileinput.input():
        coord = line.strip().split(" -> ")
        start, end = [[int(y) for y in x.split(",")] for x in coord]

        if start[0] == end[0]:
            x_range = [start[0]] * (abs(start[1] - end[1]) + 1)
        elif start[0] < end[0]:
            x_range = list(range(start[0], end[0] + 1))
        else:
            x_range = list(reversed(range(end[0], start[0] + 1)))

        if start[1] == end[1]:
            y_range = [start[1]] * (abs(start[0] - end[0]) + 1)
        elif start[1] < end[1]:
            y_range = list(range(start[1], end[1] + 1))
        else:
            y_range = list(reversed(range(end[1], start[1] + 1)))

        for x,y in list(zip(x_range, y_range)):
            vec_map[f"{x,y}"] += 1

    print(len([x for x in vec_map.items() if x[1] > 1]))
