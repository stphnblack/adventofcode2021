course = []

with open('input2.txt') as f:
    for line in f:
        (direction, distance) = line.split()
        course.append((direction, int(distance)))


def part1():
    horizontal = 0
    depth = 0
    for move in course:
        if move[0] == 'forward':
            horizontal += move[1]
        elif move[0] == 'up':
            depth -= move[1]
        else:
            depth += move[1]

    return horizontal*depth


def part2():
    horizontal = 0
    depth = 0
    aim = 0
    for move in course:
        if move[0] == 'forward':
            horizontal += move[1]
            depth += aim*move[1]
        elif move[0] == 'up':
            aim -= move[1]
        else:
            aim += move[1]

    return horizontal*depth


print(part1())
print(part2())
