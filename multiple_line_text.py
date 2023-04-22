# Kristine Joy Barrina #BSCPE 1-5 # April 23, 2023
# Creating a python program that writes multiple line of text contents to another text file.

# Pseudocode

# Initialize loop control
response_loop_ctrl = 0

# Use while loop
while response_loop_ctrl == 0:
    response_loop_ctrl += 1

# Ask the user for input
    user_input = str (input ("Enter a line of text: "))

# Create and open a file named mylife.txt
    with open ("mylife.txt", "a") as multiple_text:

        # Append the user's input to mylife.txt and separate it to new line
        multiple_text.write (str (user_input) + "\n")
        
        
# Ask the user if he/she wants add another line
# Display error message if the input is more than 1 character
# Design the output using tkinter
