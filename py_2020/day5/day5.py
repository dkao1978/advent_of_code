import fileinput

if __name__ == "__main__":
    inp = [x.strip() for x in fileinput.input()]

    results = []
    for bp in inp: 
        rows = list(range(128))
        col = list(range(8))
        for ins in bp:
            row_width = len(rows) // 2
            col_width = len(col) // 2
            if ins == "F":
                rows = rows[:row_width]
            elif ins == "B":
                rows = rows[row_width:]
            elif ins == "L":
                col = col[:col_width]
            elif ins == "R":
                col = col[col_width:]
            # print(ins, rows, col)
        result = (rows[0] * 8) + col[0]
        results.append(result)
    print(sorted(results))
    print(set(list(range(952)))-set(results) )

