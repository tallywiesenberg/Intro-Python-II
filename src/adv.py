from player import Player
from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('Player 1', room['outside'])
# Write a loop that:
#
# * Prints the current room name 
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there. 
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def adv():

    # print(room[player.current_room].n_to)
    def ask():
        input_ = ''
        while not input_:
            print('Your current room: ', player.current_room.name)
            print("Your current room's description: ", player.current_room.description)
            input_ = input("You're in a room! Enter a cardinal direction! Press q to quit. \n")
        return input_
    
    input_ = ask()

    def move(input_):
        if input_.lower() in ['north', 'south', 'east', 'west']:
            #TODO movement
            if input_ == 'north':
                if player.current_room.n_to is not None:
                    player.current_room = player.current_room.n_to
                    input_ = ask()
                    move(input_)
                else:
                    print("Can't go that direction!\n")
                    input_ = ask()
            if input_ == 'south':
                if hasattr(player.current_room, 's_to'):
                    player.current_room = room[player.current_room].s_to
                else:
                    print("Can't go that direction!\n")
                    input_ = ask()
            if input_ == 'east':
                if hasattr(player.current_room, 'e_to'):
                    player.current_room = current_room.e_to
                else:
                    print("Can't go that direction!\n")
                    input_ = ask()
            else:
                if hasattr(current_room, 'w_to'):
                    player.current_room = current_room.w_to
                else:
                    print("Can't go that direction!\n")
                    input_ = ask()
        elif input_.lower() == 'q':
            exit()
        else:
            print('\nInvalid input. Try again!')
            input_ = ask()
            move(input_)
        
        return move(input_)
    move(input_)
adv()