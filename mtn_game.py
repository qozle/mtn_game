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
room.player_loc = room.get_location()
room.merchant_loc = room.get_location()
merchant_dict[room.room_num] = Merchant()

## This makes a temp merchant to take it inventory bc I'm lazy
invis_merchant = Merchant()
win_list = set(invis_merchant.inventory_list)
del invis_merchant



##### MAIN WHILE LOOP #####

while True:

    room.draw_map()
    print("\n\n")
    print("ROOM {} ".format(room.room_num) * 6)

    ## This checks for the win condition
    inv_set = set()
    for item in toon.inventory:
        inv_set.add(str(item))
    if inv_set.intersection(win_list) == win_list:
        cls()
        input("""
Aweessooommmee!  You collected all the different items from the merchants!!


You win!!  There's not much more to do, but you can keep walking around!

Go ahead, do a victory lap!""")


    ## Takes the player's input, fills in the format with the return from
    ## avail_moves (see avail_moves() under rooms), sets the return from
    ## input to lower case.
    info = input('\nWhat do you want to do?  [Help] for help.  You can move {}. >'.format
                 (room.avail_moves()))
    info = info.lower()

    ## If it's any of the moves, then run the move_player method (see move_player
    ## under rooms)
    if info == 'left' or 'right' or 'up' or 'down':
        room.move_player(info)

    ## If it's help, print the help junk on the current instance (see help() under
    ## rooms)
    if info == 'help':
        cls()
        room.help()

    ## Cls (clear the screen), print inventory, wait for input to ctn
    if info == 'inv':
        cls()
        print("You have the following items in your inventory:" + "\n")
        for item in toon.inventory:
            print(item)
        input("Press return to continue. >")

    
    if info == 'back':

        room = room.go_back() 

    if info == 'door':

        room = room.new_room()       

        
        ## Curently broken.
    if info == 'forward':

        room = room.go_forward()

        
    if info == 'merchant':
        merchant = merchant_dict[room.room_num]
        item = merchant.activate(toon.inventory)

        ## Also currently broken.  This is some bullshit to sort out the return
        ## info from merchant.activate(). I just have to rewrite it and sort it
        ## out.
        while True:

            try:
                if set(item).issubset(set(toon.inventory)):
                    toon.inventory = item
            except:

                item = 'back'
                continue

            if item == 'back':
                break

            else:
                toon.inventory += [item]

    ## If you're lazy and want to check that the win condition works without
    ## going through the whole game like a crazy person (ok, I tried three times
    ## and had some bugs, but I think it would actually work), this just adds
    ## all the items to the player's inventory_list.  =)
    if info == 'cheat':
        toon.inventory += invis_merchant.inventory_list

    ## TIME TO GTFO oops caps
    if info == 'quit':
        break


    cls()
