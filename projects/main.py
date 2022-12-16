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


def get_slotmachine_spin(rows, columns, symbols):



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


def main():
    balance = deposit()
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
    # print(balance, lines, bet)


main()
