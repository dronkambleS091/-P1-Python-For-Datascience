import math

n = int(input("How many numbers? "))

for i in range(n):
    try:
        num = float(input("Enter a number: "))
        
        if num < 0:
            print("Square root of a negative number is not possible.")
        else:
            print("Square root =", math.sqrt(num))
            
    except ValueError:
        print("Invalid input! Please enter a valid number.")
