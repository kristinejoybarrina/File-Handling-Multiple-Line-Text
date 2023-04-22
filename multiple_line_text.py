# Kristine Joy Barrina #BSCPE 1-5 # April 23, 2023
# Creating a python program that writes multiple line of text contents to another text file.

# Pseudocode

# Import python modules
import tkinter as tk
from tkinter import *
import os

# Initialize loop control
response_loop_ctrl = 0

# Use while loop
while response_loop_ctrl == 0:
    response_loop_ctrl += 1

# Ask the user for input
    user_input = str(input("Enter a line of text: "))

# Create and open a file named mylife.txt
    with open ("mylife.txt", "a") as multiple_text:
        
        # Append the user's input to mylife.txt and separate it by new line
        multiple_text.write (str(user_input) + "\n")

        # Ask the user if he/she wants add another line
        user_response = str(input("Do you want to enter another line y/n? "))
        
        # Display error message if the input is more than 1 character
        if len(user_response) == 1:
            response_loop_ctrl = 0
            
            if user_response == "y":
                response_loop_ctrl = 0
            
            else:
                response_loop_ctrl = 1
                
        else:
            response_loop_ctrl = 0
            print ('Enter only one letter! "y/n/" \n')

# Design the output using tkinter
# Create an instance window
root = Tk ()

# Create the dimension of window
root.geometry("450x150")
root.title("Multiple Line Text")

# Create buttons
multiple_line_text_button = Button (root, text= "MULTIPLE LINE TEXT", bg="yellow")

# Create a label in window
label_window = Label(root, text= "Click here!", fg="black", justify=CENTER, font=("Arial", 14, "bold"))

# Let the pack method declares the position attributes
label_window.pack (fill="both")
multiple_line_text_button.pack ()

tk.mainloop()


