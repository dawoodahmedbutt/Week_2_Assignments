# Descriptions of rooms
descriptions = {
    "outside": "greenery all around you, you are outside the house, which stands in front of you.",
    "kitchen": "a kitchen filled with food. Ahead of you is the living room; stairs are to your left.",
    'living room': "comfy furniture placed in a living room. Ahead is the cellar; behind you is the kitchen.",
    'stairs': "some tall stairs ahead. Up them is the bathroom. The kitchen is to your right.",
    'bathroom': "a marble bathroom. Behind you are the stairs.",
    'cellar': "a dank cellar. Behind you is the living room."
}

# Exits from each room, i.e, where can the user go
locations = {
    'outside': {'N': 'kitchen','S':'no','E':'no','W':'no'},
    'kitchen': {'N': 'living room', 'W': 'stairs','S':'outside','E':'no'},
    'living room': {'S': 'kitchen', 'N': 'cellar','E':'no','W':'no'},
    'stairs': {'N': 'bathroom','S':'no','E':'kitchen','W':'no'},
    'bathroom': {'S': 'stairs','N':'no','E':'no','W':'no'},
    'cellar': {'S': 'living room','N':'no','E':'no','W':'no'}
}

# Map of locations
LOCATIONS_MAP = """
                    +-------+
                    |cellar |
                    +-------+
                        ↑ N
                        |
                        ↓ S
+---------+        +------------+
| bathroom|        |living room |
+---------+        +------------+
    ↑ N                 ↑ N
    |                   |
    ↓ S                 ↓ S
+---------+  W      +---------+
|  stairs | ←-----→ | kitchen |
+---------+      E  +---------+
                        ↑ N
                        |
                        ↓ S
                    +--------+
                    | outside|
                    +--------+
"""

# Define the core functionality to move between rooms.
def move_room(current_location):
    """ Takes current location, asks for user input and checks it, then updates location. """
    print("\n" + "You see " + descriptions[current_location])

    # Get direction from locations dictionary, representing room exits
    north = locations[current_location]["N"]
    south = locations[current_location]["S"]
    east = locations[current_location]["E"]
    west = locations[current_location]["W"]
    # Define possible directions the user can go
    if north != "no":
        print(f"You can go north to {north}.")
    if south != "no":
        print(f"You can go south to {south}.")
    if east != "no":
        print(f"You can go east to {east}.")
    if west != "no":
        print(f"You can go west to {west}.")

    # Prompt user for input
    direction = input("Where do you want to go? (N/E/S/W) or type 'Q' to exit: ").upper()
    # Check if input is Q, which is the quit game command
    if direction == 'Q':
        return 'Q'
    # Checking user input is a valid direction (N/E/S/W)
    elif direction in locations[current_location]:
        # Checking direction is valid for the location, if not user stays in current_location or updates location
        if locations[current_location][direction] == "no":
            print("\n" + "INVALID DIRECTION, PLEASE TRY AGAIN!")
            return current_location
        else:
            new_location = locations[current_location][direction]
            return new_location
    else:
        # If user input is invalid, user does not change current_location
        print("\n" + "INVALID INPUT. PLEASE TRY AGAIN!")
        return current_location


def main():
    """ Main game loop. """
    # The game starts outside
    current_location = 'outside'
    # Print welcome message and print ASCII map
    print("Welcome to the Text Based Adventure Game!")
    print(LOCATIONS_MAP)
    # Keep playing until the user types Q (exit)
    while current_location != 'Q':
        current_location = move_room(current_location)
    print("Thanks for playing!")

# Execute the game
if __name__ == "__main__":
    main()
