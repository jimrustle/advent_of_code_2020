
mins = []
maxes = []
letters = []
passwords = []
with open("day2_input", "r") as f:
    for line in f:
        first, second = line.split(':')
        first = first.split('-')
        mins.append(int(first[0]))
        maxes.append(int(first[1].split(' ')[0]))
        letters.append(first[1].split(' ')[1])
        passwords.append(second.lstrip(' ').rstrip('\n'))

def valid(min_l, max_l, letter, password):
    count = password.count(letter)
    return (min_l <= count) and (count <= max_l)

def valid2(index1, index2, letter, password):
    # print(index1, index2, letter, password)
    return ((password[index1-1] == letter) and (password[index2-1] != letter)) or ((password[index1-1] != letter) and (password[index2-1] == letter))

# part 1
# total = 0
# for (mn, mx, l, p) in zip(mins, maxes, letters, passwords):
    # if valid(mn, mx, l, p):
        # total += 1

# print(total)

# part 2
total = 0
for (mn, mx, l, p) in zip(mins, maxes, letters, passwords):
    # print(valid2(mn, mx, l, p), mn, mx, l, p)
    if valid2(mn, mx, l, p):
        total += 1

print(total)

