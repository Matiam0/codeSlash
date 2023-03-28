#import libraries below here
#________________________________________________________________
from src import tgame as tg
#Pre-Game Setup/Variable(s) below here
#________________________________________________________________
#Load files into variables lib### for libraries and file### for other files.
libCore = tg.fromJson(r"colonSlash\json\core.json")
libRaces = tg.fromJson(r"colonSlash\json\races.json")
libISC = tg.fromJson(r"colonSlash\json\isc.json")
libInfo = tg.fromJson(r"colonSlash\json\info.json")
libSettings = tg.fromJson(r"colonSlash\settings.json")
#Assign contained variables from libFile to local variables.
screenWidth = libSettings.get('screenWidth')
menuMain = libCore.get('menuMain')
gameName = libInfo.get('gameName')
gameVersion = libInfo.get('version')
title = f"{gameName} v{gameVersion}"
ch = libSettings.get('inputChar')

def main():
    # character creation
    hold = 1
    while hold == 1:
        tg.clear
        tg.menu(libCore,title,screenWidth,option="menuMain")
        inputWidth = int(screenWidth/2 - (len(ch) * 2.5))
        chi = input(ch.rjust(inputWidth))
        if chi.lower() in ["n", "new", "newgame", "new game"]:
            hold = 0
        if chi.lower() in ["l", "load"]:
            print("Saving/Loading not implemented yet.")
            tg.wait(2)
            hold = 1
        if chi.lower() in ["s", "settings", "setting", "set"]:
            print("No settings yet.")
            tg.wait(2)
            hold = 1
        if chi.lower() in ["q", "quit", "exit", "exit game"]:
            print("Exiting game...")
            tg.wait(2)
            exit()
    tg.wait(3)

main()