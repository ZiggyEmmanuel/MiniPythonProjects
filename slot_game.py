import random


MAX_LINES = 3
MAX_BET = 200
MIN_BET = 5

ROWS = 3
COLS = 3

symbol_count = {
        "A": 2,
        "B": 3,
        "C": 6,
        "D": 6,
 }

symbol_value = {
        "A": 5,
        "B": 8,
        "C": 5,
        "D": 5,
}


def check_winnings(columns, lines, bet, Values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_Check = column[line]
            if symbol != symbol_to_Check:
                break
        else:
            winnings += Values[symbol] * bet
            winnings_lines.append(line + 1)

    return winnings, winnings_lines


def get_slot_machine_spin(ROWS, COLS, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(COLS):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(ROWS):
            Value = random.choice(current_symbols)
            current_symbols.remove(Value)
            column.append(Value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(column) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()
    return columns


def deposit():
    while True:
        amount = input("How much would u like to deposit?: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid amount.")

    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")

    return lines


def get_bet():
    while True:
        amount = input("what would you like to bet? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a valid amount.")
    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"insufficient balance to bet that amount, your current balance is: ${balance}.")
        else:
            break

    print(f"you are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You Won ${winnings}.")
    print(f"You won on lines: {winnings_lines}")
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit.")
        if answer == "q":
            print(f"You left with ${balance}")
            quit()

        if balance < MIN_BET:
            print("You're out of cash, Good luck next time")
            print(f"You left with ${balance}")
            quit()
        balance += spin(balance)


main()
