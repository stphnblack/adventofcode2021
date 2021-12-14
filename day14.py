# prep data
with open('input14.txt') as f:
    template = f.readline().rstrip()
    input = f.read().splitlines()[1:]

rules = {}
for i in input:
    rules[i.split(' -> ')[0]] = i.split(' -> ')[1]


def polymers(template, rules, steps):
    # create pairs from initial template
    old_pairs = {}
    for i, char in enumerate(template):
        if i < len(template) - 1:
            pair = template[i] + template[i+1]
            if pair in old_pairs:
                old_pairs[pair] += 1
            else:
                old_pairs[pair] = 1
    # keep track of how many times each pair occurs after x number of steps
    new_pairs = {}
    for step in range(steps):
        if new_pairs != {}:
            old_pairs = new_pairs.copy()
        new_pairs = {}

        for pair in old_pairs:
            new1 = pair[0] + rules[pair]
            new2 = rules[pair] + pair[1]
            mult = old_pairs[pair]

            if new1 in new_pairs:
                new_pairs[new1] += 1 * mult
            if new2 in new_pairs:
                new_pairs[new2] += 1 * mult

            if new1 not in new_pairs:
                new_pairs[new1] = 1 * mult
            if new2 not in new_pairs:
                new_pairs[new2] = 1 * mult

    # count number of occurences for each letter
    letter_counts = {}
    for pair in new_pairs:
        letter = pair[1]
        if letter in letter_counts:
            letter_counts[letter] += new_pairs[pair]
        else:
            letter_counts[letter] = new_pairs[pair]
    if 'N' in letter_counts:
        letter_counts['N'] += 1
    else:
        letter_counts['N'] = 1

    return max(letter_counts.values()) - min(letter_counts.values())


print(polymers(template, rules, 10))
print(polymers(template, rules, 40))
