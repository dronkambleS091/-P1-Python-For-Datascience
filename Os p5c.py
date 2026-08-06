import threading

# Function to print even and odd numbers
def even_odd():
    print("Even Numbers:")
    for i in range(1, 11):
        if i % 2 == 0:
            print(i, end=" ")

    print("\n\nOdd Numbers:")
    for i in range(1, 11):
        if i % 2 != 0:
            print(i, end=" ")

# Function to reverse a string
def reverse_string(text):
    print("\n\nOriginal String:", text)
    print("Reversed String:", text[::-1])

# Main program
if __name__ == "__main__":
    print("Multithreading Example\n")

    t1 = threading.Thread(target=even_odd)
    t2 = threading.Thread(target=reverse_string, args=("Computer",))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("\n\nAll threads completed.")
print("Dron Kamble")
