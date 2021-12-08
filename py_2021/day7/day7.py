import fileinput

if __name__ == "__main__":
    inp = next(fileinput.input()).strip()
    inp = [int(x) for x in inp.split(",")]

    results = []
    for idx in range(max(inp)):
        total = 0
        for num in inp:
            n = abs(num-idx)
            total += ((n * (n + 1))/2)
        results.append(total)
    print(min(results))


