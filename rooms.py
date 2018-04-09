import random
from merchants import *



class Room:

    ##### DEFINE INITALIZE CONDITIONS #####
    def __init__(self, room_num=0, room_label="a",room_idt="0", lastroom=None, **kwargs):

        
        self.cells = [] 
        self.xlist = [] 
        self.ylist = [] 
        self.player_loc = []
        self.merchant_loc = [] 
        self.room_num = room_num 
        self.room_label = room_label
        self.room_idt = room_idt
        self.lastroom = lastroom
        self.merchant = Merchant()
        self.length = random.randrange(1, 11) 
        self.width = random.randrange(1, 11) 

        # Populate cells list (map)
        for x in range(self.length+1):
            for y in range(self.width+1):
                self.cells.extend([(x, y)])
                
        for key, value in kwargs.items():
            setattr(self, key, value)

        # Build a list of all the border cells to choose doors from 
        door_list = []
        for cell in self.cells:
            x, y = cell
            if x == 0 or x == self.length or y == 0 or y == self.width:
                door_list.extend([cell])

        a, b, c = random.sample(door_list, 3)
        self.door_coords = [a, b, c]
        # Initiate doors dict
        self.doors = {'back': [lastroom, a], 'a':['rooma', b], 'b':['roomb', c]}
                    

    def make_doors(self):
        rooma_info = self.room_num+1, 'a', str(self.room_num+1)+'a', self
        roomb_info = self.room_num+1, 'b', str(self.room_num+1)+'b', self

        rooma = self.new_room(rooma_info)
        roomb = self.new_room(roomb_info)

        self.doors['a'][0] = rooma
        self.doors['b'][0] = roomb

       
    #####  FUNCTION FOR MAKING NEW ROOM  #####  
    def new_room(self, room_info):

        room_num, room_label, room_idt, lastroom = room_info
        newroom = Room(room_num, room_label, room_idt, lastroom)
        newroom.player_loc = newroom.get_location()
        newroom.merchant_loc = newroom.get_location()

        return newroom

        
    #####  FUNCTION FOR GOING BACK  #####
    def go_back(self):

        oldroom = self.lastroom
        return oldroom


    #####  FUNCTION FOR GETTING AVAILABLE MOVES #####
    def avail_moves(self):

        x, y = self.player_loc
        self.moves = ['Up', 'Down', 'Left', 'Right']
        
        if x == self.length:
            self.moves.remove('Down')
        if x == 0:
            self.moves.remove('Up')
        if y == self.width:
            self.moves.remove('Right')
        if y == 0:
            self.moves.remove('Left')
        if self.player_loc == self.merchant_loc:
            self.moves.append('Merchant')
        if self.player_loc == self.doors['back'][1] and not self.room_num == 0:
            self.moves.append('Back')
        elif self.player_loc in self.door_coords and not self.player_loc == self.doors['back'][1]:
            self.moves.append('Door')

        return self.moves


    ##### FUNCTION FOR MOVING THE CHARACTER #####
    def move_player(self, player_move):

        x, y = self.player_loc
        player_move = player_move.lower()

        if player_move == 'left':
            y -= 1
        if player_move == 'right': 
            y += 1
        if player_move == 'up':
            x -= 1
        if player_move == 'down':
            x += 1
    
        self.player_loc = x, y

        
    #####  FUNCTION FOR DRAWING THE MAP  #####
    def draw_map(self):

        print(" _" * (self.width + 1))
        tile = "|{}"

        for cell in self.cells:
            x, y = cell
            if y < self.width:
                line_end = ""
                if cell == self.player_loc:
                    output = tile.format("X")
                elif cell == self.merchant_loc:
                    output = tile.format("M")
                elif cell in self.door_coords:
                    output = tile.format("D")
                else:
                    output = tile.format("_")
            else:
                line_end = "\n"
                if cell == self.player_loc:
                    output = tile.format('X|')
                elif cell == self.merchant_loc:
                    output = tile.format('M|')
                elif cell in self.door_coords:
                    output = tile.format('D|')
                else:
                    output = tile.format('_|')
            print(output, end=line_end)


    #####  HELP SECTION  #####    
    def help(self, *args, **kwargs):

        for x, y in kwargs.items():
            setattr(self, x, y)

        input("""
Things typed in brackets ("[]") are things you can type in as commands.  They
are not case sensetive.

To move:       [Up], [Down], [Left], [Right]
Inventory:     [Inv]
Skills:        [Skills]
Quit:          [Quit]

Press return to continue. >""")


#####  FUNCTION FOR GETTING A RANDOM LOCATION IN SELF.CELLS  ####
    def get_location(self):

        loc = random.sample(self.cells, 1)
        return loc[0]
        
