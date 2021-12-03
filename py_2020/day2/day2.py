import fileinput
import re
from collections import Counter


if __name__ == "__main__":

    #part 1
    total = 0
    for line in fileinput.input():
        lower, upper, letter, passwd = re.match(r"(\d+)-(\d+) (\w): (\w+)", line).groups()
        lower, upper = int(lower), int(upper)
        counts = Counter(passwd.strip())
        if lower <= counts[letter] <= upper:
            total += 1
    print(total)

    # part 2
    total = 0
    for line in fileinput.input():
        pos1, pos2, letter, passwd = re.match(r"(\d+)-(\d+) (\w): (\w+)", line).groups()
        pos1, pos2 = int(pos1), int(pos2)
        counts = Counter(passwd.strip())
        if passwd[pos1 - 1] == letter and passwd[pos2 - 1] == letter:
            continue
        elif passwd[pos1 - 1] == letter or passwd[pos2 - 1] == letter:
            total += 1
    print(total)
