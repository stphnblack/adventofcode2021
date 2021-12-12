# prep data
with open('input11.txt') as f:
    input = f.read().splitlines()

octo_map = []
for row in input:
    temp_row = []
    for num in row:
        temp_row.append(int(num))
    octo_map.append(temp_row)

num_flashed = 0


def flash(flashing_octos, map, flashed_octos):
    """"using a list of flashing octos, recursively resolve all flashes"""
    global num_flashed
    temp_flashing_octos = []

    # keep track of octos that have already flash to pass to the isValid func
    for coord in flashing_octos:
        flashed_octos.append(coord)

    for coord in flashing_octos:
        row = coord[0]
        col = coord[1]
        poss_neighbors = [[row + 1, col], [row - 1, col], [row, col + 1],
                          [row, col - 1], [row + 1, col + 1], [row + 1, col - 1],
                          [row - 1, col + 1], [row - 1, col - 1]]
        valid_neighbors = []

        # create list of valid neighbors & increment by 1
        for cell in poss_neighbors:
            if isValid(cell, flashed_octos):
                valid_neighbors.append(cell)

        for cell in valid_neighbors:
            map[cell[0]][cell[1]] += 1
            if map[cell[0]][cell[1]] > 9:
                temp_flashing_octos.append(cell)
                num_flashed += 1

        # keep track of neighbor octos that will flash this step
        for coord in temp_flashing_octos:
            flashed_octos.append(coord)

    # set flashed octos to 0
    for cell in flashed_octos:
        map[cell[0]][cell[1]] = 0

    # call this function for any neighbors that have flashed
    if temp_flashing_octos:
        flash(temp_flashing_octos, map, flashed_octos)

    return map


def isValid(coord, flashed_octos):
    """return false for all octos that are outside grid or already flashed"""
    row = coord[0]
    col = coord[1]
    max_row = 10
    max_col = 10
    if (row < 0 or col < 0 or row >= max_row or col >= max_col):
        return False
    if coord in flashed_octos:
        return False
    return True


def get_num_flashes(octo_map, steps):
    """return number of flashes based on given number of steps"""
    global num_flashed
    for step in range(steps):
        flashing_octos = []

        # PART 2
        # check if all octos have flashed, & if so, print the step it occurred
        map_sum = 0
        for row in octo_map:
            map_sum += sum(row)

        if map_sum == 0:
            print(f'all octos flashed on step {step}')

        # increase energy levels by 1
        for row_index, row in enumerate(octo_map):
            for col_index, num in enumerate(row):
                octo_map[row_index][col_index] += 1

        # locate all octopuses whose energy > 9
        for row_index, row in enumerate(octo_map):
            for col_index, num in enumerate(row):
                if num > 9:
                    flashing_octos.append([row_index, col_index])
                    num_flashed += 1

        # if there are flashing octos, call the flash function
        if flashing_octos:
            octo_map = flash(flashing_octos, octo_map, [])

    return num_flashed


print(get_num_flashes(octo_map, 100))
