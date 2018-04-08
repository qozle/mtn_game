import random
import os



#####  FUNCTION FOR CLEARING THE SCREEN  #####
def cls():

    os.system("cls" if os.name == "nt" else "clear")


#####  DEFINE MERCHANT CLASS  #####
class Merchant:

    def __init__(self):

        self.inventory_list = ['Torch', 'Snake', 'Chicken', 'Sponge', 'Axe',
                               'Flint and steel', 'Rope', 'Rations', 'Water',
                               'Pick', 'Shovel', 'Leather', 'Wood', 'Flute']
        self.inventory = random.sample(self.inventory_list, 3)

        self.names_list = ['Barry bird', 'Joe', 'Billy', 'Whislter', 'Frog',
                      'George', 'Jean-paul', 'Pierre', 'Sach', 'Jessie',
                      'John', 'Wheeler', 'Chase', 'Margaret', 'Grandma',
                      'Xao', 'Tyrone', 'Muhamed', 'Shliome', 'Bill', 'Guy',
                      'Samantha', 'Evenlyn']
        self.name = random.sample(self.names_list, 1)

        self.greetings_list = ["Well, it's awfully dark in here, no?",
                          "If I don't have what you  need, no one does!",
                          "Awright, let's transact!",
                          "Has your face always looked like that?"
                          "After this, I'm going home to make a great soup!",
                          "You live in teh dungeon...I wash bawrn in et!",
                          "Oh man, I've gotta switch my laundry!!!",
                          "Every star belongs in the sky =)",
                          "The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. ",
                          "We're all on a sinking ship!",
                          "The planet is flat!",
                          "The planet is round!"]
        self.greeting = random.sample(self.greetings_list, 1)


    def activate(self, player_inv):

        cls()

        print('\n')
        print("Hi, my name's {}.  {}".format(self.name, self.greeting))
        print('\n')
        print("Here's what I have to sell:")
        print('\n')
        for item in player_inv: print("-" + str(item) + '\n')
        print('\n')
        print("Here's what you  have to sell:")
        print('\n')
        for item in self.inventory: print("-" + str(item) + '\n')
        info = input("You can [Buy], [Sell], or go [Back]. >")

        return info 

    
    def buy(self, player_inv):

        cls()
        print('\n')
        for item in self.inventory: print("-" + str(item) + "\n")
        info = input("What would you like to buy?  Or [Back]. >")
        info = info.lower()
        for item in self.inventory:
            if info == item.lower():
                player_inv.append(self.inventory.pop(self.inventory.index(item)))
                return player_inv
        if info == 'back':
            return "back"

    def sell(self, player_inv):

        cls()
        print('\n')
        for item in player_inv: print("-" + str(item) + "\n")
        info = input("What would you like to sell?  Or [Back]. >")
        info = info.lower()
        for item in player_inv:
            if info == item.lower():
                self.inventory.append(player_inv.pop(player_inv.index(item)))
                return player_inv
        if info == back:
            return "back"

        
            



        
