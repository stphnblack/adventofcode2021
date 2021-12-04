import csv

# prep data
all_rows = []
with open('input4.txt') as f:
    first_row = f.readline().rstrip()
    reader = csv.reader(f, delimiter='\n')
    for row in reader:
        if row:
            all_rows.append(row[0].split())

bingo_calls = first_row.split(',')

bingo_boards = []

for i in range(0, len(all_rows), 5):
    bingo_boards.append([all_rows[i], all_rows[i+1],
                         all_rows[i+2], all_rows[i+3], all_rows[i+4]])


def get_winner(type):
    board_winners = {}
    winner = []
    break_out_flag = False
    for call in bingo_calls:
        # replace matches with 'x'
        for board in range(len(bingo_boards)):
            for row in range(5):
                if call in bingo_boards[board][row]:
                    bingo_boards[board][row][bingo_boards[board][row].index(call)] = 'x'

        # check for bingo
        # check for complete row
        for board in range(len(bingo_boards)):
            for row in range(5):
                if type == 'first':
                    if bingo_boards[board][row] == ['x', 'x', 'x', 'x', 'x']:
                        winner.append(bingo_boards[board])
                        break_out_flag = True
                        break
                else:
                    if bingo_boards[board][row] == ['x', 'x', 'x', 'x', 'x'] and board not in board_winners:
                        board_winners[board] = True
                        if len(board_winners) == len(bingo_boards):
                            winner.append(bingo_boards[board])
                            break_out_flag = True
                            break
            if break_out_flag:
                break
        if break_out_flag:
            break

        # check for complete column
        for board in range(len(bingo_boards)):
            for num in range(5):
                test_col = []
                for row in range(5):
                    if bingo_boards[board][row][num] == 'x':
                        test_col.append('x')
                if type == 'first':
                    if test_col == ['x', 'x', 'x', 'x', 'x']:
                        winner.append(bingo_boards[board])
                        break_out_flag = True
                        break
                else:
                    if test_col == ['x', 'x', 'x', 'x', 'x'] and board not in board_winners:
                        board_winners[board] = True
                        if len(board_winners) == len(bingo_boards):
                            winner.append(bingo_boards[board])
                            break_out_flag = True
                            break
            if break_out_flag:
                break
        if break_out_flag:
            break
    return (winner, call)


def calculate_score(board, call):
    score = 0
    for row in board[0]:
        for num in row:
            if num != 'x':
                score += int(num)
    return score * int(call)


first_winner, first_call = get_winner('first')
print(calculate_score(first_winner, first_call))

last_winner, last_call = get_winner('last')
print(calculate_score(last_winner, last_call))
