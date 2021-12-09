import fileinput


if __name__ == "__main__":
    inp = open("input").read()
    inp = [x.replace("\n", "") for x in inp.split("\n\n")]
    total = sum([len(set(x)) for x in inp])
    print(total)

    inp = open("input").read()
    inp = [x.strip() for x in inp.split("\n\n")]
    inp = [x.split("\n") for x in inp]
    inp = [[set(y) for y in x] for x in inp]
    inp = [set.intersection(*x) for x in inp]
    total = sum([len(set(x)) for x in inp])
    print(total)

