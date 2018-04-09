import random
from merchants import *



class Room:

    ##### DEFINE INITALIZE CONDITIONS #####
<<<<<<< HEAD
    def __init__(self, room_num=0, room_label="a", exits_used = {}, room_list = {}, gb=[], last_room=[], **kwargs):
=======
    def __init__(self, room_num=0, room_label="a",room_idt="0", lastroom=None, **kwargs):
>>>>>>> max's-branch

        
        self.cells = [] 
        self.xlist = [] 
        self.ylist = [] 
        self.player_loc = []
<<<<<<< HEAD
        self.merchant_loc = []
        self.exits = {} # list to contain the border cells of the map
        self.room_num = room_num # room's identity holder
        self.player_ll = [] # to hold player's last location in the room
        self.room_label = room_label
        self.room_list = room_list # to hold entire list of all rooms, bug but ty
        self.gb = gb
        self.exits_used = exits_used
        self.last_room = last_room
        
        self.length = random.randrange(1, 11) # get a random length
        self.width = random.randrange(1, 11) # get a random width

        ## generates the x coords for the room length
        count = 0
        while count <= self.length:
            self.xlist.extend([count])
            count += 1

        ## generates the y coords for the room width
        count = 0
        while count <= self.width:
            self.ylist.extend([count])
            count += 1

        ## for each x coord, for each y coord, add x, y as a tuple to cells
        ## to actually make the cells list from the above two values.
        for xcoord in self.xlist:
            for ycoord in self.ylist:
                x, y = xcoord, ycoord
=======
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
>>>>>>> max's-branch
                self.cells.extend([(x, y)])
                
        for key, value in kwargs.items():
            setattr(self, key, value)

<<<<<<< HEAD
        count = 0
        exits_list = []
        ## creates a new list of cells which is all the border cells on the
        ## current map.
        for cell in self.cells:
            x, y = cell
            if x == 0:
                exits_list.extend([cell])
            if x == self.length:
                exits_list.extend([cell])
            if y == 0:
                exits_list.extend([cell])
            if y == self.width:
                exits_list.extend([cell])

        ## picks 3 of the border cells randomly.  These will later be set to
        ## be doors.  I have to fix this in the draw_map method under rooms
        ## so that it draws the doors properly on the border of the room.  This
        ## part of it should be fine though.
        self.chosen_exits = random.sample(exits_list, 3)

        label = 'abc'
        for item in self.chosen_exits:
            self.exits[label[self.chosen_exits.index(item)]] = item
=======
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
                    
>>>>>>> max's-branch

    def make_doors(self):
        rooma_info = self.room_num+1, 'a', str(self.room_num+1)+'a', self
        roomb_info = self.room_num+1, 'b', str(self.room_num+1)+'b', self

<<<<<<< HEAD
    #####  FUNCTION FOR MAKING NEW ROOM  #####  This makes a new room and sends over any of the old rooms data.
    def new_room(self):

        self.player_ll = self.player_loc
        lroom = self
        
        for item in self.exits:
            if self.player_loc == self.exits[item]:
                self.exits_used[item] = ""
                self.door_taken = item

        self.room_idt = str(self.room_num + 1) + self.room_label 
        self.room_list[self.room_idt] = self
        
        newroom = Room(room_num = self.room_num + 1, room_label = self.door_taken, room_list = self.room_list,
                       last_room=lroom)
        newroom.player_loc = newroom.exits['a']
        newroom.gb = newroom.exits['a']
        newroom.merchant_loc = newroom.get_location()

        return newroom
        
    #####  FUNCTION FOR GOING BACK  #####
    def go_back(self):

        self.player_ll = self.player_ll
        oldroom = self.last_room
        oldroom.exits_used[self.room_label] = self

        return oldroom


    #####  FUNCTION FOR GOING FORWARD  #####
    def go_forward(self):

        label = ""
        self.player_ll = self.player_loc
        for item in self.exits:
            if self.player_loc == self.exits[item]:
                label = item
=======
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
>>>>>>> max's-branch

        for item in self.exits_used:
            if label == item:
                newroom = self.exits_used[item]

        return newroom
        
       
    #####  FUNCTION FOR GETTING AVAILABLE MOVES #####
    def avail_moves(self):

        x, y = self.player_loc
        self.moves = ['Up', 'Down', 'Left', 'Right']
<<<<<<< HEAD
        for item in self.exits_used:
            if self.player_loc == self.exits_used[item]:
                self.moves.append('Forward')
        if self.player_loc == self.player_ll:
            self.moves.append('Forward')
=======
        
>>>>>>> max's-branch
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
<<<<<<< HEAD
        if self.player_loc == self.gb:
=======
        if self.player_loc == self.doors['back'][1] and not self.room_num == 0:
>>>>>>> max's-branch
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
        
