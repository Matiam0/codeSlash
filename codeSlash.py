# import libraries below here
# ________________________________________________________________
import random as r
from json import dump
from sys import exit
from os import remove, system, name
from time import sleep
from termcolor import colored
# Pre-Game Setup/Variable(s) below here
# ________________________________________________________________

# Custom Functions.

def clear():
    from os import name, system
    if name == 'posix':
        system('clear')
    else:
        system('cls')

def wait(n):
    sleep(n)

# tGame integrated functions below.
class tGame():
    def rollDice(sides):
        roll = r.randint(1, sides)
        return roll

class ANSI():
    def background(code):
        return "\33[{code}m".format(code=code)
 
    def style_text(code):
        return "\33[{code}m".format(code=code)
 
    def color_text(code):
        return "\33[{code}m".format(code=code)

# End of tGame Integrated.
#Define Main
def main():
    # Main Menu
    # Todo: Menu variants, menu[0] for default no saves, menu[1] save loaded main, menu[2] in game menu
    # Todo: Settings for screen width - set[0], color - set[1], tbd
    # Todo: Stat randomizer w/ re-roll function
    print()
    # Character creation starts here.
    # ? Maybe make character creation it's own function in tgame.

    # Story generator/interaction starts here.
    # ? Maybe make the storyteller procedural.
    # ? Checkpoint system? Include in save file or create new file to save last used story for when loading.

#Run Main
main()
