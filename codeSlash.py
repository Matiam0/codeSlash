# import libraries below here
# ________________________________________________________________
import os
import json as js
import random as r
import sys as s
from os.path import exists
from time import sleep
# Pre-Game Setup/Variable(s) below here
# ________________________________________________________________
# Tru Load files into variables lib### for libraries and file### for other files if not found use built in.


def main():
    try:
        libCore = fromJson(r".\json\core.json")
    except FileNotFoundError:
        libCore = {
            "gameName": "codeSlash",
            "version": "0.0.1",
            "menuMainA": {
                "line1": "_____________",
                "line2": "| New Game  |",
                "line3": "| Load      |",
                "line4": "| Settings  |",
                "line5": "| Quit      |",
                "line6": "\\___________|"
            },
            "menuMainB": {
                "line1": "_____________",
                "line2": "| Continue  |",
                "line3": "| New Game  |",
                "line4": "| Load      |",
                "line5": "| Settings  |",
                "line6": "| Quit      |",
                "line7": "\\___________"
            },
            "menuGame": {
                "line1": "_____________",
                "line2": "| Continue  |",
                "line3": "| New Game  |",
                "line4": "| Load      |",
                "line5": "| Save      |",
                "line6": "| Settings  |",
                "line7": "| Quit      |",
                "line8": "\\___________|"
            }
        }

    try:
        libRaces = fromJson(r".\json\races.json")
    except FileNotFoundError:
        libRaces = {
            "races": {
                "Human": "Basic.",
            }
        }

    try:
        libISC = fromJson(r".\json\story.json")
    except FileNotFoundError:
        libISC = {
            "intro": {
                "1": "Such story!", 
                "2": "Anyone paying attention?", 
                "3": "Barely passing out.", 
                "4": "Credits please!", 
                "5": "Dreadfully bland.",
                "6": "Efficient use of skill [Bore]", 
                "7": "Fast asleep."
            }, 
            "story": {
                "1": "Story"
            }, 
            "credits": {
                "1": "Nope.", 
                "2": "No credits here."
            }
        }

    # Assign contained variables from libFile to local variables.
    menuMainA = libCore.get('menuMainA')
    menuMainB = libCore.get('menuMainB')
    menuGame = libCore.get('menuGame')
    gameName = libCore.get('gameName')
    gameVersion = libCore.get('version')
    title = f"{gameName} v{gameVersion}"
    loaded = False

    # Main menu
    hold = 1
    while hold == 1:
        # Determine what menu to display depending on if a save is loaded or not.
        if loaded is True:
            menu = menuMainB
        if loaded is False:
            menu = menuMainA
        clear()
        # Check for settings file and make one if it doesn't exist from the defaultSettings.
        try:
            fileSettings = fromJson(r'settings.json')
            if fileSettings.get('version') != gameVersion:
                os.remove('settings.json')
        except FileNotFoundError:
            defaultSettings = {"version":{gameVersion},"screenWidth": "60", "inputChar": ":\\"}
            with open('settings.json', mode='w') as f:
                js.dump(defaultSettings, f,  indent=4)
            fileSettings = fromJson(r"settings.json")
        # Pull from settings the inputCharacter for choices, and the screen width for the game.
        inputChar = fileSettings.get('inputChar')
        screenWidth = fileSettings.get('screenWidth')
        # Start of actual menuMain loop.
        clear()
        menu(libCore, title, screenWidth, option=menu)
        # Math to calculate where to place the input area.
        inputWidth = (int(screenWidth)/2 - (len(inputChar) * 2.5))
        # Choice input followed by if checklist for input in .lower().
        chi = input(inputChar.rjust(int(inputWidth)))
        # ? Maybe move into a function in tgame.
        # Something of a hidden option for menuMainB for when a save is loaded, will be further expanded on later.
        if chi.lower() in ["c", "continue"]:
            hold = 0
        if chi.lower() in ["n", "new", "newgame", "new game",]:
            hold = 0
        if chi.lower() in ["l", "load"]:
            #ToDo: Expand on the save/load functionality.
            saveFile = fromJson(r"save.json")
            if saveFile.get("version") == gameVersion:
                clear()
                menu(libCore, title, screenWidth, option="menuMain")
                center("Select a slot to load from.", screenWidth)
                fromJson(saveFile, get="full")
                chi2 = input(inputChar.rjust(int(inputWidth)))
                try:
                    chi2 = int(chi2, base=10)
                except ValueError:
                    print("Invalid slot number.")
                if chi2 == 0:
                    save = saveFile.get('slot0')
                    print(f"Loaded {save}.")
                if chi2 == 1:
                    save = saveFile.get('slot1')
                    print(f"Loaded {save}.")
                if chi2 == 2:
                    save = saveFile.get('slot2')
                    print(f"Loaded {save}.")
                if chi2 == 3:
                    save = saveFile.get('slot3')
                    print(f"Loaded {save}.")
                wait(2)
                loaded = True
                hold = 1
            else:
                os.remove('save.json')
        if chi.lower() in ["s", "settings", "setting", "set"]:
            settings(fileSettings)
            hold = 1
        if chi.lower() in ["q", "quit", "exit", "exit game"]:
            print("Exiting game...")
            wait(2)
            clear()
            print("Goodbye, TT__TT")  # I cri.
            wait(1)
            sys.exit()
    wait(3)
    # Character creation starts here.
    # ? Maybe make character creation it's own function in tgame.

    # Story generator/interaction starts here.
    # ? Maybe make the storyteller procedural.
    # ? Checkpoint system? Include in save file or create new file to save last used story for when loading.

#!Read Me
# Custom Functions.

def clear():
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

# define sleep as an easy to call function

def wait(n):
    sleep(n)

# tGame integrated functions below.

def rollDice(sides):
    roll = r.randint(1, sides)
    return roll

def fromJson(file, screenWidth=0, get="init", isCenter=False):
    width = int(screenWidth)
    if isCenter == True and width >= 1 and get.lower() == "value":
        for v in file.values():
            print(v.center(width))
    if isCenter == True and width >= 1 and get.lower() == "key":
        for k in file.keys():
            print(k.center(width))
    if isCenter == False and get.lower() == "value":
        for v in file.values():
            print(v)
    if isCenter == False and get.lower() == "key":
        for k in file.keys():
            print(k)
    if get.lower() == "full":
        for k, v in file.items():
            print(f"{k} : {v}")
    if get.lower() == "init":
        data = js.load(open(file, "r"))
        return data

def save(file, path=".\\"):
    filePath = f"{path}{file}.json"
    with open(file, "w", encoding=str) as f:
        js.dump(filePath, f, indent=4)

def barSeparator(screenWidth):
    width = int(screenWidth)
    while int(width) > 0:
        print("-", end="")
        width = width - 1
    print()

def center(title, screenWidth):
    title = str(title)
    width = int(screenWidth)
    print(title.center(width))

def menu(libC, title="Title Here", screenWidth=0, option="title"):
    menuMain = libC.get('menuMain')
    if option == "menuMain":
        barSeparator(screenWidth)
        center(title, screenWidth)
        barSeparator(screenWidth)
        fromJson(menuMain, screenWidth, isCenter=True, get="value")
    if option == "title":
        barSeparator(screenWidth)
        center(title, screenWidth)
        barSeparator(screenWidth)

def check(file):
    check = exists(file)
    return check

def settings(fileSettings):
    fromJson(fileSettings, screenWidth=0, get="full")
    print("You may reset to default settings with 'reset'.")
    ch = input("Choose a setting to change: ")
    if ch in fileSettings:
        fileSettings[ch] = input("New value: ")
        fromJson(fileSettings, get="save")
    elif ch == "reset":
        os.remove('settings.json')
    else:
        print("Invalid option, returning to menu.")

def createCharacter(libC,libRaces, title, screenWidth=0):
    hold = 1
    while hold == 1:
        menu(libC, title, screenWidth, option="title")
        
        print("Starting Character Creation.")


# todo fix loading bar
# def loadingBar(percent,max,text, centerValue):
#     from alive_progress import alive_bar

#     with alive_bar(max,length=58,enrich_print=False,theme='smooth',manual=True,force_tty=None,stats=False,elapsed=False,monitor=False) as bar:
#         is_max = True
#         print()
#         while is_max == True:
#             clear()
#             fromJson(centerValue)
#             print()
#             print(text.center(centerValue))
#             bar(percent)
#             wait(0.05)
#             percent = percent + 0.05
#             text = text + "."
#             if text == "Loading....":
#                 text = "Loading."
#             if percent >= max/100:
#                 is_max = False
#                 break

# todo either find a use for skillText or remove it.
def skillText(text):
    print(f"{text}")

def creationBar(name, gender, age, race, centerValue):
    text = (f"Name: {name}, Gender: {gender}, Age: {age}, Race: {race}")
    print(text.center(centerValue))

# End of tGame Integrated.

#Run Main
main()