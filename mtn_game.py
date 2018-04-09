import random
import os
from character import *
from rooms import *
from merchants import *
from skills import *
from time import time, ctime

## I'm testing to see if this affects just the local branch and not master, as
## should


#####  FUNCTION FOR CLEARING THE SCREEN  #####
def cls():

    os.system("cls" if os.name == "nt" else "clear")

variable= "I'm adding a random string variable for git testing"

<<<<<<< HEAD
=======

                    #####   SET INITIAL CONDITIONS  #####
>>>>>>> max's-branch

#####   SET INITIAL CONDITIONS  #####
## This makes the dictionary that will contain key=room_num, value=Merchant()
merchant_dict = {}

## This makes the players character and fills it will the inventory
toon = Character()
toon.create_character()

## This makes the first room and makes it merchant, assigns it to the merch_dict
room = Room()
<<<<<<< HEAD
room.player_loc = room.get_location()
=======
room.make_doors()
room.player_loc = room.doors['back'][1]
>>>>>>> max's-branch
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

    cls()
    room.draw_map()
    print("\n\n")
    print("ROOM {} ".format(room.room_idt) * 6)

    win_check()
    
    info = input('\nWhat do you want to do?  [Help] for help.  You can move {}. >'.format
                 (room.avail_moves()))
    info = info.lower()
    info = info.strip()

    if info == 'skills':
        
        SKILLS = ['wit', 'haggle', 'jump', 'climb', 'focus']
        for item in toon.inventory:
            if item.lower() in SKILLS:
                toon.skill_books.append(toon.inventory.pop(toon.inventory.index(item)))
        
        while True:
            cls()
            print("""This is the skills page.  You can see the skill books you've aquired,
which skills you've trained, and information on what skill you're currently training.\n""")
            
            if toon.current_skill == None:
                print("You are not currently training anything")

            else:
                print("""You are currently training {}. You started training it {}. It's train time is {}.
It will be done on {}.""".format(toon.current_skill.__name__, ctime(toon.current_skill.start), toon.current_skill.train_time,
                                 ctime(toon.current_skill.finish)))

            print("You can currently train:\n")

            for item in toon.skill_books:
                print("-" + str(item) + "\n")

            info = input("""Enter a skill book to begin training it, or [Back]. >""")
            info = info.lower()
            info = info.strip()

            
            for item in toon.skill_books:
                if item.lower() == info:
                    skill = toon.skill_books.pop(toon.skill_books.index(item))
                    skill = Skill(time(), 15, skill)
                    toon.current_skill = skill

            if info == 'back':
                info = 'none'
                break       
            
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

<<<<<<< HEAD
    
=======
>>>>>>> max's-branch
    if info == 'back':
        if room.player_loc == room.doors['back'][1] and room.room_num != 0:
            room = room.go_back()
        else: print("You can't go out this door yet sorry =(")

<<<<<<< HEAD
        room = room.go_back() 

=======
>>>>>>> max's-branch
    if info == 'door':
        if room.player_loc == room.doors['a'][1] or room.player_loc == room.doors['b'][1]:
            for item in room.doors:
                if room.player_loc == room.doors[item][1]:
                    room = room.doors[item][0]
                    room.make_doors()
                    room.player_loc = room.doors['back'][1]
                    room.merchant_loc = room.get_location()

<<<<<<< HEAD
        room = room.new_room()       

        
        ## Curently broken.
    if info == 'forward':

        room = room.go_forward()

        
=======
        elif room.player_loc == room.doors['back'][1]:
            print("This door only goes back, use [Back].")

        else:
            print("You're not on a valid door =(")

>>>>>>> max's-branch
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


    
