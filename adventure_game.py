import random

monsters = ["a wicked pirate", "an ugly troll", "a terrifying dragon"]
monster = random.choice(monsters)

heros = ["batman", "bumble bee", "groot"]
hero = random.choice(heros)

place = "field"
has_sword = False
score = 0

def print_pause(message, delay=1):
    import time
    print(message)
    time.sleep(delay)


def capture_input(message, options):
    choice = ""
    while not (choice in options):
        choice = input(message)
    return choice


def get_input(message, options):
    while True:
        choice = input(message)
        if choice in options:
            return choice
        else:
            print("wrong input, " \
            "please try one of the options listed")
            continue


def field():
    print_pause("you land in a very large field")
    print_pause("in front of you there is a castle")
    print_pause("to your right " \
    "there is a strange hut that seems unfamiliar")
    print_pause("press 1 to enter the castle")
    print_pause("press 2 to enter the hut")
    choice = capture_input("choose 1 or 2: ", ["1", "2"])
    if choice == "1":
        return "castle"
    elif choice == "2":
        return "hut"


def castle():
    global monster, has_sword, score
    print_pause("you enter the castle")
    print_pause(f"then come the {monster}")
    print_pause("press 1 to attack the monster")
    print_pause("press 2 to escape")
    choice = capture_input("choose 1 or 2: ", ["1", "2"])
    if choice == "1":
        if has_sword:
            print_pause(f"{monster} escapes, and you save the village!")
            score += 70
        else:
            print_pause(f"{monster} attacks you, you lose!!!")
            score -= 100
        return None
    elif choice == "2":
        print_pause("you manage to escape and return to the field")
        return "field"


def hut():
    global has_sword, score
    print_pause("you bear into the hut")
    if has_sword:
        print_pause("you got here before, nothing new to find")
    else:
        print_pause("you recognize something on the table")
        print_pause("you find the legendary sword of king arthur")
        has_sword = True
        score = score + 30
    print_pause("you return to the field")
    return "field" 


if __name__ == "__main__":
    print_pause("welcome to the mysterious land of Pythonia!")
    print_pause(f"Rumors say that {monster} is frightening the villagers.") # formatted string
    print_pause(f"but you are {hero} who will save the day!")
    while True:
        if place == "field":
            place = field()
        elif place == "castle":
            place = castle()
        elif place == "hut":
            place = hut()
        
        if place == None:
            print_pause("Game Over!!")
            if score >= 100:
                print_pause("congratulations you won!")
            elif score <= 0:
                print_pause("good luck next time")
            print_pause(f"you score is {score}")
            game_over = capture_input("do you want to play again? y/n: ", ["y", "n"])
            if game_over == "y":
                place = "field"
                sword = False
                score = 0
                continue
            elif game_over == "n":
                break

    print_pause("Thank you for playing our game")
    print_pause("we look forward to seeing you play again")
