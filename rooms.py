import random



class Room:

    ##### DEFINE INITALIZE CONDITIONS #####
    def __init__(self, room_num, room_list = {}, **kwargs):

        
        self.cells = [] # map cells, list of tuples (coords)
        self.xlist = [] # x coords to be generated
        self.ylist = [] # y coords to be generated
        self.player_loc = []
        self.merchant_loc = []
        self.exits = [] # list to contain the border cells of the map
        self.room_num = room_num # room's identity holder
        self.player_ll = [] # to hold player's last location in the room
        self.player_gb = [] # to hold the return position to go back to last room
        self.room_list = room_list # to hold entire list of all rooms, bug but ty
        self.room_list[self.room_num] = self # probbaly this, add self to the list

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
                self.cells.extend([(x, y)])

        count = 0

        ## creates a new list of cells which is all the border cells on the
        ## current map.
        for cell in self.cells:
            x, y = cell
            if x == 0:
                self.exits.extend([cell])
            if x == self.length:
                self.exits.extend([cell])
            if y == 0:
                self.exits.extend([cell])
            if y == self.width:
                self.exits.extend([cell])

        ## picks 3 of the border cells randomly.  These will later be set to
        ## be doors.  I have to fix this in the draw_map method under rooms
        ## so that it draws the doors properly on the border of the room.  This
        ## part of it should be fine though.
        self.chosen_exits = random.sample(self.exits, 3)

        ## ok this one is a beast.  probably the nastiest line I have written to date.  This makes a dictionary
        ## where key= room_num + (a, b, or c in order per item) and value= each of the three chosen exit location
        ## cell values.  We're gonna need this later in mtn_game to check against the players loc and return the
        ## given room number for that loc (which will be one of the three exits).  This might be heavy handed.
        self.exits_dict = {}
        label = 'abc'
        for item in self.chosen_exits:
            self.exits_dict[str(int(self.room_num[0]) + 1) + str( label[self.chosen_exits.index(item)])] = item

        
        self.exits_list = list(self.exits_dict.values())

        
        ## Just take in whatever key:value arguments (KWARGS = Key Word Arguments) that we spit in and set them
        ## as current attributes for the self (cuurent instance)
        for key, value in kwargs.items():
            setattr(self, key, value)
            


        
 


#####  FUNCTION FOR MAKING NEW ROOM  #####  This makes a new room and sends over any of the old rooms data.
    def new_room(self):

        for item in self.exits_dict:
            if self.player_loc == self.exits_dict[item]:
                self.door_label = item[-1] # sets door_label to whichever door the players loc is on (a, b, or c)
                self.door_used = self.exits_dict[item] # sets door_used to which door the user is standing on

        ## make a new room, give it old_room (the door we came in from), the current lsit of rooms, and set it's
        ## rooms number to whatever the current room number is but plus 1 (so 1a, 2c, 3a, 4b, 5c, whatever)
        newroom = Room(old_room=self.room_num, room_list=self.room_list,
                       room_num = str(int(self.room_num[0]) + 1) + str(self.door_label))
        
        ## spit back the new room, because this is what we're setting as the new active room variable under the
        ## main while loops in mtn_game
        return newroom




        

    #####  FUNCTION FOR GETTING A RANDOM LOCATION IN SELF.CELLS  ####
    def get_location(self):

        loc = random.sample(self.cells, 1)
        return loc[0]
        
       
        

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

        


    #####  FUNCTION FOR GETTING AVAILABLE MOVES #####
    def avail_moves(self):

        x, y = self.player_loc
        self.moves = ['Up', 'Down', 'Left', 'Right']
        if self.player_loc == self.player_ll:
            self.moves.append('Forward')
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
        if self.player_loc == self.player_gb:
            self.moves.append('Back')
        elif self.player_loc in self.chosen_exits:
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
                elif cell in self.chosen_exits:
                    output = tile.format("D")
                else:
                    output = tile.format("_")
            else:
                line_end = "\n"
                if cell == self.player_loc:
                    output = tile.format('X|')
                elif cell == self.merchant_loc:
                    output = tile.format('M|')
                elif cell in self.chosen_exits:
                    output = tile.format('D|')
                else:
                    output = tile.format('_|')
            print(output, end=line_end)
