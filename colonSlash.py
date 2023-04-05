# import libraries below here
# ________________________________________________________________
from src import tGame as tg
from os import rename, system, remove
import json
# Pre-Game Setup/Variable(s) below here
# ________________________________________________________________
# Tru Load files into variables lib### for libraries and file### for other files if not found use built in.
try:
    libCore = tg.fromJson(r".\json\core.json")
except FileNotFoundError:
    libCore = {"menuMainA":{"gameName":"colonSlash","version":"0.1.18a","line1": "_____________","line2": "| New Game  |","line3": "| Load      |","line4": "| Settings  |","line5": "| Quit      |","line6": "\\___________|"},"menuMainB": {"line1": "_____________","line2": "| Continue  |","line3": "| New Game  |","line4": "| Load      |","line5": "| Settings  |","line6": "| Quit      |","line7": "\\___________"},"menuGame":{"line1": "_____________","line2": "| Continue  |","line3": "| New Game  |","line4": "| Load      |","line5": "| Save      |","line6": "| Settings  |","line7": "| Quit      |","line8": "\\___________|"}}

try:
    libRaces = tg.fromJson(r".\json\races.json")
except FileNotFoundError:
    libRaces = {"races":{"1":"Turtle","2":"Ghostbaster","3":"Zombrella","4":"Centilphin","5":"Halvodr","6":"Lucaria"}}

try:
    libISC = tg.fromJson(r".\json\story.json")
except FileNotFoundError:
    libISC = {"intro":{"1":"Such story!","2":"Anyone paying attention?","3":"Barely passing out.","4":"Credits please!","5":"Dreadfully bland.","6":"Efficient use of skill [Bore]","7":"Fast asleep."},"story":{"1":"Story"},"credits":{ "1":"Nope.","2":"No credits here."}}


# Assign contained variables from libFile to local variables.
menuMainA = libCore.get('menuMainA')
menuMainB = libCore.get('menuMainB')
menuGame = libCore.get('menuGame')
gameName = libCore.get('gameName')
gameVersion = libCore.get('version')
title = f"{gameName} v{gameVersion}"

def main():
    # Main menu
    hold = 1
    while hold == 1:
        # Determine what menu to display depending on if a save is loaded or not.
        if loaded == True:
            menu = menuMainB
        if loaded == False:
            menu = menuMainA
        tg.clear()
        # Check for settings file and make one if it doesn't exist from the defaultSettings.
        #Todo: Move defaultSettings into hard-code.
        try:
            fileSettings = tg.fromJson(r"settings.json")
            if fileSettings.get('version') != gameVersion:
                system.remove('settings.json')
        except FileNotFoundError:
            defaultSettings = {"screenWidth": "60", "inputChar": ":\\"}
            with open('settings.json', 'w') as f:
                json.dump(defaultSettings, f,  indent=4)
            fileSettings = tg.fromJson(r"settings.json")
        # Pull from settings the inputCharacter for choices, and the screen width for the game.
        inputChar = fileSettings.get('inputChar')
        screenWidth = fileSettings.get('screenWidth')
        # Start of actual menuMain loop.
        tg.clear
        tg.menu(libCore,title,screenWidth,option=menu)
        inputWidth = (int(screenWidth)/2 - (len(inputChar) * 2.5)) # Math to calculate where to place the input area.
        chi = input(inputChar.rjust(int(inputWidth))) # Choice input followed by if checklist for input in .lower().
        #? Maybe move into a function in tgame.
        if chi.lower() in ["c", "continue"]: # Something of a hidden option for menuMainB for when a save is loaded, will be further expanded on later.
            hold = 0
        if chi.lower() in ["n", "new", "newgame", "new game",]:
            hold = 0
        if chi.lower() in ["l", "load"]:
            #ToDo: Expand on the save/load functionality.
            saveFile = tg.fromJson(r"save.json")
            if saveFile.get("version") == gameVersion:
                tg.clear()
                tg.menu(libCore,title,screenWidth,option="menuMain")
                tg.center("Select a slot to load from.",screenWidth)
                tg.fromJson(saveFile,option="full")
                chi2 = input(inputChar.rjust(int(inputWidth)))
                try:
                    chi2 = int(chi2,base=10)
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
                tg.wait(2)
                loaded = True
                hold = 1
            else:
                remove('save.json')
        if chi.lower() in ["s", "settings", "setting", "set"]:
            tg.settings(fileSettings)
            hold = 1
        if chi.lower() in ["q", "quit", "exit", "exit game"]:
            print("Exiting game...")
            tg.wait(2)
            tg.clear()
            print("Goodbye, TT__TT") # I cri.
            tg.wait(1)
            exit()
    tg.wait(3)
    # Character creation starts here.
    #? Maybe make character creation it's own function in tgame.

    # Story generator/interaction starts here.
    #? Maybe make the storyteller procedural.
    #? Checkpoint system? Include in save file or create new file to save last used story for when loading.
main()