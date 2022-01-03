
nums = []
with open("day1_input", "r") as f:
    for line in f:
        nums.append(int(line))

# part 1
# for numA in nums:
    # for numB in nums:
        # # find two entries that sum to 2020:
        # if (numA + numB == 2020):
            # print(numA, numB)

            # # their product is:
            # print(numA * numB)

# part 2
for numA in nums:
    for numB in nums:
        for numC in nums:
            # find two entries that sum to 2020:
            if (numA + numB + numC == 2020):
                print(numA, numB, numC)

                # their product is:
                print(numA * numB * numC)
