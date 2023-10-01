import tkinter as tk
from tkinter import messagebox

def start_quiz():
    # Function to start the quiz
    messagebox.showinfo("Quiz Started", "The quiz will begin!")

def show_instructions():
    # Function to show the instructions pop-up
    instructions = "Welcome to the Capital Cities Quiz!\n\n"\
                   "You will be presented with questions about the capitals of different countries.\n"\
                   "Choose the correct answer from the options provided.\n"\
                   "Good luck!"
    messagebox.showinfo("Instructions", instructions)

# Create the main window
root = tk.Tk()
root.title("Capital Cities Quiz")
root.geometry("400x300")  # Set the window size to 400x300

# Create the title label
title_label = tk.Label(root, text="Capital Cities Quiz", font=("Arial", 24))
title_label.pack(pady=20)

# Create the "Start Quiz" button
start_button = tk.Button(root, text="Start Quiz", font=("Arial", 16), command=start_quiz)
start_button.pack(pady=10)

# Create the "Instructions" button
instructions_button = tk.Button(root, text="Instructions", font=("Arial", 16), command=show_instructions)
instructions_button.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()