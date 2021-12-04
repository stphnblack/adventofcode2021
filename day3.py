with open('input3.txt') as f:
    input = f.read()
readout = input.split()


def part1(data):
    readout = data
    binary_length = len(readout[0])

    gamma = []
    epsilon = []

    for i in range(binary_length):
        count1 = 0
        count0 = 0
        for binary in readout:
            if binary[i] == '0':
                count0 += 1
            else:
                count1 += 1
        if count0 > count1:
            gamma.append('0')
            epsilon.append('1')
        else:
            gamma.append('1')
            epsilon.append('0')

    gamma_decimal = int(''.join(gamma), 2)
    epsilon_decimal = int(''.join(epsilon), 2)

    return gamma_decimal * epsilon_decimal


# part 2
def part2(gas, data):
    readout = data
    index = 0
    while len(readout) > 1:
        count1_2 = 0
        count0_2 = 0
        for binary in readout:
            if binary[index] == '0':
                count0_2 += 1
            else:
                count1_2 += 1
        if count0_2 > count1_2:
            if gas == 'o2':
                to_remove = '1'
            else:
                to_remove = '0'
        else:
            if gas == 'o2':
                to_remove = '0'
            else:
                to_remove = '1'
        # remove binary with specified digit from readout
        readout = [i for i in readout if not i[index:index+1] == to_remove]
        index += 1
        if len(readout) == 1:
            result = readout

    return result


print(part1(readout))

o2_decimal = int(''.join(part2('o2', readout)), 2)
co2_decimal = int(''.join(part2('co2', readout)), 2)
print(o2_decimal * co2_decimal)
