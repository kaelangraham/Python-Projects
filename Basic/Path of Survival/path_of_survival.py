import random
import os
import time
# Settings

# Encounters (must total 100)
encounter_nothing = 35
encounter_enemy = 20
encounter_discovery = 25
encounter_story = 15
encounter_ally = 5


# encounter nothing thought
def generate_thought():
    situations = {
        "I wonder": [
            "if I'll find food", "if anyone is left", "if it's safe to rest",
            "what happened to my family", "how it all went wrong"
        ],
        "I fear": [
            "the darkness", "being alone", "running out of supplies",
            "the mutants", "what's ahead"
        ],
        "I hope": [
            "to find other survivors", "to see the sun again", "for a better tomorrow",
            "to make it through the night", "for some relief"
        ],
        "I remember": [
            "the days before the fall", "my family", "the world as it was",
            "the good times", "the old normal"
        ],
        "I can't believe": [
            "this is real", "the world ended", "I'm still alive",
            "everything is gone", "this nightmare continues"
        ],
        "I struggle with": [
            "hunger", "fear", "loneliness", "fatigue", "hope"
        ],
        "I wish": [
            "this was a bad dream", "for a miracle", "for more strength",
            "to go back in time", "for a safe place"
        ],
        "I think about": [
            "survival", "finding food", "the future", "the past", "what to do next"
        ]
    }

    conditions = [
        "in this wasteland", "among the ruins", "in the dark", "with each step",
        "each passing day", "with little supplies", "as night falls",
        "under the dark sky"
    ]

    introspection = random.choice(list(situations.keys()))
    situation = random.choice(situations[introspection])
    condition = random.choice(conditions)

    thought = f"{introspection} {situation} {condition}."
    return thought

def generate_enemy():
    # [(chance): ('name', dmg, acc, speed, crit)]
    weapons = {(1, 8): ('Fists', 8, 80, 2, 35), (9, 13): ('Rusty pipe', 25, 60, 1, 45),
               (14, 19): ('Pocket Knife', 10, 85, 3, 20), (20, 27): ('Pistol', 17, 65, 3, 40),
               (28, 35): ('Shotgun', 35, 90, 1, 45), }
    enemy_level = random.randint(1, player_stats[0]+4)
    enemy_weapon_num = random.randint(1, 10)+enemy_level
    for prob1, prob2 in weapons:
        if not prob1 <= enemy_weapon_num <= prob2:
            continue
        enemy_weapon = weapons[(prob1, prob2)]
    # stats (lvl, hp, str, spd)
    enemy_stats = (enemy_level, 100+(enemy_level*8), random.randint(1, enemy_level+2), random.randint(1, enemy_level+2))
    return enemy_stats, enemy_weapon






def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# displays info about the player (health/hunger/etc)
def main_display():
    cls()
    print(f'Player: {player_name} - Level: {player_stats[0]} - Money: {player_stats[6]}g')
    print(f'Health: {player_health}/{player_stats[1]} - Energy: {player_energy}/{player_stats[3]}')
    print(f'Hunger: {player_hunger}/{player_stats[4]} - Thirst: {player_thirst}/{player_stats[5]}')
    print(f'Weapon: {player_weapon[0]}\n')

def fuel_loss():
    global player_health
    global player_hunger
    global player_health
    # hunger loss
    hunger_loss = random.uniform(0, 3)
    if player_hunger == 0:
        player_health = round((player_health-hunger_loss), 1)
    elif player_hunger - hunger_loss <= 0:
        player_hunger = 0
    else:
        player_hunger = round((player_hunger-hunger_loss), 1)
    # thirst loss
    global player_thirst
    thirst_loss = random.uniform(0, 3)
    if player_thirst == 0:
        player_health = round((player_health-thirst_loss), 1)
    elif player_thirst - thirst_loss <= 0:
        player_thirst = 0
    else:
        player_thirst = round((player_thirst-thirst_loss), 1)
    # health gain
    if not player_health == 100:
        player_health += random.randint(2,5)
    if player_health > 100:
        player_health = 100

    

def is_alive():
    global player_health
    if player_health <= 0:
        player_health = 0
        main_display()
        print('You died')
        input('Press Enter to continue...')
        return False
    return True

player_name = 'greg'
player_health = 100
player_energy = 100
player_hunger = 100
player_thirst = 100
player_weapon = ('Fists', 8, 80, 2, 35)
# (lvl, hp, str, energy, hunger, thirst, money, speed)
player_stats = (1, 100, 1, 100, 100, 100, 0, 1)
player_inventory = []

def inventory():
    exit_num = 1
    while True:
        main_display()
        if len(player_inventory) == 0:
            print("No items!")
        for i, item in player_inventory:
            print(f'{i}. {item[0]}')
            exit_num += 1
        print(f'{exit_num}. Exit')
        try:
            player_choice = int(input())
        except ValueError:
            print('Input is not a number')
            input('Press Enter to continue...')
            continue
        if player_choice == exit_num:
            break
    

def battle_display(opp, enemy_health):
    level = opp[0][0]
    max_health = opp[0][1]
    strength = opp[0][2]
    weapon = opp[1][0]
    print(f'\nEnemy - Level: {level} - Health: {enemy_health}/{max_health}')
    print(f'Strength: {strength} - Weapon: {weapon}\n')

def battle(opp):
    global enemy_health
    enemy_health = opp[0][1]
    run_chance = 50 + ((player_stats[7]-opp[0][3])*7)
    if run_chance < 0: run_chance = 0
    elif run_chance > 100: run_chance = 100
    while True:
        main_display()
        battle_display(opp, enemy_health)
        try:
            player_choice = int(input("1. Attack\n"+"2. Rest\n"+f"3. Run ({run_chance}%)\n"))
        except ValueError:
            print('Input is not a number')
            input("Press Enter to continue...")
            continue
        if not 1 <= player_choice <= 3:
            print(f"('{player_choice}') is not a valid option!")
            input("Press Enter to continue...")
            continue
        if player_choice == 2:
            print("rest")
            input()
            continue
        elif player_choice == 3:
            run_roll = random.randint(1, 100)
            if run_roll > run_chance:
                print("Could not escape!")
                input("Press Enter to continue...")
                if enemy_attack(opp):
                    return True
                continue
            print("Escape Successful!")
            return False
        if player_energy == 0:
            print('Energy too low')
            input("Press Enter to continue...")
            continue
        if plr_attack(opp):
            return False
        if enemy_attack(opp):
            return True
        
        

def plr_attack(opp):
    global player_energy
    player_energy -= 10
    if player_energy < 0:
        player_energy = 0
    # speed
    global enemy_health
    dmg = 0
    prev_atks = []
    main_display()
    battle_display(opp, enemy_health)
    for i in range(player_weapon[3]):
        # if attack hit
        hit_roll = random.randint(1, 100)
        if hit_roll > player_weapon[2]:
            # miss
            print("miss")
            prev_atks.append('miss')
            time.sleep(1/player_weapon[3])
            continue
        dmg = player_weapon[1] + random.randint(0,4)*player_stats[2]
        prev_atks.append(dmg)
        enemy_health -= dmg
        if not enemy_health <= 0:
            main_display()
            battle_display(opp, enemy_health)
            for _ in range(i+1):
                if prev_atks[_] == 'miss':
                    print('miss')
                    continue
                print(f'Hit enemy with {player_weapon[0]} for {prev_atks[_]}dmg')
            time.sleep(1/player_weapon[3])
            continue
        main_display()
        print("Enemy Defeated!\n")
        return True
    input('Press Enter to continue...\n')
    return False
        
def enemy_attack(opp):
    # speed
    global player_health
    dmg = 0
    prev_atks = []
    main_display()
    battle_display(opp, enemy_health)
    for i in range(opp[1][3]):
        # if attack hit
        hit_roll = random.randint(1, 100)
        if hit_roll > opp[1][2]:
            # miss
            print("miss")
            prev_atks.append('miss')
            time.sleep(1/opp[1][3])
            continue
        dmg = opp[1][1] + random.randint(0,4)*opp[0][2]
        prev_atks.append(dmg)
        player_health -= dmg
        if not player_health <= 0:
            main_display()
            battle_display(opp, enemy_health)
            for _ in range(i+1):
                if prev_atks[_] == 'miss':
                    print('miss')
                    continue
                print(f'Enemy hit {player_name} with {opp[1][0]} for {prev_atks[_]}dmg')
            time.sleep(1/opp[1][3])
            continue
        return True
    input('Press Enter to continue...\n')
    return False

def discover_item():
    items_junk = []
    items_supplies = []
    items_weapons = []
    items_other = []


    



encounter_enemy += encounter_nothing
encounter_discovery += encounter_enemy
encounter_story += encounter_discovery
encounter_ally += encounter_story
def generate_encounter():
    encounter_type = random.randint(1, 100)
    # nothing
    if 1 <= encounter_type <= encounter_nothing:
        print(generate_thought())
    # enemy
    elif encounter_nothing+1 <= encounter_type <= encounter_enemy:
        enemy = generate_enemy()
        return battle(enemy)
    # discovery
    elif encounter_enemy+1 <= encounter_type <= encounter_discovery:
        item = discover_item()
    # story
    elif encounter_discovery+1 <= encounter_type <= encounter_story:
        print('story')
    # ally
    elif encounter_story+1 <= encounter_type <= encounter_ally:
        print('ally')
    global player_hunger

    fuel_loss()
    
    
    

def main():
    while True:
        if not is_alive():
            break
        main_display()
        user_choice = input("Enter to Walk\n"+"1. Inventory\n"+"2. Quit\n")
        try:
            user_choice = int(user_choice)
            # input not in range
            if not 1 <= user_choice <= 2:
                print(f"('{user_choice}') is not a valid option!")
                input('Press Enter to continue...')
                continue
            if user_choice == 2:
                break
            if user_choice == 1:
                inventory()
                continue
        # input not number
        except ValueError:
            if not user_choice == '':
                print(f"('{user_choice}') is not a valid input!")
                input('Press Enter to continue...')
                continue

        # player walked
        if generate_encounter():
            is_alive()
            break
        input('Press Enter to continue...')




        



if __name__ == "__main__":
    main()