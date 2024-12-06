# Task 1: String Manipulation

print("Test 1:")
print("You can type literally anything")

response = input() 

uppercase_response = response.upper() # Makes every character in the response uppercase
lowercase_response = response.lower() # Every character in the response becomes lowercase
reverse_response = response[::-1] # Reverses the input

vowel_erase = response.replace('A', '*').replace('a', '*').replace('E', '*').replace('e', '*').replace('I', '*').replace('i', '*').replace('O', '*').replace('o', '*').replace('U', '*').replace('u', '*')
# Replaces every vowel with a * uppercase and lowercase

character_count = len(response) # Counts how many characters are in the input

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("You typed", response)
print(uppercase_response)
print(lowercase_response)
print(reverse_response)
print(vowel_erase)
print(character_count)

# Prints out variables



# Part 2: Math operators

x = input("Pick your first number: ")
y = input("Pick your second number: ")
# You pick the number

print("You chose the numbers", x, "and", y)

add = int(x) + int(y)
subtract = int(x) - int(y)
multiply  = int(x) * int(y)
divide = int(x) / int(y)
modulus = int(x) % int(y)
exponent = int(x) ** int(y)

# X and Y get converted to an integer and go through one of these formulas

# -----------------------------------------------------------------------------------------

print(x, "plus", y, "is", add)
print(x, "minus", y, "is", subtract)
print(x, "times", y, "is", multiply)
print(x, "divided by", y, "is", divide)
print(x, "divided by", y, "leaves a remainder of", modulus)
print(x, "to the power of", y, "is", exponent)

# Prints out the solution





# Part 3: Concatenation

first_name = input("What is your first name? ")
last_name = input ("What is your last name? ")

print("Hello", first_name, last_name + "!")

# A "," leaves a space while a "+" leaves no space

fav_number = input("What is your favorite number? ")


print("Your modified name is:", first_name, last_name + fav_number)

# Part 4: Functions
name = input("What is your name? ")

def greet_user(name):
    print("Hello there,", name + "!")

greet_user(name)

# -----------------------------------------------------

length = 9
width = 4

def calculate_area(length, width):
    return length * width
    # Multiples the length and the width and then returns the value

area = calculate_area(length, width)
# Shorten the function

print("The area of the Rectangle is", area)

# -------------------------------------------------------

fahrenheit = 95

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
    # Fahrenheit goes through calculations to become Celsius and the value is returned

temp = convert_to_celsius(fahrenheit)
# Shorten the function

print("The temperature is", temp, "degrees Celsius")