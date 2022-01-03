
def check_passport(passport):
    passport = ' '.join(passport)
    # part 1
    # return ("byr" in passport) and \
    # ("iyr" in passport) and \
    # ("eyr" in passport) and \
    # ("hgt" in passport) and \
    # ("hcl" in passport) and \
    # ("ecl" in passport) and \
    # ("pid" in passport)
    # part 2
    valid = False
    if ("byr" in passport) and ("iyr" in passport) and \
            ("eyr" in passport) and ("hgt" in passport) and \
            ("hcl" in passport) and ("ecl" in passport) and ("pid" in passport):
        valid = True
        # split on spaces
        for pair in (passport.split(' ')):
            k, v = pair.split(':')
            if k == "byr":
                if not(1920 <= int(v) <= 2002):
                    print("bad year", v)
                    valid = False
                    break
            if k == "iyr":
                if not(2010 <= int(v) <= 2020):
                    print("bad iyr", v)
                    valid = False
                    break
            if k == "eyr":
                if not(2020 <= int(v) <= 2030):
                    print("bad eyr", v)
                    valid = False
                    break
            if k == "hgt":
                if v.endswith("cm"):
                    if not(150 <= int(v.strip("cm")) <= 193):
                        print("bad cm", v)
                        valid = False
                        break
                elif v.endswith("in"):
                    if not(59 <= int(v.strip("in")) <= 76):
                        print("bad in", v)
                        valid = False
                        break
                else:
                    print("bad heightcode", v)
                    valid = False
                    break
            if k == "hcl":
                if not(v.startswith('#') and all((c in "0123456789abcdef") for c in v[1:])):
                    print("bad hcl", v)
                    valid = False
                    break
            if k == "ecl":
                if v not in ["amb","blu","brn", "grn", "gry","hzl","oth"]:
                    print("bad ecl", v)
                    valid = False
                    break
            if k == "pid":
                if not(len(v) == 9 and int(v)):
                    print("bad pid", v)
                    valid = False
                    break
    return valid

def mk_passports(lines):
    passport = []
    good = 0
    for line in lines:
        if line != '':
            passport.append(line)
        else:
            if (check_passport(passport)):
                good += 1
                print("good:", passport)
            else:
                print("bad:", passport)
            passport = []
    print(good)

passport_input = []
with open("day4_input", "r") as f:
    for line in f:
        passport_input.append(line.strip('\n'))

# print(passport_input)
mk_passports(passport_input)

