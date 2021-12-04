import fileinput
import re
import string


if __name__ == "__main__":

    needed_keys = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

    # part 1
    num_valid = 0
    passport = ""
    passports = []
    for line in fileinput.input():
        if line != "\n":
            passport += f" {line.strip()}"
        else:
            passports.append(passport)
            passport = ""
    passports.append(passport)

    for passport in passports:
        keys = re.findall(r"(\w{3}):([#0-9a-z]+)", passport)
        keys = {x[0]: x[1] for x in keys}
        if "cid" in keys:
            del keys["cid"]
        if len(keys) == len(needed_keys):
            num_valid += 1
    print(num_valid)

    # part 2
    num_valid = 0
    for passport in passports:
        keys = re.findall(r"(\w{3}):([#0-9a-z]+)", passport)
        keys = {x[0]: x[1] for x in keys}
        if "cid" in keys:
            del keys["cid"]
        if len(keys) != len(needed_keys):
            continue

        valid = True
        for key in keys.items():
            match key:
                case ("byr", year) if int(year) >= 1920 and int(year) <= 2002:
                    continue
                case ("iyr", year) if int(year) >= 2010 and int(year) <= 2020:
                    continue
                case ("eyr", year) if int(year) >= 2020 and int(year) <= 2030:
                    continue
                case ("hgt", height):
                    matches =  re.match(r"(\d+)(\w{2})", height)
                    if matches:
                        num, unit = matches.groups()
                    else:
                        print("invalid ", passport)
                        valid = False
                        break
                    if unit == "cm" and 150 <= int(num) <= 193:
                        continue
                    elif unit == "in" and 59 <= int(num) <= 76:
                        continue
                    else:
                        print("invalid ", passport)
                        valid = False
                        break
                case ("hcl", hair_color) if re.match(r"#[0-9a-f]{6}$", hair_color):
                    continue
                case ("ecl", eye_color) if eye_color in ["amb", "blu", "brn", "gry",
                                                         "grn", "hzl", "oth"]:
                    continue
                case ("pid", passport_id) if passport_id.isnumeric() and len(passport_id) == 9:
                    continue
                case _:
                    print("invalid ", passport, key)
                    valid = False
        if valid == True:
            num_valid += 1

    print(num_valid)
