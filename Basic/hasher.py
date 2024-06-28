# random generator
import random
# allows automatic copy to clipboard
import subprocess
def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)
# hashes an inputted password + generates a random hashing factor (stores hashing factor inside hashed password)
def hash_password(password):
    # generates random hashing factor + hash indetifier
    hashing_factor = random.randint(-79, -1)
    if len(str(hashing_factor * (-1))) != 2:
        password_hash = [0, hashing_factor * (-1)]
    else:
        password_hash = [int(str(hashing_factor)[1]), int(str(hashing_factor)[2])]
    # hash indetifier start
    hashed_password = chars[password_hash[0]]+chars[password_hash[1]]
    for i in range(password_hash[0]):
        random_index = random.randint(0,79)
        hashed_password += chars[random_index]
    # hashes password
    for i in password:
        char_index = chars.index(i)
        hashed_password += chars[char_index + hashing_factor]
    # hash identifier end
    for i in range(password_hash[1]):
        random_index = random.randint(0,79)
        hashed_password += chars[random_index]
    return hashed_password

# unhashes a password using hashed password and hashing factor
def dehash_password(hashed_password):
    # finds hashing factor
    password_hash = chars.index(hashed_password[0]), chars.index(hashed_password[1])
    hashing_factor = int(str(password_hash[0]) + str(password_hash[1])) * (-1)
    hashed_password = hashed_password[2+password_hash[0]:-password_hash[1]]
    password = ''
    for i in hashed_password:
        char_index = chars.index(i)
        password += chars[(char_index - hashing_factor) % len(chars)]
    return password

# list of characters
global chars
chars = ['9', '6', '%', '$', 'O', '8', 'l', '~', 'o', '2', 
         'S', 'z', 'N', '*', '!', 'u', 'V', ':', 'X', 'e', 
         'B', 'C', '&', 'M', 'k', '_', 'p', '3', '=', '/', 
         'R', 'b', '?', 'y', 'x', 's', 'P', '-', 'T', 'W', 
         'v', '+', 'U', 'L', '4', 'i', 'G', 'w', 'a', ';', 
         'h', 't', 'Y', 'E', '0', 'K', 'g', 'd', 'I', '#', 
         'H', 'Q', 'j', 'Z', '@', 'F', 'm', '7', 'D', 'q', 
         '1', 'J', 'f', 'A', 'r', '^', '`', 'c', 'n', '5']
def main():
    while True:
        user_input = input('Password Hasher\n' + '1. Hash a Password\n' + '2. Dehash a Password\n' + '3. Exit\n')
        # exit
        if user_input == '3':
            break
        # hash a password
        elif user_input == '1':
            user_password = input('Enter a password to be hashed:\n')
            hashed_password = str(hash_password(str(user_password)))
            print(hashed_password)
            copy2clip(hashed_password)
            input('Copied to clipboard, press enter to continue...')
            # dehash a password
        elif user_input == '2':
            user_hashed_password = input('Enter a password to be dehashed:\n')
            password = str(dehash_password(str(user_hashed_password)))
            print(password)
            copy2clip(password)
            input('Copied to clipboard, press enter to continue...')
            # bad input
        else:
            print(f'Invalid Input ("{user_input}")')
if __name__ == '__main__':
    main()