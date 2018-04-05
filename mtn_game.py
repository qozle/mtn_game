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



#####   SET INITIAL CONDITIONS  #####

## This makes the dictionary that will contain key=room_num, value=Merchant()
merchant_dict = {}

## This makes the players character and fills it will the inventory
toon = Character()
toon.create_character()

## This makes the first room and makes it merchant, assigns it to the merch_dict
room = Room('0')
room.player_loc = (0,0)
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

    ## If player_loc = player_gb, they're standing on the door they came in from
    ## Not really, they can type this whenever and it might give an error but
    ## either way it has to be fixed, for all these if statements that require
    ## the player's pos to be on a door or merch, I need to check somewhere
    ## other than avail_moves that they are actually there.
    if info == 'back':

        ## Reset the room to the one they came in from, set player_loc to the
        ## door they left out of
        room = room.room_list[room.old_room]
        room.player_loc = room.door_used

    ## If they're standing on a door (again, not really...)
    if info == 'door':

        ## sets room.door to the name of the door they left out of.  It checks
        ## if the player's loc is any of the three exits, and if it is, then it
        ## sets the key of that value to room.door
        for item in room.exits_dict:
            if room.player_loc == room.exits_dict[item]:
                room.door = item

        ## If the door they're trying to leave out of is already saved as an
        ## instance, then load that instance (merch data is already preserved!)
        if room.door in room.room_list:
            room = room.room_list[room.door]

        ## If it's not already in the instance dict (room.room_list), then make
        ## a new room.  Set the player's loc to the first exit in the list
        ## (room_num + 'a') bc whatever, get a new random merchant location from
        ## the list of
        ## cells (see the get_location method under rooms), and then make a new
        ## merchant for that room, add it to the dictionary of merchants (re:
        ## preserved).
        else:

            room = room.new_room()
            room.player_loc = room.exits_list[0]
            room.player_gb = room.player_loc
            room.merchant_loc = room.get_location()
            merchant_dict[room.room_num] = Merchant()


        ## Curently broken.
    if info == 'forward':

        room = room.room_list[(room.room_num + 1)]
        room.player_loc = room.player_ll

        ## If they're standing on a merchant, set the current merchant to the
        ## one assigned to the current room, and then run it's activation method
        ## see activate(self) under merchants
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
