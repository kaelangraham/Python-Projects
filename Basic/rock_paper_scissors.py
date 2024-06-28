import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def main():
    print('Rock Paper Scissors Game!\n\n')
    score = [0, 0]
    winning_score = 3
    cls()
    while True:
        try:
            print(f"You {score[0]} : Bot {score[1]}")
            usr_rps = int(input('1. Rock\n' + '2. Paper\n' + '3. Scissors\n'))
            if not 1 <= usr_rps <= 3:
                print(f"('{usr_rps}') not between 1-3")
                continue
            com_rps = random.choice([(1, 2, 'Rock'),(2, 3, 'Paper'),(3, 1, 'Scissors')])
            if usr_rps == com_rps[1]:
                print(f"You win! Bot played ('{com_rps[2]}')")
                score[0] += 1
            elif usr_rps == com_rps[0]:
                print("Draw!")
            else:
                print (f"You lost! Bot played ('{com_rps[2]}')")
                score[1] += 1
            if score[0] == winning_score:
                print("\nYou won!" + f"The final score was - You {score[0]} : Bot {score[1]}")
                input()
                break
            if score[1] == winning_score:
                print("\nYou lost!" + f"The final score was - You {score[0]} : Bot {score[1]}")
                input()
                break
            input('Press Enter to continue...')
            cls()
            
        except ValueError:
            print('Input is not a number')
            continue

if __name__ == "__main__":
    main()