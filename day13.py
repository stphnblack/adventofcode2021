# prep data
with open('input13.txt') as f:
    input = f.read().splitlines()

dots = []
instructions = []
input.remove('')

for line in input:
    if line[0] in '0123456789':
        dots.append(line.split(','))
    else:
        instructions.append(line[11:].split('='))

dots = [[int(i) for i in row] for row in dots]


def display_grid(dots):
    """create & display grid"""
    max_x = max([i[0] for i in dots])
    max_y = max([i[1] for i in dots])
    for y in range(max_y + 1):
        print()
        for x in range(max_x + 1):
            if [x, y] in dots:
                print('#', end='')
            else:
                print('.', end='')


def fold(dots, axis, value):
    """fold paper based on given axis and location"""
    if axis == 'y':
        temp_dots = dots.copy()
        for coord in dots:
            x = coord[0]
            y = coord[1]
            if y > value:
                temp_dots.remove(coord)
                temp_dots.append([x, (value - (y-value))])
    else:
        temp_dots = dots.copy()
        for coord in dots:
            x = coord[0]
            y = coord[1]
            if x > value:
                temp_dots.remove(coord)
                temp_dots.append([(value - (x-value)), y])

    return temp_dots


def part1(dots):
    """counts number of unique dots"""
    unique_dots = []
    for coord in dots:
        if coord not in unique_dots:
            unique_dots.append(coord)
    return len(unique_dots)


def part2(dots, instructions):
    """implements fold instructions & displays the page"""
    for i in instructions:
        dots = fold(dots, i[0], int(i[1]))
    display_grid(dots)


print(part1(fold(dots, instructions[0][0], int(instructions[0][1]))))
part2(dots, instructions)
