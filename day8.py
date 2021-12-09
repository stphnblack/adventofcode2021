# prep data
with open('input8.txt') as f:
    input = f.read().split('\n')

prep_sig = []
prep_out = []
data = []

for line in input:
    data.append(line.split('|'))

for line in data[:-1]:
    prep_sig.append(line[0])
    prep_out.append(line[1])

output = []
signal = []

for line in prep_out:
    output.append(line.split())

for line in prep_sig:
    signal.append(line.split())


# part 1
def part1(output):
    unique_digits = 0
    for line in output:
        for num in line:
            if len(num) == 2 or len(num) == 4 or len(num) == 3 or len(num) == 7:
                unique_digits += 1

    return unique_digits


# part 2
def find_letters(signal, output):
    """fix codes by assigning scrambled letters to correct letters"""
    one = ''
    four = ''
    line_keys = []
    for line in signal:
        letter_counts = {}
        # count instances of letters
        for num in line:
            if len(num) == 2:
                one = num
            elif len(num) == 4:
                four = num
            for letter in num:
                if letter in letter_counts:
                    letter_counts[letter] += 1
                else:
                    letter_counts[letter] = 1
        # map scrambled letters to correct letters
        mapped_letters = {}
        for letter in letter_counts:
            if letter_counts[letter] == 8 and letter not in one:
                mapped_letters[letter] = 'a'
            elif letter_counts[letter] == 6:
                mapped_letters[letter] = 'b'
            elif letter_counts[letter] == 8 and letter in one:
                mapped_letters[letter] = 'c'
            elif letter_counts[letter] == 7 and letter in four:
                mapped_letters[letter] = 'd'
            elif letter_counts[letter] == 4:
                mapped_letters[letter] = 'e'
            elif letter_counts[letter] == 9:
                mapped_letters[letter] = 'f'
            elif letter_counts[letter] == 7 and letter not in four:
                mapped_letters[letter] = 'g'
        line_keys.append(mapped_letters)

    # convert output to standard format
    fixed_lines = []
    for index, line in enumerate(line_keys):
        fixed_nums = []
        for num in output[index]:
            temp_num = ''
            for letter in num:
                temp_num += line[letter]
            # alphabetize
            temp_sort = sorted(temp_num)
            temp_num = ''.join(temp_sort)
            fixed_nums.append(temp_num)
        fixed_lines.append(fixed_nums)

    return fixed_lines


def find_numbers(codes):
    """convert standardized letter-codes to digits"""
    output_digits = []
    key = {'abcefg': '0', 'cf': '1', 'acdeg': '2', 'acdfg': '3', 'bcdf': '4',
           'abdfg': '5', 'abdefg': '6', 'acf': '7', 'abcdefg': '8', 'abcdfg': '9'}
    for line in codes:
        output_line = []
        for num in line:
            output_line.append(key[num])
        output_digits.append(int(''.join(output_line)))

    return sum(output_digits)


print(part1(output))
print(find_numbers(find_letters(signal, output)))
