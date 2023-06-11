# import libraries below here
# ________________________________________________________________
from random import randint
from json import dump
from sys import exit
from os import remove, system, name
from time import sleep
# Pre-Game Setup/Variable(s) below here
maxStats = 20
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
class game():
    def rollDice(sides):
        roll = randint(1, sides)
        return roll
    
    def fromDic(dic):
        for i,v in dic:
            print(f"{i}:{v}")

    class charInit():
        ##Defaults
        statusDefault = {
            "fName":"Mafe",
            "lName":"Roe",
            "Level": 0,
            "Exp":0,
            "Stats":{
                "Physical":{
                    "Strength":3,
                    "Agility":3
                    },
                "Spirit":{
                    "Lore":3,
                    "Determination":3
                },
                "Mental":{
                    "Intelligence":3,
                    "Charisma":3
                }
            }
        }
        def create(status=statusDefault):
            print()
            

class tFormat():
    def fCode(code):
        return "\33[{code}m".format(code=code)

    def fClear():
        print(tFormat.fCode(0))

    def cJustify(text, width=-1):
      lines = text.split('\n')
      width = max(map(len, lines)) if width == -1 else width
      return '\n'.join(line.center(width) for line in lines)

    def rJustify(text,width=-1):
        lines = text.split('\n')
        width = max(map(len,lines)) if width == -1 else width
        return '\n'.join(line.rjust(width) for line in lines)

    def fTitle(text,width=100,bg="40",st="31",cc="1"):
        print(tFormat.fCode(bg) + tFormat.fCode(st) + tFormat.fCode(cc),end="")
        text = tFormat.fCode(bg) + tFormat.fCode(st) + tFormat.fCode(cc) + text
        print(tFormat.cJustify(text,width))
        tFormat.cclear()

# End of tGame Integrated.
#Define Main
def main():
    # Main Menu
    # Todo: Menu variants, menu[0] for default no saves, menu[1] save loaded main, menu[2] in game menu
    # Todo: Settings for screen width - set[0], color - set[1], tbd
    # Todo: Stat randomizer w/ re-roll function
    test_text = "Hello stranger."
    tFormat.fTitle(test_text)
    wait(3)
    clear()
    tGame.charInit.create()
    # Character creation starts here.
    # ? Maybe make character creation it's own function in tgame.

    # Story generator/interaction starts here.
    # ? Maybe make the storyteller procedural.
    # ? Checkpoint system? Include in save file or create new file to save last used story for when loading.

#Run Main
main()
