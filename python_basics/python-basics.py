'''
WHAT IS PYTHON
Python is a high-level, general-purpose, and very popular programming language. Python programming language (latest Python 3) is being used in web development, Machine Learning applications, along with all cutting-edge technology in Software Industry.

Python language is being used by almost all tech-giant companies like - Google, Amazon, Facebook, Instagram, Dropbox, Uber… etc.

The biggest strength of Python is huge collection of standard library which can be used for the following:

Machine Learning
GUI Applications (like Kivy, Tkinter, PyQt etc. )
Web frameworks like Django (used by YouTube, Instagram, Dropbox)
Image processing (like OpenCV, Pillow)
Web scraping (like Scrapy, BeautifulSoup, Selenium)
Test frameworks
Multimedia
Scientific computing
Text processing and many more..

Python is currently the most widely used multi-purpose, high-level programming language, which allows programming in Object-Oriented and Procedural paradigms. Python programs generally are smaller than other programming languages like Java. Programmers have to type relatively less and the indentation requirement of the language, makes them readable all the time.
'''
'''PYTHON COMMENTS and Rules for all of programming
Rule 1: Comments should not duplicate the code.
Rule 2: Good comments do not excuse unclear code.
Rule 3: If you can't write a clear comment, there may be a problem with the code.
Rule 4: Comments should dispel confusion, not cause it.
Rule 5: Explain unidiomatic code in comments.
Rule 6: Provide links to the original source of copied code.
Rule 7: Include links to external references where they will be most helpful.
Rule 8: Add comments when fixing bugs.
Rule 9: Use comments to mark incomplete implementations.

# is a single line comment
Anything between '''''' is a single to multiple line comment
'''

'''VARIABLES: Variables do not need to be declared with any particular type, and can even change type after they have been set. Just start with a initial value or not

VARIABLE NAMES: A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
***A variable name must start with a letter or the underscore character
***A variable name cannot start with a number
***A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
***Variable names are case-sensitive (age, Age and AGE are three different variables)
***A variable name cannot be any of the Python keywords.
MULTI VARIABLE CREATION:
#f_name,l_name,age = "Khadeem","Bernard", 21
print(f_name,l_name,age) or print(f_name+l_name+age)

or
#initialValue = start = i = 0

CASTING VARIABLES:If you want to specify the data type of a variable, this can be done with casting.
'''
'''PYTHON DATATYPES:
Python has the following data types built-in by default, in these categories:

Text Type:  str
Numeric Types:  int, float, complex
Sequence Types: list, tuple, range
Mapping Type:   dict
Set Types:  set, frozenset
Boolean Type:   bool
Binary Types:   bytes, bytearray, memoryview
None Type:  NoneType
'''

'''Python Indentation
Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

Python uses indentation to indicate a block of code.'''



'''PYTHON STRING MANIPULATION 
String Slicing returns a piece of a string that is dictated by the inputs.
Ex.'''
test= "This is a test string in Python"
print(test[5]) #how to access a character in a string
print(test[15:35]) #how to access a range of characters in a string

'''String Methods'''
print(test.upper())#uppercase letters
spacey = "   This has a lot of spacey before and after   "
print(spacey.strip().upper()) # Gets rid of the extra spaces
location = (spacey.find('before'))
print(spacey[location:(location*6)])

'''String Concatenation:'''
print(test + " " + spacey)

name = 'Take 5'
amount = 10
cost = 20
statements = "I had my favorite candy {0}, I bought a total of {1} for ${2}"
print(statements.format(name,amount,cost))

#Need to finish string quotes using the escape character

'''Conditionals for Python'''
import math
x = 23
last_name = "Abbas"
first_name = "Karam"
age = 16
fake_age = "21"
patience = 3
verbal_abuse = 50
kenny_is_alive = True
if kenny_is_alive and age > 25 or kenny_is_alive == False:
    print("This is what you are doing. This is what I want you to do.")
if last_name == "Abbas" or last_name == "Karam":
    print("You're a certified 1000 ELO chess enjoyer.")
if last_name == "Abbas" and first_name == "Karam":
    print("It's not over for you yet. Keep it pushing.")
if age > 20:
    print("You old!")
    age += 1
elif age == 19:
    print("Your birthday last year was nice.")
else:
    print("Generation of Social Goblins")
    age = 19
if first_name == "Karam":
    print("NO!")
if not kenny_is_alive:
    print("Kevin Whyyyyyy")
print("Karam Abbas")
print(2**6)
print(math.sqrt(age))
print(math.pow(2,6))
grade = 84
if grade >= 90:
    print("A")
if grade >= 80:
    print("B")
if grade >= 70:
    print("C")
if grade >= 60:
    print("D")
else:
    print("F")
print(math.pi)
print(math.gcd(0, 34))
print(math.isfinite(2000))
print(math.cos(10))
print(math.asin(1))
print(math.cos(3.14159265359))
print("I'm blue da boo de da boo dae")
# Lists In Python
'''Lists are used to store multiple items in a single variable
If you have coded in another language it works the same as an array
'''
food = ["rice", "wheat", "bread", "potatoes", "meat", "water"]

print(food)
print(len(food)) # Length of the list
print(food[2]) # Prints a specific part of the list
print(sorted(food)) # Sorts the list alphabetically
print(food)
food.sort() # Sorts and alters the original list
print(food)
food.reverse() # Reverses the list order
print(food)
food.append("maize") # Added to the end of the list OR
food[6] = "maize" # Added to the end
print(food)
print(food.index("potatoes")) # Returns the index of the item in the list 
del food[4]
print(food)

# Dictionaries - Key value pairs like a dictionary and fefinition
favGames = {"Hussein": "Warframe", "Maryam": "She is not a gamer...", 
"Mom": "Royal Match"}
print(favGames)
print(favGames.keys()) # All of the keys in the dictionary
print(favGames.values()) # All of the values in the dictionary
print(len(favGames))

users = {"Karam": 5558840, "Mom": 6666, "Maryam": 1212958186}
user = "starBoy"
password = "theWeeknd"

login_username = input("What is your username?")
login_password = input("What is your password?")
if login_username == user and login_password == password:
    print("Success!")
else:
    print("Failure.")

#To the Loops: For Loops used for sequential loops like a list, dictionary set or even a string
for thing in food:
    print(thing)

for y in favGames:
    print(y)

for thing in food:
    print("Nah!")

# While loops

contacts = []
index = 2

while index <= 10:
    print(index)
    index += 2
