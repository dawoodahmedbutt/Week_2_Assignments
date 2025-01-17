import random

# Sample stories that will generate the final story based on user inputs
sample_stories = [
    "The {adjective} {animal} discovered a {noun} hiding behind the {place}.",
    "Deep in the {place}, a {adjective} {noun} learned how to {verb} from a wise {animal}.",
    "Nobody knew why the {noun} would {verb} every time it visited the {place}.",
    "The {adjective} {animal} built a secret {place} where {noun}s could {verb} freely.",
    "There was a legend about a {adjective} {noun} that would {verb} near the {place}.",
    "Every {animal} in the {place} wanted to {verb} with the {adjective} {noun}.",
    "The most {adjective} {place} was home to a {noun} that loved to {verb}.",
    "A {adjective} {animal} taught the {noun} how to {verb} in the middle of the {place}.",
    "The {noun} had never seen such a {adjective} {animal} {verb} before.",
    "At the edge of the {place}, the {adjective} {noun} met a mysterious {animal}.",
    "The {animal} couldn't believe that the {noun} could {verb} so {adjective}.",
    "Inside the {place}, the {adjective} {animal} found a {noun} trying to {verb}.",
    "The {noun} traveled to every {place} to {verb} with each {adjective} {animal}.",
    "Sometimes the {adjective} {noun} would {verb} while the {animal} watched.",
    "The {place} became famous when a {adjective} {animal} and {noun} decided to {verb} there."
]

# Function to collect user inputs for a given category
def user_inputs(category, count):

    print(f"Please input {count} {category}.")
    return [input(f"Please insert {category[:-1]} #{i + 1}: ").strip() for i in range(count)]
# Category[-1] means that the last character of category is being removed, i.e. adjectives --> adjectives as the s (the final character) is being removed.  
# #{i+1} is which adjective i'm inserting. so if I'm on my second one, then it will say "Please insert adjective 2"

# Define the number of items to collect. This could be whatever the user chooses. For simplicity, 3 has been chosen
upper_bound = 3

# Collect inputs for each category (adjectives is the category in user_inputs, and upper_bound is the count)
adjectives = user_inputs("adjectives", upper_bound)
animals = user_inputs("animals", upper_bound)
nouns = user_inputs("nouns", upper_bound)
places = user_inputs("places", upper_bound)
verbs = user_inputs("verbs", upper_bound)

while True:
# Ask the user if they would like to hear a story
    message = input("Would you like to hear a story? yes/no: ").lower()
    if message == "yes":
            # Create a story if the user chooses yes
            story = (random.choice(sample_stories)).format(
                adjective = random.choice(adjectives),
                animal = random.choice(animals),
                noun = random.choice(nouns),
                place = random.choice(places),
                verb = random.choice(verbs),
    )
            print ("Enjoy your story!")
            print(story) 

    elif message == "no":
            # Another story will not be displayed if the user chooses no. 
            print ("Thank you for listening to me talk. ")
            break
        # If the input is not yes/no, ask the user to input correctly
    else:
            print ("Pick yes or no")

