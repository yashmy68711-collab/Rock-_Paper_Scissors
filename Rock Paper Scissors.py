import tkinter as tk
from tkinter import messagebox
import random

choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    result = ""

    if user_choice == computer_choice:
        result = "It's a Tie!"

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        user_score += 1

    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(
        text=f"Computer Chose: {computer_choice}\n{result}"
    )

    score_label.config(
        text=f"You: {user_score} | Computer: {computer_score}"
    )

window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("450x300")

title = tk.Label(
    window,
    text="Rock Paper Scissors",
    font=("Arial", 18, "bold")
)

title.pack(pady=15)

rock_btn = tk.Button(
    window,
    text="Rock",
    width=15,
    command=lambda: play("Rock")
)

rock_btn.pack(pady=5)

paper_btn = tk.Button(
    window,
    text="Paper",
    width=15,
    command=lambda: play("Paper")
)

paper_btn.pack(pady=5)

scissors_btn = tk.Button(
    window,
    text="Scissors",
    width=15,
    command=lambda: play("Scissors")
)

scissors_btn.pack(pady=5)

result_label = tk.Label(
    window,
    text="Choose an option",
    font=("Arial", 12)
)

result_label.pack(pady=15)

score_label = tk.Label(
    window,
    text="You: 0 | Computer: 0",
    font=("Arial", 12, "bold")
)

score_label.pack()

window.mainloop()