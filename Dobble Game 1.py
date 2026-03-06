import string
import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Global variables to hold the cards and the matching symbol
card1 = []
card2 = []
samesymbol = ""
turn = 0  # To keep track of turns
pp1 = 0   # Player 1's score
pp2 = 0   # Player 2's score
MAX_TURNS = 10  # Maximum number of turns in the game

# Function to create and display the cards
def create_cards():
    global card1, card2, samesymbol

    # Reset symbols and cards
    symbols = list(string.ascii_letters)
    card1 = [0] * 5
    card2 = [0] * 5

    post1 = random.randint(0, 4)
    post2 = random.randint(0, 4)

    # Same symbol for both cards
    samesymbol = random.choice(symbols)
    symbols.remove(samesymbol)

    if post1 == post2:
        card1[post1] = samesymbol
        card2[post1] = samesymbol
    else:
        card1[post1] = samesymbol
        card2[post2] = samesymbol
        card1[post2] = random.choice(symbols)
        symbols.remove(card1[post2])
        card2[post1] = random.choice(symbols)
        symbols.remove(card2[post1])

    i = 0
    while i < 5:
        if i != post1 and i != post2:
            alphabet1 = random.choice(symbols)
            symbols.remove(alphabet1)
            alphabet2 = random.choice(symbols)
            symbols.remove(alphabet2)
            card1[i] = alphabet1
            card2[i] = alphabet2
        i += 1

    # Display the cards in the GUI
    card1_label.config(text=f"Card 1: {card1}")
    card2_label.config(text=f"Card 2: {card2}")

    # Update which player's turn it is
    if turn % 2 == 0:
        player_turn_label.config(text=f"{p1name.get()}'s Turn")
    else:
        player_turn_label.config(text=f"{p2name.get()}'s Turn")

# Function to check the player's guess
def check_guess():
    global pp1, pp2, turn

    guess = guess_entry.get()
    if guess == samesymbol:
        if turn % 2 == 0:  # Player 1's turn
            pp1 += 1
            messagebox.showinfo("Result", f"Correct! {p1name.get()} spotted the right symbol.")
        else:  # Player 2's turn
            pp2 += 1
            messagebox.showinfo("Result", f"Correct! {p2name.get()} spotted the right symbol.")
    else:
        messagebox.showinfo("Result", f"Wrong! The correct symbol was {samesymbol}.")

    # Update scores
    score1_label.config(text=f"{p1name.get()}'s Score: {pp1}")
    score2_label.config(text=f"{p2name.get()}'s Score: {pp2}")

    # Move to the next turn
    turn += 1
    if turn >= MAX_TURNS:
        end_game()
    else:
        create_cards()  # Restart the game with new cards
        guess_entry.delete(0, tk.END)  # Clear the input field for the next round

# Function to end the game and declare the winner
def end_game():
    if pp1 > pp2:
        winner = p1name.get()
    elif pp2 > pp1:
        winner = p2name.get()
    else:
        winner = "It's a Draw"

    messagebox.showinfo("Game Over", f"Game over! The winner is: {winner}\n\nFinal Scores:\n{p1name.get()}: {pp1}\n{p2name.get()}: {pp2}")
    root.quit()  # Close the game window

# Initialize tkinter window
root = tk.Tk()
root.title("Dobble Game")
root.geometry("500x600")

# Load the new background image
bg_image = Image.open("new_background.jpg")  # Replace with your new image path
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label for the background
background_label = tk.Label(root, image=bg_photo)
background_label.place(relwidth=1, relheight=1)  # Make the label fill the window

# Game name in bold white color
game_name_label = tk.Label(root, text="DOBBLE GAME", font=("Helvetica", 24, "bold"), fg="black", bg="white")
game_name_label.pack(pady=20)

# Instructions label
instructions_label = tk.Label(root, text="Instructions:\n"
                                          "1. Two cards will be displayed.\n"
                                          "2. Spot the similar symbol between the two cards.\n"
                                          "3. Players take turns guessing.\n"
                                          "4. Each correct guess scores a point.\n"
                                          "5. The player with the most points after 10 turns wins!", 
                              font=("Helvetica", 12), justify="left", bg="white", fg="black")
instructions_label.pack(pady=10)

# Player names
p1name = tk.StringVar()
p2name = tk.StringVar()

# Player name entry labels and fields
tk.Label(root, text="Player 1 Name:", font=("Helvetica", 12), bg="white", fg="black").pack(pady=5)
tk.Entry(root, textvariable=p1name, font=("Helvetica", 12)).pack(pady=5)

tk.Label(root, text="Player 2 Name:", font=("Helvetica", 12), bg="white", fg="black").pack(pady=5)
tk.Entry(root, textvariable=p2name, font=("Helvetica", 12)).pack(pady=5)

# Button to start the game
start_button = tk.Button(root, text="Start Game", font=("Helvetica", 12), command=create_cards)
start_button.pack(pady=10)

# Labels to display the two cards
card1_label = tk.Label(root, text="", font=("Helvetica", 16), bg="white", fg="black")
card1_label.pack(pady=10)

card2_label = tk.Label(root, text="", font=("Helvetica", 16), bg="white", fg="black")
card2_label.pack(pady=10)

# Entry for the player's guess
guess_label = tk.Label(root, text="Your Guess:", font=("Helvetica", 12), bg="white", fg="black")
guess_label.pack(pady=10)
guess_entry = tk.Entry(root, font=("Helvetica", 14))
guess_entry.pack(pady=5)

# Button to submit the guess
submit_button = tk.Button(root, text="Submit Guess", font=("Helvetica", 12), command=check_guess)
submit_button.pack(pady=10)

# Score labels
score1_label = tk.Label(root, text="Player 1 Score: 0", font=("Helvetica", 12), bg="white", fg="black")
score1_label.pack(pady=5)

score2_label = tk.Label(root, text="Player 2 Score: 0", font=("Helvetica", 12), bg="white", fg="black")
score2_label.pack(pady=5)

# Label to show whose turn it is
player_turn_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white", fg="black")
player_turn_label.pack(pady=10)

# Start the tkinter loop
root.mainloop()

