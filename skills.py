from time import *
import os



#####  FUNCTION FOR CLEARING THE SCREEN  #####
def cls():

    os.system("cls" if os.name == "nt" else "clear")

variable= "I'm adding a random string variable for git testing"



class Skill:

    def __init__(self, start, train_time, name, **kwargs):

        self.start = start
        self.train_time = train_time
        self.finish = self.start + self.train_time
        self.train_time = train_time
        self.__name__ = name


def activate(toon):
    
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
It will be done on {}.""".format(toon.current_skill.__name__, ctime(int(toon.current_skill.start)),
                             toon.current_skill.train_time,
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
                toon.current_skill = skill
                return toon
                
        if info == 'back':
            info = 'none'
            return toon
            break     





    
        
