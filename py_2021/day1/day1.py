import fileinput


if __name__ == "__main__":

    input = [int(x.strip()) for x in fileinput.input()]

    # part 1
    count = sum([int(x) < int(y) for x, y in zip(input, input[1:])])
    print(count)

    # part 1
    triples = list(zip(input, input[1:], input[2:]))
    count2 = sum([sum(x) < sum(y) for x,y in zip(triples, triples[1:])])
    print(count2)

