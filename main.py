# python slot machine project
# TechWithTim youtube video: https://www.youtube.com/watch?v=th4OBktqK1I&t=2483s&ab_channel=TechWithTim

import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


# slot machines
ROWS = 3
COLS = 3

symbols = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value ={
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def get_slot_machine_spin(rows, cols, symbols):
    # what symbols are going to show up when the slot machine is spun
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        # current_symbols = all_symbols.copy()
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machines(columns):
    # [A, B, C] -> col1
    # [A, A, C] -> col2
    # [B, A, A] -> col3

    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row])

def check_winnings(columns, lines, bet, values):
    # 1 line bet - top line
    # 2 line bet - top and middle
    # 3 line bet - check all lines

    winnings = 0
    winning_lines = []
    # remember range(3) -> 0, 1, 2
    for line in range(lines):
        first_col_symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if first_col_symbol == symbol_to_check:
                # match, go to next column
                pass
            else:
                # some symbol on the row didn't match the first column symbol, not a winning row
                break
        else:
            # all columns have the same symbol, winning row
            winning_lines.append(lines + 1)
            winnings += values[first_col_symbol] * bet

    return winnings, winning_lines



def deposit():
    while True:
        amount = input("how much is your deposit? $")
        if amount.isdigit():
            # -ve false
            # alpha fasle
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("deposit must be greater than 0")
        else: 
            print("give number")
    return amount

def get_number_of_lines():
    while True:
        lines = input("how many lines do you want to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("give valid number of lines")
        else: 
            print("give number")
    return lines    

def get_bet():
    while True:
        amount = input("how much you want to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"bet amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("give number")
    return amount

def spin(balance):
    # bet on ?# lines
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print(f"you dont have enough balance to bet that amount. your current balance is ${balance}.")
        else:
            break
        
    print(f"you are betting ${bet} on {lines} lines. total bet amount ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbols)
    print_slot_machines(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)

    print(f"you win ${winnings}")
    print(f"you won on lines: ", *winning_lines)

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"currnet balance is ${balance}")
        answer = input("press enter to play (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"you left with ${balance}")
    

# main
main() 
# print_slot_machines(get_slot_machine_spin(ROWS, COLS, symbols))