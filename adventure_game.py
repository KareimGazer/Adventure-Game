import random

monsters = ["a wicked pirate", "an ugly troll", "a terrifying dragon"]
monster = random.choice(monsters)

heros = ["batman", "bumble bee", "groot"]
hero = random.choice(heros)


def print_pause(message, delay=1):
    import time
    print(message)
    time.sleep(delay)


def capture_input(message, options):
    choice = ""
    while not (choice in options):
        choice = input(message)
    return choice

print_pause("welcome to the mysterious land of Pythonia!")
print_pause(f"Rumors say that {monster} is frightening the villagers.") # formatted string
print_pause(f"but you are {hero} who will save the day!")

place = "field"
while True:
    if place == "field":
        print_pause("you land in a very large field")
        print_pause("in front of you there is a castle")
        print_pause("to your right there is a strange hut that seems unfamiliar")
        print_pause("press 1 to enter the castle")
        print_pause("press 2 to enter the hut")
        choice = capture_input("choose 1 or 2: ", ["1", "2"])
        if choice == "1":
            place = "castle"
        elif place == "2":
            place = "hut"
    elif place == "castle":
        print_pause("you are inside the castle")
    elif place == "hut":
        print_pause("you are inside the hut")
    game_over = capture_input("do you want to continue? y/n: ", ["y", "n"])
    if game_over == "n":
        break
    elif game_over == "y":
        continue
