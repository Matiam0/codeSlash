# import libraries below here
# ________________________________________________________________
from random import randint
from json import dump
from sys import exit
from os import remove, system, name
from time import sleep
# Pre-Game Setup/Variable(s) below here
maxStats = 20
menu = {
    "0":{
        "l1":"/-----------------------------------------------------------------------------------------",
        "l2":"| 1 |    New Game         /",
        "l3":"| 2 |    Load Game        |",
        "l4":"| 3 |    Settings         |",
        "l5":"\------------------------/"
    },
    "1":{
        "l1":"",
        "l2":"",
    },
    "2":{
        "l1":"",
        "l2":"",
    }
    }
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
        roll = randint(1, sides) # type: ignore
        return roll
    
    def fromDic(dic):
        for i,v in dic: # type: ignore
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
        inventoryDefault = {
            "Slot 1" : "Empty",
        }
        def create(statusDefault):
            print()
            

class tFormat():
    def fCode(code):
        return "\33[{code}m".format(code=code)

    def fClear(): # type: ignore
        print(tFormat.fCode(0)) # type: ignore

    def cJustify(text, width=-1):
      lines = text.split('\n') # type: ignore
      width = max(map(len, lines)) if width == -1 else width
      return '\n'.join(line.center(width) for line in lines)

    def rJustify(text,width=-1):
        lines = text.split('\n') # type: ignore
        width = max(map(len,lines)) if width == -1 else width
        return '\n'.join(line.rjust(width) for line in lines)

    def fTitle(text,width=100,bg="40",st="31",cc="1"):
        print(tFormat.fCode(bg) + tFormat.fCode(st) + tFormat.fCode(cc),end="") # type: ignore
        text = tFormat.fCode(bg) + tFormat.fCode(st) + tFormat.fCode(cc) + text # type: ignore
        print(tFormat.cJustify(text,width))
        tFormat.cclear() # type: ignore

# End of tGame Integrated.
#Define Main
def main():
    # Main Menu
    # Todo: Menu variants, menu[0] for default no saves, menu[1] save loaded main, menu[2] in game menu
    # Todo: Settings for screen width - set[0], color - set[1], tbd
    # Todo: Stat randomizer w/ re-roll function
    test_text = "Hello stranger."
    tFormat.fTitle(test_text) # type: ignore
    wait(3)
    clear()
    tGame.charInit.create() # type: ignore
    # Character creation starts here.
    # ? Maybe make character creation it's own function in tgame.

    # Story generator/interaction starts here.
    # ? Maybe make the storyteller procedural.
    # ? Checkpoint system? Include in save file or create new file to save last used story for when loading.

#Run Main
main()


