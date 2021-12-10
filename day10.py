from statistics import median

# prep data
with open('input10.txt') as f:
    lines = f.read().splitlines()

# use a stack to iterate through symbols
# keep track of corrupting symbols
# create list of symbols that complete incomplete lines
open_symbols = '([{<'
close_symbols = ')]}>'
symbol_pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
rev_symbol_pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
corrupting = []
completing = []
for line in lines:
    stack = []
    completing_symbols = []
    break_flag = False
    while True:
        for symbol in line:
            if symbol in open_symbols:
                stack.append(symbol)
            else:
                if stack[-1] == symbol_pairs[symbol]:
                    stack.pop()
                else:
                    corrupting.append(symbol)
                    break_flag = True
                    break
        if break_flag:
            break
        # if the line is incomplete
        for symbol in stack:
            completing_symbols.append(rev_symbol_pairs[symbol])
        completing_symbols.reverse()
        completing.append(completing_symbols)
        break

# calculate score for part 1
corrupt_score = 0
for symbol in corrupting:
    if symbol == ')':
        corrupt_score += 3
    elif symbol == ']':
        corrupt_score += 57
    elif symbol == '}':
        corrupt_score += 1197
    else:
        corrupt_score += 25137

print(corrupt_score)

# calculate score for part 2
total_complete_score = []
for line in completing:
    complete_score = 0
    for symbol in line:
        if symbol == ')':
            complete_score = (complete_score * 5) + 1
        elif symbol == ']':
            complete_score = (complete_score * 5) + 2
        elif symbol == '}':
            complete_score = (complete_score * 5) + 3
        else:
            complete_score = (complete_score * 5) + 4
    total_complete_score.append(complete_score)

print(median(total_complete_score))
