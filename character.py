import random
import os
from pathlib import Path as path
import pickle


## Function for clearing the screen, this should probably just be imported
def cls():

    os.system("cls" if os.name == "nt" else "clear")


class Character:

    def __init__(self, charinfo={}, *args, **kwargs):

        self.inventory = ['Torch', 'Book', 'Dagger']
        self.skills = [] # Skills fully trained
        self.skill_books = [] # Skills trainable
        self.current_skill = 'nope' # Skill that's currently training

        for key, value in charinfo.items():
            setattr(self, key, value)

        for key, value in kwargs.items():
            setattr(self, key, value)


    def load_toon(filename):

        saves = path("../mtn_game/saves/")
        directory = sorted(item for item in saves.iterdir())
        

        for item in directory:
            if item.name == filename:
                p = path(str(saves) + "/" + str(item.name))
                f = open(p, 'rb')
                char = pickle.load(f)
                f.close()               

                return char


    def save_toon(toon, filename):

        p = path("../mtn_game/saves/" + str(filename))
        f = open(p, "wb+")
        pickle.dump(toon, f)
        f.close()
        
    ## Walks user through creating new character
    def new_toon():
        CLASSES = ['rogue', 'warrior', 'cleric', 'wizard']
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




#####  CLASSES, CHILD CLASS OF CHARACTER  #####
class Rogue(Character):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.strn = 7
        self.dex = 9
        self.con = 3

        for key, value in kwargs.items():
                setattr(self, key, value)

        self.sneaky = True

class Warrior(Character):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.strn = 9
        self.dex = 4
        self.con = 7

        for key, value in kwargs.items():
                setattr(self, key, value)

        self.brave = True

class Cleric(Character):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.strn = 5
        self.dex = 7
        self.con = 6

        for key, value in kwargs.items():
                setattr(self, key, value)

        self.holy = True

class Wizard(Character):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.strn = 3
        self.dex = 5
        self.con = 3

        for key, value in kwargs.items():
                setattr(self, key, value)

        self.arcane = True
