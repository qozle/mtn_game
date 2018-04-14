from time import *
import os




#####  FUNCTION FOR CLEARING THE SCREEN  #####
def cls():

    os.system("cls" if os.name == "nt" else "clear")


def skill_window(toon):

    while True:
        cls()
        print("""This is the skills page.  You can see the skill books you've aquired,
which skills you've trained, and information on what skill you're currently training.\n""")
        
        if toon.current_skill == 'nope':
            print("You are not currently training anything")
        else:
            print("""You are currently training {}. You started training it {}. It's train time is {}.
It will be done on {}.""".format(toon.current_skill.__name__, ctime(toon.current_skill.start),
                             toon.current_skill.train_time,
                             ctime(toon.current_skill.finish)))

        print("You can currently train:\n")

        for item in toon.skill_books:
            print("-" + str(item) + "\n")

        info = input("""Enter a skillbook (case sensetive) to begin training it, or [Back]. >""")
        
        for item in toon.skill_books:
            if item == info:
                skill = Skillbook(time(), toon.skill_books[item], item.strip('Skillbook: '))
                toon.current_skill = skill
                toon.skill_books.pop(item)
                input("You're now training {}! Enter return to continue. >".format(toon.current_skill.__name__))
                return toon
                
        if info == 'back':
            info = 'none'
            return toon
            break


def check_training(toon):

        if toon.current_skill == 'nope':
            pass
        elif toon.current_skill.finish <= time():
            cls()
            input("""You've finished training {}!  You can now use it.  See the skills window for more
info.  Enter return to continue. >""".format(toon.current_skill.__name__))
            toon.skills.append(toon.current_skill.__name__)
            toon.current_skill = 'nope'



class Skillbook:

    def __init__(self, start, train_time, name, **kwargs):

        self.start = start
        self.train_time = train_time
        self.finish = self.start + self.train_time
        self.train_time = train_time
        self.__name__ = name  
        
