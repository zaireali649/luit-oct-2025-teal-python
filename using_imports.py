# --- Import statements ---
import random  # Used to generate random numbers
import math  # Provides access to mathematical functions like sqrt and pi
import os  # Lets you interact with the operating system (e.g., directories)
from datetime import datetime  # Used to get the current date and time
import matplotlib.pyplot as plt  # Used to create visualizations and plots
import hello_world  # Custom module that prints a greeting


# --- Random number generation ---
number = random.randint(0, 10)  # Generate a random integer between 0 and 10
print(f"Random number between 0 and 10: {number}")  # Print the random number


# --- Using math module ---
square_root = math.sqrt(number)  # Calculate the square root of the number
print(f"Square root of {number}: {square_root:.2f}")  # Display square root rounded to 2 decimals

circle_area = math.pi * (number ** 2)  # Calculate area of a circle (πr²)
print(f"Area of a circle with radius {number}: {circle_area:.2f}")  # Display circle area


# --- Using os module ---
current_directory = os.getcwd()  # Get the current working directory
print(f"Current working directory: {current_directory}")  # Print current directory path

files = os.listdir()  # List all files and folders in the current directory
print("Files in this directory:")
for file in files:  # Loop through each file/folder name
    print(f" - {file}")  # Print the name of each file/folder


# --- Using datetime module ---
now = datetime.now()  # Get the current date and time
print(f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}")  # Format and print timestamp


# --- Using matplotlib to visualize data ---
numbers = list(range(0, 11))  # Create a list of numbers from 0 to 10
squares = [n ** 2 for n in numbers]  # Create a list of squares for each number

plt.plot(numbers, squares, marker='o')  # Plot numbers vs squares with circle markers
plt.title("Squares of Numbers 0–10")  # Add a title to the graph
plt.xlabel("Number")  # Label the x-axis
plt.ylabel("Square")  # Label the y-axis
plt.grid(True)  # Add a grid for better readability
plt.show()  # Display the plot window


# --- Custom module ---
hello_world.hello_world()  # Call the custom function from hello_world.py
