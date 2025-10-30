def hello_world() -> None:
    """
    Prints a friendly greeting message to the console.

    This function demonstrates a simple Python function that
    performs an action (printing text) but does not return any value.
    """
    print("Hello World")  # Output a greeting to the screen


# This block ensures the code runs only when the file is executed directly,
# not when imported as a module into another script.
if __name__ == "__main__":
    hello_world()  # Call the function to print "Hello World"
