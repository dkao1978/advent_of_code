import fileinput


if __name__ == "__main__":
    inp = [x.strip().split(" | ") for x in fileinput.input()]

    p1_total, p2_total = 0,0
    for signal_pattern, output in inp:
        output = output.split(" ")
        sub_total = [x for x in output if len(x) in [2,3,4,7]]
        p1_total += len(sub_total)

        decode = {len(x): set(x) for x in signal_pattern.split(" ")}
        num = ""
        for x in output:
            has_4 = len(set(x)&set(decode[4]))
            has_2 = len(set(x)&set(decode[2]))
            match len(x), has_4, has_2:
                case 2, _, _: num += "1"
                case 3, _, _: num += "7"
                case 4, _, _: num += "4"
                case 7, _, _: num += "8"
                case 5, 2, _: num += "2"
                case 5, 3, 1: num += "5"
                case 5, 3, 2: num += "3"
                case 6, 4, _: num += "9"
                case 6, 3, 1: num += "6"
                case 6, 3, 2: num += "0"
        p2_total += int(num)

    print(p1_total)
    print(p2_total)

