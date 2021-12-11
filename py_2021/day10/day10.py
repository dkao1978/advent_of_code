import fileinput

if __name__ == "__main__":
    inp = [x.strip() for x in fileinput.input()]

    illegal_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    autocomplete_points = {")": 1, "]": 2, "}": 3, ">": 4}
    pairs = [("(", ")"), ("{", "}"), ("[", "]"), ("<", ">")]
    left = [x[0] for x in pairs]
    left_to_right = {x[0]: x[1] for x in pairs}
    right_to_left = {x[1]: x[0] for x in pairs}

    illegal = []
    unclosed = []
    results = []

    for line in inp:
        stack = []
        for cmd_idx in range(len(line)):
            cmd = line[cmd_idx]
            if cmd in left:
                stack.append(cmd)
            else:
                open_cmd = stack.pop()
                if open_cmd != right_to_left[cmd]:
                    illegal.append(cmd)
                    break
        else:
            # unclosed.append(reversed(stack))
            sub_total = 0
            for y in reversed(stack):
                sub_total *= 5
                sub_total += autocomplete_points[left_to_right[y]]
            results.append(sub_total)

    print(sum([illegal_points[x] for x in illegal]))
    print(sorted(results)[len(results) // 2])
