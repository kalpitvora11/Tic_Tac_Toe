"""
Tic Tac Toe Game Module.

This module implements a standard Tic Tac Toe game using Python's Tkinter library.
It features a GUI with score tracking for two players.
"""

import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    """
    Main game class that handles the GUI and game logic.
    """

    def __init__(self, root_window, p1_name, p2_name):
        """
        Initialize the game window and variables.

        Args:
            root_window: The main Tkinter window.
            p1_name (str): Name of Player X.
            p2_name (str): Name of Player O.
        """
        self.root = root_window
        self.root.title("TIC TAC TOE")
        self.root.geometry("600x550")
        self.root.config(bg="Cadet Blue")

        # Game Variables
        self.p1_name = p1_name
        self.p2_name = p2_name
        self.current_player = "X"
        self.buttons = []
        self.player_x_score = tk.IntVar(value=0)
        self.player_o_score = tk.IntVar(value=0)

        # Build UI
        self.create_widgets()
        
        # Start Message
        messagebox.showinfo("Game Info", "Game starts with Player X")

    def create_widgets(self):
        """Create all the labels, frames, and buttons for the GUI."""
        # Title
        tk.Label(self.root, text="TIC TAC TOE", font=("Arial", 30, "bold"),
                 bg="Cadet Blue", fg="white").pack(pady=10)

        # Score Section
        score_frame = tk.Frame(self.root, bg="Cadet Blue")
        score_frame.pack()

        tk.Label(score_frame, text=f"Player X: {self.p1_name}",
                 font=("Arial", 12), bg="Cadet Blue").grid(row=0, column=0)
        tk.Entry(score_frame, textvariable=self.player_x_score, width=5).grid(row=0, column=1)

        tk.Label(score_frame, text=f"Player O: {self.p2_name}",
                 font=("Arial", 12), bg="Cadet Blue").grid(row=1, column=0)
        tk.Entry(score_frame, textvariable=self.player_o_score, width=5).grid(row=1, column=1)

        # Game Board Area
        board_frame = tk.Frame(self.root)
        board_frame.pack(pady=20)

        # Create 9 Buttons
        for i in range(9):
            btn = tk.Button(
                board_frame, text=" ", font=("Arial", 20, "bold"),
                width=5, height=2, bg="gainsboro",
                command=lambda index=i: self.on_button_click(index)
            )
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)

        # Control Buttons
        control_frame = tk.Frame(self.root, bg="Cadet Blue")
        control_frame.pack(pady=10)

        tk.Button(control_frame, text="RESET ROUND", width=15,
                  command=self.reset_board).grid(row=0, column=0, padx=5)
        tk.Button(control_frame, text="NEW GAME", width=15,
                  command=self.new_game).grid(row=0, column=1, padx=5)
        tk.Button(control_frame, text="QUIT", width=15,
                  command=self.root.destroy).grid(row=0, column=2, padx=5)

    def check_winner(self):
        """
        Check the board for a winning combination.
        Returns 'X', 'O', or None.
        """
        win_positions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]

        for a, b, c in win_positions:
            btn_a = self.buttons[a]
            btn_b = self.buttons[b]
            btn_c = self.buttons[c]

            if btn_a["text"] == btn_b["text"] == btn_c["text"] != " ":
                btn_a.config(bg="yellow")
                btn_b.config(bg="yellow")
                btn_c.config(bg="yellow")
                return btn_a["text"]
        return None

    def on_button_click(self, index):
        """
        Handle a click on the game board.

        Args:
            index (int): The index (0-8) of the button clicked.
        """
        if self.buttons[index]["text"] == " ":
            self.buttons[index]["text"] = self.current_player

            winner = self.check_winner()
            if winner:
                if winner == "X":
                    current_score = self.player_x_score.get()
                    self.player_x_score.set(current_score + 1)
                    messagebox.showinfo("Winner", f"{self.p1_name} wins!")
                else:
                    current_score = self.player_o_score.get()
                    self.player_o_score.set(current_score + 1)
                    messagebox.showinfo("Winner", f"{self.p2_name} wins!")
                self.reset_board()
            elif " " not in [btn["text"] for btn in self.buttons]:
                messagebox.showinfo("Draw", "It's a Tie!")
                self.reset_board()
            else:
                # Switch Player
                self.current_player = "O" if self.current_player == "X" else "X"

    def reset_board(self):
        """Clear the board for a new round but keep scores."""
        self.current_player = "X"
        for btn in self.buttons:
            btn.config(text=" ", bg="gainsboro")

    def new_game(self):
        """Reset scores and the board for a completely new game."""
        self.player_x_score.set(0)
        self.player_o_score.set(0)
        self.reset_board()


if __name__ == "__main__":
    # Console Inputs
    print("------------------ BASIC INFO ------------------")
    print("HELLO EVERYONE")
    print("PROJECT : TIC TAC TOE")
    
    # Using 'input' inside the main block ensures it runs only when executed directly
    name_x = input("Enter Player X Name: ")
    name_o = input("Enter Player O Name: ")

    # Window Setup
    root = tk.Tk()
    app = TicTacToe(root, name_x, name_o)
    root.mainloop()
