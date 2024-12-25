import tkinter as tk
from tkinter import messagebox
import random

def play_game():
    user_choice = user_choice_var.get()
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
        scores["User"] += 1
    else:
        result = "Computer wins!"
        scores["Computer"] += 1

    label_result.config(text=f"Result: {result}\nYou chose: {user_choice}, Computer chose: {computer_choice}")
    label_scores.config(text=f"Scores - You: {scores['User']}, Computer: {scores['Computer']}")

def reset_game():
    user_choice_var.set("Rock")
    label_result.config(text="Result: ")
    scores["User"] = 0
    scores["Computer"] = 0
    label_scores.config(text=f"Scores - You: {scores['User']}, Computer: {scores['Computer']}")

# Initialize scores
scores = {"User": 0, "Computer": 0}

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Create and place widgets
label_instruction = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
label_instruction.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

user_choice_var = tk.StringVar(value="Rock")
option_menu = tk.OptionMenu(root, user_choice_var, "Rock", "Paper", "Scissors")
option_menu.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

button_play = tk.Button(root, text="Play", command=play_game)
button_play.grid(row=2, column=0, padx=10, pady=10)

button_reset = tk.Button(root, text="Reset", command=reset_game)
button_reset.grid(row=2, column=1, padx=10, pady=10)

label_result = tk.Label(root, text="Result: ", font=("Arial", 12))
label_result.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

label_scores = tk.Label(root, text=f"Scores - You: {scores['User']}, Computer: {scores['Computer']}", font=("Arial", 12))
label_scores.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
