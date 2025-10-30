# --- Import statements ---
import random
import math
import os
from datetime import datetime
import matplotlib.pyplot as plt
import hello_world


# --- Random number generation ---
number = random.randint(0, 10)
print(f"Random number between 0 and 10: {number}")


# --- Using math module ---
square_root = math.sqrt(number)
print(f"Square root of {number}: {square_root:.2f}")

circle_area = math.pi * (number ** 2)
print(f"Area of a circle with radius {number}: {circle_area:.2f}")


# --- Using os module ---
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

files = os.listdir()
print("Files in this directory:")
for file in files:
    print(f" - {file}")


# --- Using datetime module ---
now = datetime.now()
print(f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}")


# --- Using matplotlib to visualize data ---
numbers = list(range(0, 11))
squares = [n ** 2 for n in numbers]

plt.plot(numbers, squares, marker='o')
plt.title("Squares of Numbers 0–10")
plt.xlabel("Number")
plt.ylabel("Square")
plt.grid(True)
plt.show()


# --- Custom module ---
hello_world.hello_world()
