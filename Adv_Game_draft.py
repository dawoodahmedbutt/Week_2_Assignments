# The below is an early draft of Assignment 4. 
# The group ultimately decided to go in a different direction, but it was still fun creating this
# Challenges:
#           The code gets very complex very quickly. Loops wihtin loops are created, and it can get hard to keep a track of these. 
#           I was trying to find a way to print a message which says which room I'm in, but wasn't ablemto
#           I was also unsure how to go from the cellar when i get my math problem wrong... so essentially, got it wrong, and go to the cellar (the cellar is past the living room... so a loop of some sort
# Although this isn't the assignment I'm submitting, I would like some feedback if possible. 


print ("some form of intro message")
print ("You have magically arrived at the mistery house!")
print ("You are outside the house. It's an old looking house, with the roof tiles falling off, the paint could do with some work, and the front yard is severely overgrown")

# Ask the user if they'd like to enter the house
message = input(print ("Do you want to enter the house?")).lower()
if message == 'yes':
    print ("You have entered the house and are now in the kitchen")
elif message == 'no':
    print ("You have decided to turn away from the house, and have quit the game")
else:
    print ('Invalid choice. Please input yes or no')

    # Kitchen Description
print("You are now in the kitchen. The cabinets are chipped and hanging slightly ajar, the tiles are cracked and stained, "
      "and a faint smell of grease lingers in the air, mingling with the musty scent of forgotten leftovers.")
print("There is a smell of gas coming from the oven.")

# Get the user to choose whether they want to investigate the oven
while True:
    oven = input("Do you want to investigate the smell? (yes/no): ").lower()
    if oven == 'yes':
        print("There was gas leaking from the oven, and the moment you opened it, the gas ignited with a nearby ignition source. "
              "The house blew up, but you were lucky to make it out with barely any scratches.")
        break
    elif oven == 'no':
        print("You spotted that the oven was on, and so you turned it off. Phew! Disaster averted.")
        break
    else:
        print("Invalid choice. Please input 'yes' or 'no'.")

# Ask the user if they want to go up the staircase or into the living room
print("You can now choose to enter the staircase or proceed into the living room.")

while True:
    room = input("Where would you like to go? (staircase/living room): ").lower()

    if room == 'staircase':
        print("You are on the staircase. The wooden steps creak loudly with each movement, "
              "the banister is loose and splintered, and a layer of dust blankets everything, "
              "interrupted only by the faint trail of footprints.")
        print("The staircase is blocked. In order to get past, you must solve a problem.")

        # Get the user to answer the problem
        while True:
            try:
                math_problem = int(input("What is 3x3+3? "))
                if math_problem == 12:
                    print("You have correctly solved the problem. You may now proceed.")
                    break
                else:
                    print("Oops! Wrong answer! The staircase cracks open, and you fall through the stairs, ending up in the cellar.")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        break

    elif room == 'living room':
        print("You're now in the living room.")
        break

    else:
        print("Invalid input. Please enter 'staircase' or 'living room'.")