import random
# generates random number
def random_number():
    return random.randint(1, 100)
# checks if user guess is correct
def guess_check(secret_number, guess):
    if secret_number == guess:
        return True
    return 'Lower' if secret_number < guess else 'Higher'
# guessing loop
def main():
    secret_number = random_number()
    while True:
        try:
            # asks user to guess a number
            guess = int(input('Guess a number between 1 and 100: '))
            if not 1 <= guess <= 100:
                print(f"('{guess}') not between 1-100")
                continue
            # checks the guess
            guess_result = guess_check(secret_number, guess)
            # if guessed ends game
            if guess_result == True:
                print(f"Congratulations, you guessed the number {secret_number}!")
                input()
                break
            # else says Higher or Lower
            print(f"{guess_result}!")
        # catches non integer inputs
        except ValueError:
            print("Input is not a number")
            continue
# runs called from main file
if __name__ == '__main__':
    main()