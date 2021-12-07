from statistics import mean, median

with open('input7.txt') as f:
    input = f.read().split(',')
positions = [int(i) for i in input]


# part 1 can be solved using the median
median_pos = int(median(positions))

median_fuel = 0
for num in positions:
    median_fuel += abs(num-median_pos)

print(median_fuel)

# part 2 can be solved by using the mean
# (finding the optimal position may involve rounding up or down)
mean_fuel = 0
mean_pos = int(mean(positions))

for num in positions:
    diff = abs(num-mean_pos)
    for i in range(diff):
        mean_fuel += 1 + (1 * i)

print(mean_fuel)
