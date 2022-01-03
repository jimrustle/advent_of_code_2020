
passes = []
with open("day5_input", "r") as f:
    for line in f:
        passes.append(line.rstrip('\n'))

# print(passes)

def get_seat_id(boarding_pass):
    row_lower = 0
    row_upper = 127
    col_lower = 0
    col_upper = 7
    for i in range(7):
        # print(boarding_pass[i])
        if boarding_pass[i] == 'F':
            row_upper = row_lower + int((row_upper - row_lower)/2)
        else:
            row_lower += int((row_upper - row_lower)/2) + 1

    row = row_lower
    for i in range(7, 10):
        if boarding_pass[i] == 'L':
            col_upper = col_lower + int((col_upper - col_lower)/2)
        else:
            col_lower += int((col_upper - col_lower)/2) + 1

    col = col_lower
    return(row * 8 +  col) # part 1


# get_seat_id("FBFBBFFRLR")
# get_seat_id("BFFFBBFRRR")
# get_seat_id("FFFBBBFRRR")
# get_seat_id("BBFFBBFRLL")

# part 1
seats = list(map(get_seat_id, passes))
# print(seats)
# print(max(seats)) # 861
# print(min(seats)) # 100

# part 2
for i in range(101, 861):
    if i not in seats:
        print(i)
