"""
Priyanka Gorentla code changes done on 1/28/2023.
I have added Tuples,sets and Dictionaries related to my domain Yoga

"""



"""
TUPLES
"""

# Create some tuples with weight on joining day and after few months of few students
tuple = (45,65,78,93,24,51)
tupleBefore= ('Georg',[189,230,210,190,220,225])
trainer_name1 , ageBefore = tupleBefore
tupleAfter = ()
print(f"length of tuple after is:", len(tupleAfter))
print()
tupleAfter = 'Alex',[155,190,180,170,195,202]
trainer_name2 , ageAfter = tupleAfter
print(f"tupleAfter and its lenght:", tupleAfter , len(tupleAfter))
print()
print(f"Index and values of tupleAfter:", list(enumerate(tupleAfter)))
print()
print(f"Trainer1 and trainer2 name :",trainer_name1,trainer_name2)


# tuple concatenation

tupleCat = tupleBefore + tupleAfter

# tuple repetition
tupleThrice = tuple * 3

#Printing tuples
print(f"{tupleBefore = }")
print()
print(f"{tupleAfter = }")
print()
print(f"{tupleCat = }")
print()
print(f"{tupleThrice = }")
print()

# tuple membership testing

hasGeorge = 'George' in tupleBefore   # True
hasGeorgeinAfter =  'George' in tupleAfter  # False

print(f"checking geroge in tupleBegore and tupleAfter:", hasGeorge , hasGeorgeinAfter)
print()


# tuple indexing (0 is first, -1 is last, or 1 less than the length)


first = tupleBefore[0]
second = tupleBefore[1]
last = tupleBefore[-1]
second_third = tupleAfter[1][2]

print(f"Displaying first,second and last values of tuples:" , first,'\n',
second,'\n' ,
last,'\n',
second_third)
print()

# Use tuples to return multiple values from a function


def divide_and_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder


q, r = divide_and_remainder(10, 3)
print(f"Quotient: {q}, Remainder: {r}")
print()


"""
SETS 
"""

setZ = {'Breathing Excercise','cobra pose','Tree Pose','Triangle Pose','Plant Pose'}
setX = {'Pranayama','Yamas','Niyamas','Bridge Pose'}
set1 = {23,65,78,45,64}
set2 = {44,76,89,43,67}

print(f"setZ:", setZ)
print()
print(f"setX:", setX)
print()

# set union
setY = setZ | setX

print(f"setY is union of X and Z:", setY)
print()

# set intersection
setW = setZ & setX
print(f" setW is Intersection of X and Z:", setW)
print()

# set difference
set3 = set1 - set2
print(f"set3 is difference between set1 and set2:", set3)
print()

set1.pop()
set1.add(99)

print(f"new set1:",set1)

# sets are often used to remove duplicates from a list
# after gettin the set, convert it back to a list with list() or []
listWords = ["vijay", "priyanka", "vikram", "nani", "mike" , "annie","vijay"]
print(f"listwords with duplicates:", listWords)

setWords = set(listWords)
listWordsNoDuplicates = [setWords]

print(f"listwords without duplicates:", listWordsNoDuplicates)
print()

"""
DICTIONARIES 
"""

Locations = {"Florida": "FL", "New Jersey": "NJ", "North Carolina": "NC", "California":"CA"}
print("Key's of Location:", Locations.keys())
print()
Details = {"name": "George", "age": 35, "weight_kg": 85.2, "level": "Intermediate", "Gender":"Male"}
print("Values of Details:",Details.values())
print()
list = {"George":1,"Alex":2,"Lisa":3,"Max":4}
list2 = {number: name for name, number in list.items()}
print(f"Dictionaty comprehention:",list2)
print()



with open("C:\\Users\\KONGA\\Documents\\datafun-03-datatypes\\about_yoga.txt") as file_object:
    word_list = file_object.read().split()

word_counts_dict = {}
for word in word_list:
    if word in word_counts_dict:
        word_counts_dict[word] += 1
    else:
        word_counts_dict[word] = 1

print(word_counts_dict)


# IMPORTANT: Dictionary comprehesions - the preferred approach

# Create a dictionary of word counts from a list of words
# A dictionary is alawys key:value pairs
# Say "I want word:count for each word in word_list"
# Remember to wrap the result in curly braces
word_counts_dict = {word: word_list.count(word) for word in word_list}

# Spend most of your practice on comprehensions - they are
# key to transforming data in Python.

