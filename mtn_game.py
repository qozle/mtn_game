import random
import os
from pathlib import Path as path
from character import *
from rooms import *
from merchants import *
from skills import *
from time import time, ctime



SKILLBOOKS= {'Skillbook: Wit': 200, 'Skillbook: Haggle': 200, 'Skillbook: Jump': 200, 'Skillbook: Climb':200,
             'Skillbook: Focus': 200}

SKILLS = ['wit', 'haggle', 'jump', 'climb', 'focus']


#####  FUNCTION FOR CLEARING THE SCREEN  #####
def cls():

    os.system("cls" if os.name == "nt" else "clear")


#####   SET INITIAL CONDITIONS  #####
## This makes the first room and makes it merchant
room = Room()
room.make_doors()
room.player_loc = room.doors['back'][1]
room.merchant_loc = room.get_location()
## This makes a temp merchant to take it inventory bc I'm lazy
invis_merchant = Merchant()
win_list = set(invis_merchant.inventory_list)


## Win condition check
def win_check():
    inv_set = set()
    for item in toon.inventory:
        inv_set.add(str(item))
    if inv_set.intersection(win_list) == win_list:
        cls()
        input("""
Aweessooommmee!  You collected all the different items from the merchants!!


You win!!  There's not much more to do, but you can keep walking around!

Go ahead, do a victory lap!""")

## This sets up the file structure
p = path(str(path.cwd()) + "/saves")
if p.is_dir() == False: p.mkdir()
directory = sorted(item for item in p.iterdir())


#####  START OF GAME  #####
cls()
if directory == []:
    toon = Character.new_toon()
    
else:
    info = input("You can make a [new] character, or [load] a saved one.  What would you like to do? >")
    info.lower()
    info.strip()
    if info == 'new':
        toon = Character.new_toon()
    if info == 'load':
        print("\n\n")
        for item in directory: print(item.name + "\n\n")
        info = input("Enter a character file to load it. >")
        info.strip()
        for item in directory:
            if info == item.name:
                toon = Character.load_toon(item.name)
                
                
##### MAIN WHILE LOOP #####

while True:
    check_training(toon)
    cls()
    room.draw_map()
    print("\n\n")
    print("[Save][Quit][Help][Inv][Skills]")
    print("ROOM {} ".format(room.room_idt) * 6)

    win_check()
    
    info = input('\nWhat do you want to do? You can move {}. >'.format
                 (room.avail_moves()))
    info = info.lower()
    info = info.strip()

    if info == 'skills':
        toon = skill_window(toon)               
            
    if info == 'left' or 'right' or 'up' or 'down':  ## This should be replaced with tkinter functionality
        room.move_player(info)

    if info == 'help':
        cls()
        room.help()

    ## Could eventually make inventory a class
    if info == 'inv':
        while True:
            cls()
            print("You have the following items in your inventory:" + "\n") 

            for item in toon.inventory:
                print(item + "\n")
            print("You have the following skillbooks to read:\n\n")

            for item in toon.inventory:
                if 'Skillbook' in item:
                    print(item + '\n')

            info = input("\nEnter a skillbook to read it, or [Back]. >")
            for item in toon.inventory:
                try:
                    if info == item and item in SKILLBOOKS:
                        toon.skill_books[item] = SKILLBOOKS[item]
                        toon.inventory.pop(toon.inventory.index(item))
                        input("You've read {} and can now begin training it under the skills window!".format(item))

                except: input("Sorry, I don't understand, enter return to try again")
            if info == 'back':
                break              
            

    if info == 'back':
        if room.player_loc == room.doors['back'][1] and room.room_num != 0:
            room = room.go_back()
        else: print("You can't go out this door yet sorry =(")

    if info == 'door':
        if room.player_loc == room.doors['a'][1] or room.player_loc == room.doors['b'][1]:
            for item in room.doors:
                if room.player_loc == room.doors[item][1]:
                    room = room.doors[item][0]
                    room.make_doors()
                    room.player_loc = room.doors['back'][1]
                    room.merchant_loc = room.get_location()

        elif room.player_loc == room.doors['back'][1]:
            print("This door only goes back, use [Back].")

        else:
            print("You're not on a valid door =(")

    if info == 'merchant':
        if room.player_loc == room.merchant_loc:
            while True:
                info = room.merchant.activate(toon.inventory)
                info = info.lower()

                if info == 'buy':
                    info = room.merchant.buy(toon.inventory)
                    if info == 'back': break
                    else: toon.inventory = info
                                          

                if info == 'sell':
                    info = room.merchant.sell(toon.inventory)
                    if info == 'back': break
                    else: toon.inventory = info

                if info == 'back': break
                    
    ## IF SAVE
    if info == 'save':
        cls()
        nameinfo = input("What do you want to save your character as? >")
        nameinfo = nameinfo.lower()
        Character.save_toon(toon, nameinfo)
        print('\n')
        info = input("Ok!  Your character has been saved in a file as {}.  Enter return to continue. >".format(nameinfo))

    # Check that the victory condition works
    if info == 'cheat':
        toon.inventory += invis_merchant.inventory_list

    ## TIME TO GTFO oops caps
    if info == 'quit':
        break
