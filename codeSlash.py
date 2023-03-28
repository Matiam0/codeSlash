#import libraries below here
#________________________________________________________________
from src import tGame as tg
#Pre-Game Setup/Variable(s) below here
#________________________________________________________________
#Load files into variables lib### for libraries and file### for other files.
libCore = tg.fromJson(r".\json\core.json")
libRaces = tg.fromJson(r".\json\races.json")
libISC = tg.fromJson(r".\json\isc.json")
libInfo = tg.fromJson(r".\json\info.json")
#Assign contained variables from libFile to local variables.
menuMain = libCore.get('menuMain')
gameName = libInfo.get('gameName')
gameVersion = libInfo.get('version')
title = f"{gameName} v{gameVersion}"

def main():
    # Main menu
    hold = 1
    while hold == 1:
        fileSettings = tg.fromJson(r"settings.json")
        inputChar = fileSettings.get('inputChar')
        screenWidth = fileSettings.get('screenWidth')
        tg.clear
        tg.menu(libCore,title,screenWidth,option="menuMain")
        inputWidth = (int(screenWidth)/2 - (len(inputChar) * 2.5))
        chi = input(inputChar.rjust(int(inputWidth)))
        if chi.lower() in ["n", "new", "newgame", "new game"]:
            hold = 0
        if chi.lower() in ["l", "load"]:
            print("Saving/Loading not implemented yet.")
            tg.wait(2)
            hold = 1
        if chi.lower() in ["s", "settings", "setting", "set"]:
            tg.settings(fileSettings)
            hold = 1
        if chi.lower() in ["q", "quit", "exit", "exit game"]:
            print("Exiting game...")
            tg.wait(2)
            exit()
    tg.wait(3)
    ##Character creation starts here.

main()