import threading

# Ask the user for the number of inputs
n = int(input("Enter the number of elements: "))

# Initialize an empty list
numbers = []

# Ask the user for each number and add it to the list
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Function to calculate square of numbers
def square(numbers):
        print("Square of %d is %d" % (numbers, numbers**2))

# Function to calculate cube of numbers
def cube(numbers):
        print("Cube of %d is %d" % (numbers, numbers**3))

# Create threads for square and cube functions


threads = []

# Start the threads
for i in threads:
    thread1 = threading.Thread(target=square, args=(numbers,))
    thread2 = threading.Thread(target=cube, args=(numbers,))
    threads.append(thread1)
    threads.append(thread2)
    
for thread in threads:
    thread.start()
    
for thread in threads:
    thread.join()

print("Calculation is complete.")