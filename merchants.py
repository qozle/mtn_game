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


    def activate(self, player_inv):

        cls()
        info = input("""

Hello!  It's awfully dark in here, isn't it?  I have some things you might be
interested in, care to see what I have? [Buy], [Sell], or [Back]""")

        info = info.lower()

        while True:

            print(info)
            if info == 'buy':
                print("\n")
                print("Here's what I have to sell!:")
                print("\n")
                for item in self.inventory:
                    print("-" + item + "\n")
                info = input("Enter an item to buy it!")

                for item in self.inventory:
                    if info.lower() == item.lower():
                        self.inventory.remove(item)
                break
                return item


            if info =='sell':
                print('\n')
                print("Here's what you have to sell!:")
                print("\n")
                for item in player_inv:
                    print('-' + item + "\n")
                info = input("Enter an item to sell it!")

                for item in player_inv:
                    if info.lower() == item.lower():
                        player_inv.remove(item)
                break
                return player_inv


            if info == 'back':
                break
                return 'back'

            else:

                info = input("""Sorry, I don't understand.  Try again- do you
want to [Buy], [Sell], or go [Back]? >""")
