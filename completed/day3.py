map_input = []
with open("day3_input", "r") as f:
    for line in f:
        map_input.append(line.strip('\n'))

def expand_map(map_input):
    map_depth = len(map_input)
    map_width = len(map_input[0])
    new_map = []
    for line in map_input:
        new_map.append(line * 7 * int(map_depth/map_width + 1))
    # print('y', len(new_map), 'x', len(new_map[0]))
    return new_map

def step(map_input, xstep, ystep):
    x = 0
    y = 0
    tree = 0
    while y < len(map_input):
        if map_input[y][x] == '#':
            tree +=1
        x += xstep
        y += ystep
        # print(y, x)
    return tree

# print(map_input)
# print(expand_map(map_input))

# part 1
print(step(expand_map(map_input), 3, 1))

# part 2
print(step(expand_map(map_input), 1, 1) *
      step(expand_map(map_input), 3, 1) *
      step(expand_map(map_input), 5, 1) *
      step(expand_map(map_input), 7, 1) *
      step(expand_map(map_input), 1, 2))

