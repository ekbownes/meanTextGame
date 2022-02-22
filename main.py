# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random

import place

def print_welcome(name):
    # Use a breakpoint in the code line below to debug your script.
    print("{0}, congratulations, you're trapped in a text game.".format(name))  # Press ⌘F8 to toggle the breakpoint.
    print("Move your character using the basic WASD keyboard rules.\n"
          "Go ahead and try now.")

responses = ["Try again shithead", "That's not an option", "Wow you're fucking dumb", "Read directions better"]

def get_action():
    actn = raw_input("do something ").upper()
    valid_movements = {"W": "forward", "A": "left", "S": "back", "D": "right", "Q": "quit"}
    if valid_movements.has_key(actn) :
        mvmnt = valid_movements.get(actn)
        return mvmnt
    else:
        print(responses[random.randrange(len(responses))])
        return get_action()

# Press the green button in the gutter to run the script.

places = {
        "welcome": place.Place("This is the first Place, some day a really cute description will sit here", "final", "there is nothing behind you", "you see a blank wall to your left", "nothing to your right", True),
        "final": place.Place("Congratz u won, go get a life :)", "", "", "", "", False)
    }

if __name__ == '__main__':
    username = raw_input("Hey asshole, what's your name? ")
    print_welcome(username)
    actn = get_action()
    print ("Okay, you get it, we're starting for real now")
    in_game = True
    current_place = places.get("welcome")
    print(current_place.description)
    while in_game:
        actn = get_action()
        thing = current_place.move(actn)
        if places.has_key(thing):
            current_place = places.get(thing)
            print(current_place.description)
        else:
            print(thing)
        in_game = current_place.get_victory()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
