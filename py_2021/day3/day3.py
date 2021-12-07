import fileinput

if __name__ == "__main__":
    input = [x.strip() for x in fileinput.input()]

    num_len = len(input[0])
    
    input = [int(x, 2) for x in input]
    
    # Part 1
    gamma = ""
    for idx in reversed(range(num_len)):
        ones = 0
        zeroes = 0
        for num in input:
            if (num >> idx) & 1 == 1:
                ones += 1
            else:
                zeroes += 1
        gamma += "1" if ones > zeroes else "0"
    gamma = int(gamma, 2)
    mask = (1<<num_len) - 1
    epsilon = gamma ^ mask
    print(gamma * epsilon)


    # part 2
    for idx in reversed(range(num_len)):
        ones = 0
        zeroes = 0
        for num in input:
            if (num >> idx) & 1 == 1:
                ones += 1
            else:
                zeroes += 1
        ones_input = [x for x in input if (x >> idx) & 1 == 1]
        zeroes_input = [x for x in input if (x >> idx) & 1 == 0]
        if len(ones_input) >= len(zeroes_input):
            input = ones_input
        else:
            input = zeroes_input
        if len(input) == 1:
            break
    oxygen = input[0]

    input = [x.strip() for x in fileinput.input()]
    num_len = len(input[0])
    
    input = [int(x, 2) for x in input]
    for idx in reversed(range(num_len)):
        ones = 0
        zeroes = 0
        for num in input:
            if (num >> idx) & 1 == 1:
                ones += 1
            else:
                zeroes += 1
        ones_input = [x for x in input if (x >> idx) & 1 == 1]
        zeroes_input = [x for x in input if (x >> idx) & 1 == 0]
        if len(ones_input) < len(zeroes_input):
            input = ones_input
        else:
            input = zeroes_input
        if len(input) == 1:
            break
    co2 = input[0]
    print(oxygen * co2)

