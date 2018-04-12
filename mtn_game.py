import random
import os
from pathlib import Path as path
from character import *
from rooms import *
from merchants import *
from skills import *
from time import time, ctime


#####  FUNCTION FOR CLEARING THE SCREEN  #####
def cls():

    os.system("cls" if os.name == "nt" else "clear")

variable= "I'm adding a random string variable for git testing"


#####  FUNCTION FOR CREATING NEW CHARACTER  #####
def new_toon():
    print("Hi!  Welcome!  You don't have a character yet.  Let's make one!\n")
    name = input("Let's make one! What's your character's name? >")
    ht = input("Great!  How tall is your character? >")
    ec = input("Cool!  What color are your characters eyes? >")
    hair = input("Nice!  What color is your character's hair? >")
    charinfo = {}
    charinfo.update(name=name, ht=ht, ec=ec, hair=hair)
    toon = Character()

    print("""
    Alright {}, you are {} feet tall, have {} eyes and {} hair.

    Also, you have this in your inventory:\n""".format(name, ht, ec, hair))
    for item in toon.inventory:
        print(item + "\n")

    while True:
        which_class = input("Which class would you like to be? {} >".
                            format(CLASSES))
        if which_class.lower() == CLASSES[0]:
            toon = Rogue(charinfo)
            input("Ok, you are a Rogue!  STATS: str: {}, dex: {}, con: {}.  Press return to start game. >".
                  format(toon.strn, toon.dex, toon.con))
            break

        elif which_class.lower() == CLASSES[1]:
            toon = Warrior(charinfo)
            input("Ok, you are a Warrior!  STATS: str: {}, dex: {}, con: {}.  Press return to start game. >".
                  format(toon.strn, toon.dex, toon.con))
            break
        
        elif which_class.lower() == CLASSES[2]:
            toon = Cleric(charinfo)
            input("Ok, you are a Cleric!  STATS: str: {}, dex: {}, con: {}.  Press return to start game. >".
                  format(toon.strn, toon.dex, toon.con))
            break

        elif which_class.lower() == CLASSES[3]:
            toon = Wizard(charinfo)
            input("Ok, you are a Wizard!  STATS: str: {}, dex: {}, con: {}.  Press return to start game. >".
                  format(toon.strn, toon.dex, toon.con))
            break

        else:
            input(
                "Sorry, that's not one of the choices, press return to try again.")

    return toon



                    #####   SET INITIAL CONDITIONS  #####

CLASSES = ['rogue', 'warrior', 'cleric', 'wizard']
## This makes the dictionary that will contain key=room_num, value=Merchant()
merchant_dict = {}
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

## This sets up the file structure and checks if there are files in /saves
p = path(str(path.cwd()) + "/saves")
if p.is_dir() == False: p.mkdir()
directory = sorted(item for item in p.iterdir())





#####  START OF GAME  #####
cls()
if directory == []:
    toon = new_toon()
    
else:
    info = input("You can make a [new] character, or [load] a saved one.  What would you like to do? >")
    info.lower()
    info.strip()
    if info == 'new':
        toon = new_toon()
    if info == 'load':
        print("\n\n")
        for item in directory: print(item.name + "\n\n")
        info = input("Enter a character file to load it. >")
        info.strip()
        for item in directory:
            if info == item.name:
                charinfo = Character.load_toon(item.name)
                toon = Character(charinfo)
                if toon.current_skill == 'nope': continue
                else:
                    toon.current_skill = Skill(float(toon.currentskill[0]), float(toon.currentskill[1]),
                                               toon.current_skill)
            



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

    ## IF SKILLS
    if info == 'skills':
        
        SKILLS = ['wit', 'haggle', 'jump', 'climb', 'focus']
        for item in toon.inventory:
            if item.lower() in SKILLS:
                toon.skill_books.append(toon.inventory.pop(toon.inventory.index(item)))
        
        while True:
            cls()
            print("""This is the skills page.  You can see the skill books you've aquired,
which skills you've trained, and information on what skill you're currently training.\n""")
            
            if toon.current_skill == 'nope':
                print("You are not currently training anything")
                
            else:
                print("""You are currently training {}. You started training it {}. It's train time is {}.
It will be done on {}.""".format(toon.current_skill.__name__, ctime(int(toon.current_skill.start)), toon.current_skill.train_time,
                                 ctime(int(toon.current_skill.finish))))

            print("You can currently train:\n")

            for item in toon.skill_books:
                print("-" + str(item) + "\n")

            info = input("""Enter a skill book to begin training it, or [Back]. >""")
            info = info.lower()
            info = info.strip()

            
            for item in toon.skill_books:
                if item.lower() == info:
                    skillname = toon.skill_books.pop(toon.skill_books.index(item))
                    skill = Skill(time(), 15, skillname)
                    setattr(toon, 'currentskill', [time(), 15])
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
        Character.save_toon(toon.__dict__, nameinfo)
        info = input("Ok!  Your character has been saved in a file as {}.  Enter return to continue. >".format(nameinfo))



    # Check that the victory condition works
    if info == 'cheat':
        toon.inventory += invis_merchant.inventory_list

    ## TIME TO GTFO oops caps
    if info == 'quit':
        break


    
