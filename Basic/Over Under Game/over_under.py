import random
import os
import time
DIR = os.path.dirname(__file__)
starting_balance = 100

# finds money location
data_path = "Data Storage/money.txt"
money_path = os.path.join(DIR, data_path)
min_bet = 10

def title_bal():
    cls()
    print('Over Under')
    print(f"Balance: ${balance}\n")

# clears screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def find_balance():
    try:
        # read data
        data=open(money_path)
        data_read = data.read()
        data.close()
        return int(data_read)
    except:
        # sets money to starting balance
        data=open(money_path, "w")
        data.write(str(starting_balance))
        data.close()
        # read data
        data=open(money_path)
        data_read = data.read()
        data.close()
        return int(data_read)
    
def edit_balance(value):
    # changes balance based on passed value
    if value == 'reset':
        new_balance = starting_balance
    else:
        new_balance = find_balance() + value
    data=open(money_path, "w")
    data.write(str(new_balance))
    data.close()
    # updates balance variable
    global balance
    balance = new_balance

    
    
def user_bet():
    while True:
        title_bal()
        # user enters a bet
        try:
            bet = int(input(f'Enter a bet (min: ${min_bet}): $'))
        # checks if bet is a number
        except ValueError:
            print('Input is not a number!')
            input('Press Enter to continue...')
            continue
        # checks if bet is valid
        if bet < min_bet:
            print(f'Bet is too low (min: ${min_bet})')
            input('Press Enter to continue...')
            continue
        elif bet > balance:
            print(f'Not enought money (Balance: {balance})')
            input('Press Enter to continue...')
            continue
        break
    # edits the balance + returns bet
    edit_balance(-bet)
    return bet

def user_bet_type(bet):
    while True:
        title_bal()
        print(f"Bet: ${bet}\n")
        # user enters a bet type
        try:
            bet_type = int(input('Enter a bet type\n'+'1. (1-6) x2\n'+'2. (7) x12\n'+'3. (8-13) x2\n'))
        # checks if number
        except ValueError:
            print('Input is not a number!')
            input('Press Enter to continue...')
            continue
        # checks if valid option
        if not 1 <= bet_type <= 3:
            print(f"('{bet_type}') is not a valid option")
            input('Press Enter to continue...')
            continue
        break
    # returns bet type
    return bet_type

def roll(roll_display):
    rolls = random.randint(5, 30)
    roll_result = random.randint(1, 13)
    for i in range(rolls):
        # rolling display
        title_bal()
        print(roll_display)
        print(random.randint(1,13))
        time.sleep(0.05)
    # final display
    title_bal()
    print(roll_display)
    print(roll_result)
    return roll_result





def number_roll(bet, bet_type):
    title_bal()
    # displays bet and bet type
    if bet_type != 2:
        roll_display = f"Bet: ${bet} on {bet_types[bet_type][0]}-{bet_types[bet_type][1]}\n"
    else:
        roll_display = f"Bet: ${bet} on {bet_types[bet_type][0]}\n"
    print(roll_display)
    input("Press Enter to roll...")
    number = roll(roll_display)
    # if loss
    if not bet_types[bet_type][0] <= number <= bet_types[bet_type][1]:
        print('You Lost!')
        return False
    # if win
    print('You Won!')
    return True


def main():
    global balance
    global bet_types
    bet_types = {1:(1,6), 2:(7,7), 3:(8,13)}
    while True:
        balance = find_balance()
        title_bal()
        # main menu
        try:
            option = int(input('1. Play\n'+'2. Exit\n'+'3. Reset Balance ($100)\n'+'4. How to Play?\n'))
            # if invalid option
            if not 1 <= option <= 4:
                print(f"('{option}') is not a valid option")
                input('Press Enter to continue...')
                continue
            # if input is not a number
        except ValueError:
            print('Input is not a number!')
            input('Press Enter to continue...')
            continue
        # exit
        if option == 2:
            break
        # reset balance
        elif option == 3:
            title_bal()
            edit_balance('reset')
            print('Balance reset!')
            input('Press Enter to continue...')
            continue
        # how to play
        elif option == 4:
            title_bal()
            print("1. Place a bet between min bet and your total balance")
            print("2. Choose a bet option (1-6) x2, (7) x12, (8-13) x2")
            print("3. Win = Bet x multplier")
            print("4. Loss = 0")
            input('\nPress Enter to continue...')
            continue
        # checks if player has enough to bet
        if not balance >= min_bet:
            title_bal()
            print(f"Can't afford min bet! (min: ${min_bet})")
            input('Press Enter to continue...')
            continue
        # plays game
        bet = user_bet()
        bet_type = user_bet_type(bet)
        result = number_roll(bet, bet_type)
        if result:
            if bet_type == 2:
                edit_balance(bet*12)
            else:
                edit_balance(bet*2)
        input('Press Enter to continue...')

if __name__ == '__main__':
    main()