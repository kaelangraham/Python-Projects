import random as r
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# variables
wins = {
    'xx' : 3,
    'xxx': 8,
    '77' : 8,
    '777': 25,
}

def sim(starting_bal, spins, bet):
    bal = starting_bal
    win = 0
    for i in range(1, spins+1):
        roll = {}
        if bal - bet < 0:
            spins = i
            break           
        bal -= bet 
        # 3 columns
        for i in range(1,4):
            roll[i] = r.randint(1,7)

        # check if win
        if roll[1] == roll[2] == roll[3]:
            if roll[1] == 7:
                # win (777)
                bal += (bet*wins['777'])
                win += 1
            # win (xxx)
            bal += (bet*wins['xxx'])
            win += 1
        else:
            isDub = [roll[1] == roll[2], roll[2] == roll[3], roll[3] == roll[1]]
            if any(isDub):
                if roll[isDub.index(True)+1] == 7:
                    # win (77)
                    bal += (bet*wins['77'])
                    win += 1
                # win (xx)
                bal += (bet*wins['xx'])
                win += 1
    return {'bal': bal, 'spins': spins, 'wins': win}

def user_check(a):
    if a=='x':
        return True
    try:
        int(a)
    except ValueError:
        return False
    return 

def main():
    while True:
        cls()
        print("Make Money Calculator")
        print("=====================")
        print("Type 'x' to quit")
        starting_bal = input("Enter starting bal: $")
        if user_check(starting_bal):
            break
        elif user_check(starting_bal) == False:
            continue
        spins = input("Number of spins: ")
        if user_check(spins):
            break
        elif user_check(spins) == False:
            continue
        bet = input("Bet per spin: ")
        if user_check(bet):
            break
        elif user_check(bet) == False:
            continue
        results = (sim(int(starting_bal), int(spins), int(bet)))
        print("\n")
        print(f"Total Money: ${results['bal']}")
        print(f"Total Spins: {results['spins']}")
        print(f"Total Return: {results['bal']/int(starting_bal):.2f}")
        print(f"Money per spin: +${(results['bal']-int(starting_bal))/results['spins']:.2f}")
        print(f"Win/Loss: {results['wins']}/{results['spins']-results['wins']}")
        print("\n")
        input("Press Enter to continue...")

if __name__ == '__main__':
    main()