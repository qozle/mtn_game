import random
import os
from pathlib import Path as path


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

        p = path(str(path.cwd()) + "\\saves")
        directory = sorted(item for item in p.iterdir())
        

        for item in directory:
            if item.name == filename:
                p = path(item.name)

                raw = p.read_text()
                kwlist = []
                for item in raw.split("+"):
                    kwlist.append(item)
                kwlist.remove('')
                keys = []
                prevalues = []
                for items in kwlist:
                    keys.append(items.split("-")[0])
                    prevalues.append(items.split("-")[1])
                values = []
                for item in prevalues:
                    values.append(item.split(","))
                for item in values:
                    item.remove('')
                charinfo = {}
                for item in keys: charinfo[item] = values[keys.index(item)]
                charinfo['name'] = charinfo['name'][0]
                charinfo['ht'] = charinfo['ht'][0]
                charinfo['ec'] = charinfo['ec'][0]
                charinfo['hair'] = charinfo['hair'][0]
                charinfo['current_skill'] = charinfo['current_skill'][0]

                return charinfo

            
                
                
        
                




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
