 # Print square of numbers from 1 to 10

for i in range(1, 11):
    print("Square of", i, "=", i*i)

count = 0

print("\nEnter 5 numbers:")

for i in range(5):
    num = int(input("Enter number: "))
    
    if num % 2 == 0:
        count += 1

print("Even numbers count =", count)
