import fileinput

if __name__ == "__main__":
    input = [x.strip().split(' ') for x in fileinput.input()]
    input = [[x[0], int(x[1])] for x in input]
    x = y = aim = 0

    # part 1
    for command in input:
        match command:
            case ["forward", units]:
                x += units
            case ["down", units]:
                y -= units
            case ["up", units]:
                y += units
    print (x * y)

    x = y = aim = 0
    # part 2
    for command in input:
        match command:
            case ["forward", units]:
                x += units
                y += aim * units
            case ["down", units]:
                aim += units
            case ["up", units]:
                aim -= units
    print (x * y)
