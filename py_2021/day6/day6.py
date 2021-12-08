import fileinput
from collections import Counter

if __name__ == "__main__":
    inp = next(fileinput.input()).strip()
    inp = [int(x) for x in inp.split(",")]
    cur_fishes = Counter(inp)
    fishes = [cur_fishes[x] for x in range(9)]
    for _ in range(256):
        fishes = fishes[1:] + fishes[:1]
        fishes[6] += fishes[-1]
    print(sum(fishes))

