#import libraries below here
#________________________________________________________________
from src import tgame as tg
#Pre-Game Setup/Variable(s) below here
#________________________________________________________________
#Load files into variables lib### for libraries and file### for other files.
libJson = "json\core.json"
fileSave = "saves\save.json"
#pull the game values from libJson.
gameName =  tg.fromJson(libJson).get("gameName")
gameState = tg.fromJson(libJson).get("gameState")
gameVersion = tg.fromJson(libJson).get("version")
menuMain = tg.fromJson(libJson).get("menuMain")
menuGame = tg.fromJson(libJson).get("menuGame")
title = tg.fromJson(libJson).get("title")
gameOpening = tg.fromJson(libJson).get("intro")
gameCredits = tg.fromJson(libJson).get("credits")
centerValue = tg.fromJson(libJson).get("centerValue")

def main():
    #Main menu
    check = True
    while check == True:
        tg.clear() #using tg.clear() clears text from the screen.
        tg.jsonValue(title,centerValue) #tg.jsonValue(target) is used to pull pre-setup/formatted menus/text from the lib.json
        tg.jsonValue(menuMain,centerValue)
        print()
        option = input("/Select option: ").lower()
        if option in ["new", "new game", "n"]:
            tg.clear()
            tg.jsonValue(title,centerValue)
            tg.loadingBar(0,100,"Loading",title,centerValue)
            tg.wait(1)
            tg.clear()
            check = False
        elif option in ["load", "l"]: #Todo: finish implementation of saving/loading.
            saveCheck = tg.check(fileSave)
            if saveCheck == True:
                save = tg.fromJson(fileSave)
                tg.jsonValue(save,centerValue)
                tg.clear()
                tg.jsonValue(title,centerValue)
                slot = input("What save slot do you want to load? ")
                if slot == "1":
                    save = tg.fromJson(fileSave).get("slot1")
                elif slot == "2":
                    save = tg.fromJson(fileSave).get("slot2")
                elif slot == "3":
                    save = tg.fromJson(fileSave).get("slot3")
                else:
                    print("Please enter a number.")
                check = False
            elif saveCheck == False:
                tg.clear()
                print("You have no save files. Try starting a new game!")
                tg.wait(2)
                check = False
        elif option in ["settings", "setting","s"]:
            tg.clear()
            tg.jsonValue(title,centerValue)
            print("There currently are no settings available in the game. This is a placeholder for when I find things I want users to have settings for.")
            tg.wait(10)
            check = True
        elif option in ["quit", "q"]:
            tg.clear()
            tg.jsonValue(title,centerValue)
            print("Exiting...")
            tg.wait(4)
            exit()
        else:
            print("Invalid Input: Try something else. Like Q for quitting.")
            tg.wait(5)
    tg.clear()
    tg.jsonValue(title,centerValue) #prints out the opening credits
    tg.barSeparator(centerValue)
    for i in gameOpening:
        text = gameOpening.get(i)
        print(text.center(centerValue))
        tg.wait(1)

    
    #ToDo:Character Creation
    ##Name
    hold = 1
    while hold == 1:
        tg.clear()
        tg.jsonValue(title,centerValue)
        name = "None"
        gender = "None"
        age = "None"
        race = "None"
        tg.creationBar(name, gender, age, race, centerValue)
        tg.barSeparator(centerValue)
        name = str(input("What is your name? ")).capitalize()
        if name == "":
            name = "Trollolol Johnson"
            print(f"Using default, {name}.")
            tg.wait(1)
            hold = 0
        else:
            hold = 0
    ##Gender
    hold = 1
    while hold == 1:
        tg.clear()
        tg.jsonValue(title,centerValue)
        tg.creationBar(name, gender, age, race,centerValue)
        tg.barSeparator(centerValue)
        gender = str(input("Are you male or female? : ")).lower()
        if gender in ["male", "female", "m", "f"]:
            if gender in ["m", "male"]:
                gender = "Male"
            elif gender in ["f","female"]:
                gender = "Female"
            hold = 0
        else:
            gender="male"
            print(f"Using default, {gender}.")
            tg.wait(1)
            hold = 0
    else:
        tg.clear()
        
    
    ##Age
    hold = 1
    while hold == 1:

        tg.clear()
        tg.jsonValue(title,centerValue)
        tg.creationBar(name, gender, age, race,centerValue)
        tg.barSeparator(centerValue)
        age = input("How old are you? : ")
        if age is not int:
            age = 16
        if age != 0 and age >= 9 and age <= 60:
            confirm = input(f"You have chosen to be {age} years old, are you sure? (y/n): ").lower()
            if confirm in ("y", "yes"):
                hold = 0
            elif age == None:
                age = 16
                confirm = input(f"You have chosen to be {age} years old, are you sure? (y/n)").lower()
                if confirm in ("y", "yes"):
                    hold = 0
        else:
            hold = 1
                

    ##Race selection.
    raceList = tg.fromJson(libJson).get("races")
    hold = 1
    while hold == 1:
        tg.clear()
        tg.jsonValue(title,centerValue)
        tg.creationBar(name, gender, age, race,centerValue)
        tg.barSeparator(centerValue)
        print("Please, select a race from the following: ")
        for key,value in raceList.items():
            print(f"{key} : {value}")
        selection = input("What race enter the number matching it: ")
        race = raceList.get(selection)
        if race == raceList.keys():
            race = raceList.get("1")
        if race == None:
            race = raceList.get("1")
        confirm = input(f"You have selected {race}, are you sure you want this one? (y/n)").lower()
        if confirm in ("y","yes"):
            hold = 0
        else: 
            hold = 1
            
    ##initial stats.
    tg.clear()
    tg.jsonValue(title,centerValue)
    tg.barSeparator(centerValue)
    strength = tg.rollDice(6)
    dexterity = tg.rollDice(6)
    intelligence = tg.rollDice(6)
    charisma = tg.rollDice(6)
    stats = {"str": strength, "dex": dexterity, "int": intelligence, "cha": charisma}
    sp = tg.rollDice(6) + tg.rollDice(6) + tg.rollDice(6)
    ##dictionary sheet to hold stats age, name, and race.
    char = {"name":name, "gender":gender, "age":age, "race":race}
    sheet = {"char":char, "stats":stats, "sp": sp}
    print(sheet)
    ##ToDo: initialize XP/Level system.

    tg.clear()
    ## Credits
    tg.jsonValue(title,centerValue)
    for i in gameCredits:
        text = gameCredits.get(i)
        print(text.center(centerValue))
        tg.wait(2)
    #Finale screen clear.
    tg.wait(20)
    tg.clear()
        

main()