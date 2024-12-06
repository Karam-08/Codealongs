n = 4

def factorial(n):
    if n < 2:
        return 1 # Sends the number 1 back and ends the function
    else:
        return n * factorial(n - 1) # Keeps the result to be used again in the function

print(factorial(n))