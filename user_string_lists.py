"""
Priyanka Gorentla code changes done on 1/28/2023.
I have added different string lists related to my domain Yoga

"""

import random
import math
import statistics

# Define a string list
list_tech = ['Breathing Excercise','cobra pose','Tree Pose','Triangle Pose','Plant Pose','Pranayama','Yamas','Niyamas','Bridge Pose']

# Define a list of levels
list_level = ["Beginning", "Intermediate", "Advanced"]

# Define a list of gender's 
list_gender = ["male", "female"]

# Define a list of trainee names
list_trainees = ["vijay", "priyanka", "vikram", "nani", "mike" , "annie"]

# Define a list of places
list_loc = ["Jacksonville", "Charlotte", "Detroit", "Pennsylvania", "Edison", "Harrisburg"]


# read in about yoga to get a list of words
with open("C:\\Users\\KONGA\\Documents\\datafun-03-datatypes\\about_yoga.txt", "r") as fileObject:
    text = fileObject.read()
    list_words = text.split()  # split on whitespace
    unique_words = set(list_words)  # remove duplicates

# Print the count and list of words
word_ct = len(list_words)

# Print the count and list of unique words
unique_word_ct = len(unique_words)


# define functions 

def yoga_techniques(list):
     for name in list_tech:
        return list_tech
print('Some of Yoga Techniques are :', list_tech)
print()

# Upper case list

LIST = [item.upper() for item in list_gender]

print('upper case list:',LIST)
print()

# Create a random sentence
sentence = (
    f"The {random.choice(list_loc)} institute with trainee {random.choice(list_trainees)} will teach {random.choice(list_tech)}"
    f" techniques to {random.choice(list_gender)} for {random.choice(list_level)} levels."
)
print()
print(sentence)
print()
print(f"length of unique words from about_yoga text file:", unique_word_ct)
print()
print(f"length of text file about_yoga:", word_ct)
print()

# For finding the minimum and maximum strings first we need to convert string into complete lower case or UPPER case as below:

min_loc = min(list_loc,key=lambda s:s.lower())
max_loc = max(list_loc,key=lambda s:s.lower())

print(f"Minimum location and maximum location:", min_loc ,'\n', max_loc)
print()

# using Zip funcationality

for location,trainees,levels in zip(list_loc,list_trainees,list_level):
    print(f'LOCATION={location}; TRAINEES={trainees} LEVELS={levels}')


# Game bot for rock, paper, scissors ................

# Define a function to get the winner message
# Use keyword arguments to be clear about the order of the arguments
def get_message(traineelevel, trainerlevel):
    if traineelevel == trainerlevel:
        return "both trainer and trainee are in same level"
    elif traineelevel == "Beginning":
        if trainerlevel == "Advanced":
            return "Trainee need to learn a lot"
        else:
            return "You are almost done..keep going"


ready_for_continous_level_checks = True  # change this when ready

while True:
    if not ready_for_continous_level_checks:
        quit()  # don't get stuck in an infinite loop until ready

    print()
    trainee_level = input("Say intermediate or beginning or advanced or q to quit:")
    if trainee_level == "q":
        break  # break out of the loop
    # if still here, the bot makes a choice
    # don't indent unnecessarily
    trainer_level = random.choice(list_level)
    print(f"You said {trainee_level}.")
    print(f"I said {trainer_level}.")
    # When calling a function, the order of arguments matters!
    # We don't want to accidentally provide the guesses in the wrong order
    # So we'll use keyword arguments so the order doesn't matter
    msg1 = get_message(traineelevel=trainee_level, trainerlevel=trainer_level)
    msg2 = get_message(trainerlevel=trainer_level, traineelevel=trainee_level)
    if msg1 == msg2:
        print(msg2)
    print()
    print("This program will run forever unless you type q to quit.")
    print("or use Ctrl-C to stop the program.")
    print()

