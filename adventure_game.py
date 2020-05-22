import random
import time


def print_sleep(message, wait_time):
    print(message)
    time.sleep(wait_time)

def combat(weapon):
    print_sleep(f"The {enemy} attacks you!", 2)
    if weapon == "batlef":
        print_sleep(f"You a chosen warrior. Last of a dying breed, "
                    "your armed with a {weapon}.", 2)
    choice = input("Would you like to (1) bust some heads or (2) "
                   "run away like a coward?")
    if choice == '1':
        if weapon == "batlef":
            print_sleep(f"You do your best...", 1)
            print_sleep(f"but your {weapon} is no match for the {enemy}.", 2)
            print_sleep(f"You have been defeated!""", 2)
        elif weapon == "sword":
            print_sleep(f"As the {enemy} moves to "
                        "attack, you unsheath your new sword.", 2)
            print_sleep(f"The sword shines brightly "
                        "in your hand as you prepare "
                        "yourself for any attack.", 3)
            print_sleep(f"But the {enemy} takes one "
                        "look at your sword and prepares to fight!", 3)
            print_sleep(f"You have rid the town of the {enemy}. "
                        "You are victorious!", 3)
        elif weapon == "ak-47":
            print_sleep(f"As the {enemy} tries to grab your ak-r7, "
                        "you pull the trigger.", 2)
            print_sleep(f"The gold colored rifle shines brightly "
                        "in your warrior hands!", 3)
            print_sleep(f"The {enemy} tries to grab the Marine "
                        "but he gets a chest full of lead!", 3)
            print_sleep(f"The {enemy} wakes from his dream screaming. "
                        "He can't believe he's alive!", 3)
    elif choice == '2':
        print_sleep("You run back into the field. Luckily, you don't "
                    "seem to have been followed.", 2)
        where_to()
    elif choice == '3':
        print_sleep("End Game", 3)
        where_to()


def play_again():
    choice = ''
    while choice not in ['y', 'n']:
        choice = input("Would you like to play again? (y/n)")
        if choice == 'n':
            print_sleep("Thanks for playing! See you next time.", 2)
            return 'game_over'
        elif choice == 'y':
            print_sleep("Excellent! Restarting the game ...", 2)
            weapon = 'batlef'
            return 'running'


def intro():
    print_sleep("You find yourself standing in the streets of "
                "Baltimore, the concrete jungle.", 3)
    print_sleep(f"Command has said that a {enemy} is somewhere "
                "around here, and has been terrifying the city.", 3)
    print_sleep("In front of you is an abandoned building.", 2)
    print_sleep("To your right is a dark alley.", 2)
    print_sleep(f"In your hand you hold your trusty {weapon}.", 2)


def where_to():
    print_sleep("", 1)
    print_sleep("Enter 1 to knock on the door of the abandoned buiding.", 2)
    print_sleep("Enter 2 to peer into the alley.", 2)
    print_sleep("What would you like to do?", 0)
    choice = ''
    while choice not in ['1', '2']:
        choice = input("(Please enter 1 or 2.)\n")

    if choice == '1':
        building()
    # elif choice == '2':
        # alley()


def building():
    print_sleep("You approach the door of the building.", 2)
    print_sleep(f"You are about to knock when the door "
                "opens and out steps a {enemy}.", 2)
    print_sleep(f"Ahhhh! That is the {enemy}'s building!", 2)
    combat(weapon)


def alley_visited():
    global alley_visited
    global weapon
    print_sleep("You look down the alley.", 2)
    if alley_visited:
        print_sleep("You've been here before, and gotten "
                    "all the good stuff. It's just an empty alley now.", 2)
    elif alley_visited is False:
        print_sleep("It turns out to be only a very small "
                    "abandoned building.", 2)
        print_sleep("Your eye catches a glint of metal behind a rock.", 2)
        print_sleep("You have found the ak-47 of your dreams!", 2)
        print_sleep(f"You discard your silly old {weapon} "
                    "and take the ak-47 with you.", 2)
        weapon = "sword"
    alley_visited = True
    print_sleep("You walk back out to the field. You wipe of "
                "the sweat and drink your gatorade", 2)
    where_to()


game_state = 'running'
while game_state == 'running':

    enemies = ['nokton', 'kaylon', 'vulcan', 'klingon', 'moklan']
    enemy = random.choice(enemies)
    weapon = 'batlef'
    alley_visited = False

    intro()
    where_to()

    game_state = play_again()
