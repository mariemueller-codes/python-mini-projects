import random

# global constant
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# number of columns and rows in the slot machine
ROWS = 3
COLUMNS = 3

# how many symbols in the reels
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_check = column[line]
            if symbol != symbol_check:
                break
        else:
            winings += values[symbol] * bet
            winnings_lines.append(line + 1)

    return winnings, winnings_lines


def get_slotmachine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


# print slot machine
def print_slotMachine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


# collecting user input that gets the deposit from the user
def deposit():
    while True:
        amt = input("How much you like to deposit? $ ")
        if amt.isdigit():
            amt = int(amt)
            if amt > 0:
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("Please enter a number.")

    return amt


# number of lines to bet
def get_num_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-"
                      + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


# collect the bet from the user
def get_bet():
    while True:
        amt = input("What would you like to bet on each line? ")
        if amt.isdigit():
            amt = int(amt)
            if MIN_BET <= amt <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amt


def spin(balance):
    lines = get_num_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet

        if total_bet > balance:
            print(f"Insufficient funds, your balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet}  on {lines} lines." +
          f" Total bet is equal to ${total_bet}.")

    # generate the slot machine
    slots = get_slotmachine_spin(ROWS, COLUMNS, symbol_count)
    print_slotMachine(slots)

    # TODO - Add conditional statement if user didn't win
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winnings}.")
    print(f"You won on lines: ", *winning_lines)

    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balace is : ${balance}")
        response = input("Press enter to spin (q to quit).")
        if response == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}.")


main()
