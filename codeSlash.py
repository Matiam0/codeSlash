# import libraries below here
# ________________________________________________________________
from random import randint
from json import dump
from sys import exit
from os import remove, system, name
from time import sleep
# Pre-Game Setup/Variable(s) below here
# ________________________________________________________________

# Custom Functions.

def clear():
    if name == 'posix':
        system('clear')
    else:
        system('cls')

def wait(n):
    sleep(n)

# tGame integrated functions below.
class tGame():
    def rollDice(sides):
        roll = randint(1, sides)
        return roll

class ANSI():
    def background(code):
        return "\33[{code}m".format(code=code)
 
    def style_text(code):
        return "\33[{code}m".format(code=code)
 
    def color_text(code):
        return "\33[{code}m".format(code=code)

    def color(text="test",bg=0,style=0,color=0):
        output = ANSI.background(bg) + ANSI.style_text(style) + ANSI.color_text(color) + text + ANSI.background(0) + ANSI.style_text(0) + ANSI.color_text(0)
        return output

# End of tGame Integrated.
#Define Main
def main():
    # Main Menu
    # Todo: Menu variants, menu[0] for default no saves, menu[1] save loaded main, menu[2] in game menu
    # Todo: Settings for screen width - set[0], color - set[1], tbd
    # Todo: Stat randomizer w/ re-roll function
    test_text = ANSI.color("Hello stranger.",40,30,0)
    print(test_text)
    wait(3)
    clear()
    # Character creation starts here.
    # ? Maybe make character creation it's own function in tgame.

    # Story generator/interaction starts here.
    # ? Maybe make the storyteller procedural.
    # ? Checkpoint system? Include in save file or create new file to save last used story for when loading.

#Run Main
main()
