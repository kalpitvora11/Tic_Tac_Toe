from tkinter import *
import tkinter.messagebox as msg

# ------------------ BASIC INFO ------------------
print("HELLO EVERYONE")
print("My Name is Kalpit vora")
print("PROJECT : TIC TAC TOE")

playerX_name = input("Enter Player X Name: ")
playerO_name = input("Enter Player O Name: ")

# ------------------ WINDOW ------------------
window = Tk()
window.title("TIC TAC TOE")
window.geometry("600x500")
window.config(bg="Cadet Blue")

# ------------------ VARIABLES ------------------
current_player = "X"
buttons = []
playerX_score = IntVar(value=0)
playerO_score = IntVar(value=0)

# ------------------ FUNCTIONS ------------------
def check_winner():
    win_positions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]

    for a,b,c in win_positions:
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != " ":
            buttons[a].config(bg="yellow")
            buttons[b].config(bg="yellow")
            buttons[c].config(bg="yellow")
            return buttons[a]["text"]
    return None


def button_click(index):
    global current_player

    if buttons[index]["text"] == " ":
        buttons[index]["text"] = current_player

        winner = check_winner()
        if winner:
            if winner == "X":
                playerX_score.set(playerX_score.get() + 1)
                msg.showinfo("Winner", f"{playerX_name} wins!")
            else:
                playerO_score.set(playerO_score.get() + 1)
                msg.showinfo("Winner", f"{playerO_name} wins!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"


def reset_board():
    global current_player
    current_player = "X"
    for btn in buttons:
        btn.config(text=" ", bg="gainsboro")


def new_game():
    playerX_score.set(0)
    playerO_score.set(0)
    reset_board()


def quit_game():
    window.destroy()

# ------------------ UI ------------------
Label(window, text="TIC TAC TOE", font=("Arial", 30, "bold"),
      bg="Cadet Blue", fg="white").pack(pady=10)

score_frame = Frame(window, bg="Cadet Blue")
score_frame.pack()

Label(score_frame, text=f"Player X: {playerX_name}",
      font=("Arial", 12), bg="Cadet Blue").grid(row=0, column=0)
Entry(score_frame, textvariable=playerX_score, width=5).grid(row=0, column=1)

Label(score_frame, text=f"Player O: {playerO_name}",
      font=("Arial", 12), bg="Cadet Blue").grid(row=1, column=0)
Entry(score_frame, textvariable=playerO_score, width=5).grid(row=1, column=1)

board = Frame(window)
board.pack(pady=20)

# ------------------ GAME BUTTONS ------------------
for i in range(9):
    btn = Button(
        board, text=" ", font=("Arial", 20, "bold"),
        width=5, height=2, bg="gainsboro",
        command=lambda i=i: button_click(i)
    )
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# ------------------ CONTROL BUTTONS ------------------
control = Frame(window, bg="Cadet Blue")
control.pack(pady=10)

Button(control, text="RESET ROUND", width=15, command=reset_board).grid(row=0, column=0, padx=5)
Button(control, text="NEW GAME", width=15, command=new_game).grid(row=0, column=1, padx=5)
Button(control, text="QUIT", width=15, command=quit_game).grid(row=0, column=2, padx=5)

# ------------------ START ------------------
msg.showinfo("Game Info", "Game starts with Player X")
window.mainloop()
