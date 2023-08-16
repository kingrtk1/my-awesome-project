import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class GuessTheNumberGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")

        self.pages = [StartPage(root, self), GamePage(root)]
        self.current_page = 0
        self.show_current_page()

    def show_current_page(self):
        self.pages[self.current_page].frame.pack()

    def next_page(self):
        self.pages[self.current_page].frame.pack_forget()
        self.current_page += 1
        self.show_current_page()

class StartPage:
    def __init__(self, root, gui):
        self.root = root
        self.gui = gui

        self.frame = tk.Frame(root)

        self.start_label = tk.Label(self.frame, text="Welcome to Guess the Number!", font=("Helvetica", 16))
        self.start_label.pack(pady=20)

        self.start_button = tk.Button(self.frame, text="Start Game", font=("Helvetica", 14), command=self.start_game)
        self.start_button.pack()

    def start_game(self):
        self.gui.next_page()

class GamePage:
    def __init__(self, root):
        self.root = root

        self.frame = tk.Frame(root)

        self.min_label = tk.Label(self.frame, text="Enter the minimum range:", font=("Helvetica", 12))
        self.min_label.pack(pady=10)

        self.min_entry = tk.Entry(self.frame, font=("Helvetica", 12), width=20)
        self.min_entry.pack()

        self.max_label = tk.Label(self.frame, text="Enter the maximum range:", font=("Helvetica", 12))
        self.max_label.pack(pady=10)

        self.max_entry = tk.Entry(self.frame, font=("Helvetica", 12), width=20)
        self.max_entry.pack()

        self.start_button = tk.Button(self.frame, text="Start Game", font=("Helvetica", 12), command=self.start_game)
        self.start_button.pack(pady=20)

    def start_game(self):
        min_range = int(self.min_entry.get())
        max_range = int(self.max_entry.get())

        secret_number = random.randint(min_range, max_range)

        guess = simpledialog.askinteger("Guess the Number", f"I'm thinking of a number between {min_range} and {max_range}. Take a guess:")

        attempts = 1

        while guess != secret_number:
            if guess < secret_number:
                guess = simpledialog.askinteger("Guess the Number", "Too low! Take another guess:")
            else:
                guess = simpledialog.askinteger("Guess the Number", "Too high! Take another guess:")

            attempts += 1

        messagebox.showinfo("Congratulations", f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        self.root.next_page()

if __name__ == "__main__":
    root = tk.Tk()
    app = GuessTheNumberGUI(root)
    root.mainloop()
