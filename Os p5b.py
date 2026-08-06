import threading

# Function to calculate factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"Factorial of {n} = {fact}")

# Main program
if __name__ == "__main__":
    print("Multi-threaded Factorial Program\n")

    numbers = [4, 5, 6]
    threads = []

    # Create and start threads
    for num in numbers:
        t = threading.Thread(target=factorial, args=(num,))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print("\nAll threads completed.")
print("Dron Kamble")
