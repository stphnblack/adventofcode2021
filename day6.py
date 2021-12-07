with open('input6.txt') as f:
    input = f.read().split(',')
fish = [int(i) for i in input]

# parts 1 & 2
# keep track of how many fish are at each age
grouped_fish = []
for i in range(9):
    grouped_fish.append(sum([1 for j in fish if j == i]))


def get_population(days, grouped_fish):
    for i in range(days):
        temp_fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        if grouped_fish[0] == 0:
            for index, group in enumerate(grouped_fish):
                if index != 8:
                    temp_fish[index] = grouped_fish[index + 1]
        else:
            for index, group in enumerate(grouped_fish):
                if index != 8:
                    temp_fish[index] = grouped_fish[index + 1]
                if index == 6 or index == 8:
                    temp_fish[index] += grouped_fish[0]
        grouped_fish = temp_fish

    return sum(grouped_fish)


print(get_population(80, grouped_fish))
print(get_population(256, grouped_fish))
