import random
import os
from character import *
from rooms import *
from merchants import *

## I'm testing to see if this affects just the local branch and not master, as
## should


#####  FUNCTION FOR CLEARING THE SCREEN  #####
def cls():

    os.system("cls" if os.name == "nt" else "clear")

variable= "I'm adding a random string variable for git testing"


#####   SET INITIAL CONDITIONS  #####
## This makes the dictionary that will contain key=room_num, value=Merchant()
merchant_dict = {}

## This makes the players character and fills it will the inventory
toon = Character()
toon.create_character()

## This makes the first room and makes it merchant, assigns it to the merch_dict

room = Room()
room.make_doors()
room.player_loc = room.doors['back'][1]
room.merchant_loc = room.get_location()

## This makes a temp merchant to take it inventory bc I'm lazy
invis_merchant = Merchant()
win_list = set(invis_merchant.inventory_list)
invis_merchant


## This checks for the win condition
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


##### MAIN WHILE LOOP #####

while True:

    room.draw_map()
    print("\n\n")
    print("ROOM {} ".format(room.room_idt) * 6)

    win_check()
    
    info = input('\nWhat do you want to do?  [Help] for help.  You can move {}. >'.format
                 (room.avail_moves()))
    info = info.lower()

    if info == 'left' or 'right' or 'up' or 'down':
        room.move_player(info)

    if info == 'help':
        cls()
        room.help()

    if info == 'inv':
        cls()
        print("You have the following items in your inventory:" + "\n")
        for item in toon.inventory:
            print(item)
        input("Press return to continue. >")

    
    if info == 'back':
        if room.player_loc == room.doors['back'][1]:
            room = room.go_back() 

    if info == 'door':
        for item in room.doors:
            if room.player_loc == room.doors[item][1]:
                room = room.doors[item][0]
                
                room.make_doors()
                room.player_loc = room.doors['back'][1]
                room.merchant_loc = room.get_location()

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
                    

    # Check that the victory condition works
    if info == 'cheat':
        toon.inventory += invis_merchant.inventory_list

    ## TIME TO GTFO oops caps
    if info == 'quit':
        break


    cls()
