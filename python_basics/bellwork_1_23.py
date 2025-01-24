# 1: Operators

# a. Evaluate the following expressions and provide the results:
# 5 + 3 * 2,  (10 - 4) / 2,  7 % 3,  2 ** 3 + 1

print(5 + 3 * 2)
print((10 - 4) / 2)
print(7 % 3)
print(2 ** 3 + 1)

# b. Write a Python program that checks if a number is divisible by both 3 and 5. Use the modulo operator (%).

fizzBuzz = 22

if fizzBuzz % 5 == 0 and fizzBuzz % 3 == 0:
    print(fizzBuzz, "is divisible by both 3 and 5")
else:
    print(fizzBuzz, "is not divisible by 3 and 5")

# ========================================================================================================

# 2: 
# a. Write a function square_and_cube(num) that takes a number as input and returns both its square and cube.

def square_and_cube(num):
    square = num*num
    cube = num*num*num
    return square, cube

result = square_and_cube(3)

print(result)

# b:

def greet_user(name):
    return "Hello" + " " + name

greet = greet_user("Alice")

print(greet)

# Example input: "Alice"
# Expected output: "Hello, Alice!"

# 3: Loops
# a:

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# b:

while True:
    user_input = input("Enter a number or 'exit': ")
    
    if user_input == "exit":
        break  # Exit the loop if the user types "exit"

    try:
        number = int(user_input)
        if number % 2 == 0:
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")
    except ValueError:
        print("Invalid input. Please enter a number or 'exit'.")

# Bonus Factorial

n = 6

def factorial(n):
    if n < 2:
        return 1 # Sends the number 1 back and ends the function
    else:
        return n * factorial(n - 1) # Keeps the result to be used again in the function

print(factorial(n))