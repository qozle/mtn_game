import random
import os


class Character:

    def __init__(self, *args, **kwargs):

            self.inventory = ['Torch', 'Book', 'Dagger']

            for key, value in kwargs.items():
                setattr(self, key, value)


    #####  FUNCTION FOR CREATING A NEW CHARACTER  #####
    def create_character(self):

        CLASSES = ['rogue', 'warrior', 'cleric', 'wizard']

        name = input("""Hi!  Welcome!  You don't have a character yet.  Let's make one! What's your character's name? >""")

        ht = input("Great!  How tall is your character? >")
        ec = input("Cool!  What color are your characters eyes? >")
        hair = input("Nice!  What color is your character's hair? >")

        toon = Character(name=name, ht=ht, ec=ec, hair=hair)

        print("""
Alright {}, you are {} feet tall, have {} eyes and {} hair.  Also, you
have this in your inventory:\n""".format(toon.name, toon.ht, toon.ec, toon.hair))

        for item in toon.inventory:
            print(item + "\n")

        while True:
            which_class = input("What class do you want to be? {} >".format(CLASSES))

            if which_class.lower() == CLASSES[0]:

                from library import Rogue
                toon = Rogue(5, 9, 2)
                print("Ok, you are a Rogue!  STATS: str: {}, dex: {}, con: {}".format(toon.strn,
                                                                                      toon.dex,
                                                                                      toon.con))
                break
            elif which_class.lower() == CLASSES[1]:

                from library import Warrior
                toon = Warrior(9, 4, 7)
                print("Ok, you are a Warrior!  STATS: str: {}, dex: {}, con: {}".format(toon.strn,
                                                                                      toon.dex,
                                                                                      toon.con))
                break
            elif which_class.lower() == CLASSES[2]:

                from library import Cleric
                toon = Cleric(5, 7, 6)
                print("Ok, you are a Cleric!  STATS: str: {}, dex: {}, con: {}".format(toon.strn,
                                                                                      toon.dex,
                                                                                      toon.con))
                break
            elif which_class.lower() == CLASSES[3]:

                from library import Wizard
                toon = Wizard(2, 6, 3)
                print("Ok, you are a Wizard!  STATS: str: {}, dex: {}, con: {}".format(toon.strn,
                                                                                       toon.dex,
                                                                                       toon.con))
                break

            else:

                input("Sorry, that's not one of the choices, press return to try again.")
                pass
        return toon






#####  CLASSES, CHILD CLASS OF CHARACTER  #####
class Rogue(Character):

    def __init__(self, strn, dex, con, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.strn = strn
        self.dex = dex
        self.con = con

        for key, value in kwargs.items():
                setattr(self, key, value)

        self.sneaky = True

class Warrior(Character):

    def __init__(self, strn, dex, con, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.strn = strn
        self.dex = dex
        self.con = con

        for key, value in kwargs.items():
                setattr(self, key, value)

        self.brave = True

class Cleric(Character):

    def __init__(self, strn, dex, con, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.strn = strn
        self.dex = dex
        self.con = con

        for key, value in kwargs.items():
                setattr(self, key, value)

        self.holy = True

class Wizard(Character):

    def __init__(self, strn, dex, con, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.strn = strn
        self.dex = dex
        self.con = con

        for key, value in kwargs.items():
                setattr(self, key, value)

        self.arcane = True
