import random

monsters = ["a wicked pirate", "an ugly troll", "a terrifying dragon"]
monster = random.choice(monsters)

heros = ["batman", "bumble bee", "groot"]
hero = random.choice(heros)

def print_pause(message, delay=0):
    import time
    print(message)
    time.sleep(delay)

print_pause("welcome to the mysterious land of Pythonia!")
print_pause(f"Rumors say that {monster} is frightening the villagers.") # formatted string
print_pause(f"but you are {hero} who will save the day!")

print_pause("you land in a very large field")
print_pause("in front of you there is a castle")
print_pause("to your right there is a strange hut that seems unfamiliar")
print_pause("press 1 to enter the castle")
print_pause("press 2 to enter the hut")

def capture_input(message, options):
    choice = ""
    while not (choice in options):
        choice = input(message)
    return choice

move = capture_input("please enter 1 or 2: ", ["1", "2"])
print("you chose ", move)
