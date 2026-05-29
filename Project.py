import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe: Player vs Computer")
        self.player = "X" 
        self.computer = "O"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()

    def create_buttons(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", font=('Arial', 36), width=5, height=2,
                                   command=lambda r=row, c=col: self.player_move(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def player_move(self, row, col):
        button = self.buttons[row][col]
        if button["text"] == "":
            button["text"] = self.player
            if self.check_winner(self.player):
                messagebox.showinfo("Game Over", "Congratulations! You have won the game")
                self.reset_game()
                return
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
                return
            self.root.after(500, self.computer_intelligence)

    def computer_intelligence(self):
        b = self.buttons
        if (b[0][0]["text"] == b[1][1]["text"] == self.player and b[2][2]["text"] == ""):
            b[2][2]["text"] = self.computer
            self.checking_result()
        
        elif (b[0][2]["text"] == b[1][1]["text"] == self.player and b[2][0]["text"] == ""):
            b[2][0]["text"] = self.computer
            self.checking_result()

        elif (b[0][0]["text"] == b[0][1]["text"] == self.player and b[0][2]["text"] == ""):
            b[0][2]["text"] = self.computer
            self.checking_result()

        elif (b[0][0]["text"] == b[1][0]["text"] == self.player and b[2][0]["text"] == ""):
            b[2][0]["text"] = self.computer
            self.checking_result()

        elif (b[1][0]["text"] == b[1][1]["text"] == self.player and b[1][2]["text"] == ""):
            b[1][2]["text"] = self.computer
            self.checking_result()

        elif (b[0][1]["text"] == b[1][1]["text"] == self.player and b[2][1]["text"] == ""):
            b[2][1]["text"] = self.computer
            self.checking_result()

        elif (b[2][0]["text"] == b[2][1]["text"] == self.player and b[2][2]["text"] == ""):
            b[2][2]["text"] = self.computer
            self.checking_result()

        elif (b[0][2]["text"] == b[1][2]["text"] == self.player and b[2][2]["text"] == ""):
            b[2][2]["text"] = self.computer
            self.checking_result()

        elif (b[0][0]["text"] == b[0][2]["text"] == self.player and b[0][1]["text"] == ""):
            b[0][1]["text"] = self.computer
            self.checking_result()

        elif (b[0][0]["text"] == b[2][0]["text"] == self.player and b[1][0]["text"] == ""):
            b[1][0]["text"] = self.computer
            self.checking_result()

        elif (b[1][0]["text"] == b[1][2]["text"] == self.player and b[1][1]["text"] == ""):
            b[1][1]["text"] = self.computer
            self.checking_result()

        elif (b[0][1]["text"] == b[2][1]["text"] == self.player and b[1][1]["text"] == ""):
            b[1][1]["text"] = self.computer
            self.checking_result()

        elif (b[2][0]["text"] == b[2][2]["text"] == self.player and b[2][1]["text"] == ""):
            b[2][1]["text"] = self.computer
            self.checking_result()

        elif (b[0][2]["text"] == b[2][2]["text"] == self.player and b[1][2]["text"] == ""):
            b[1][2]["text"] = self.computer
            self.checking_result()

        elif (b[0][2]["text"] == b[0][1]["text"] == self.player and b[0][0]["text"] == ""):
            b[0][0]["text"] = self.computer
            self.checking_result()

        elif (b[2][0]["text"] == b[1][0]["text"] == self.player and b[0][0]["text"] == ""):
            b[0][0]["text"] = self.computer
            self.checking_result()

        elif (b[1][2]["text"] == b[1][1]["text"] == self.player and b[1][0]["text"] == ""):
            b[1][0]["text"] = self.computer
            self.checking_result()

        elif (b[2][1]["text"] == b[1][1]["text"] == self.player and b[0][1]["text"] == ""):
            b[0][1]["text"] = self.computer
            self.checking_result()

        elif (b[2][2]["text"] == b[2][1]["text"] == self.player and b[2][0]["text"] == ""):
            b[2][0]["text"] = self.computer
            self.checking_result()

        elif (b[2][2]["text"] == b[1][2]["text"] == self.player and b[0][2]["text"] == ""):
            b[0][2]["text"] = self.computer
            self.checking_result()

        else:
            self.computer_move()
            self.checking_result()

    def computer_move(self):
        b = self.buttons
        empty_cells = [(r, c) for r in range(3) for c in range(3)
                       if b[r][c]["text"] == ""]
        if not empty_cells:
            return
        row, col = random.choice(empty_cells)
        b[row][col]["text"] = self.computer

    def checking_result(self):
        if self.check_winner(self.computer):
            messagebox.showinfo("Game Over", "Computer wins!,Better Luck next time")
            self.reset_game()
        elif self.is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_game()

    def check_winner(self, symbol):
        b = self.buttons
        for i in range(3):
            if all(b[i][j]["text"] == symbol for j in range(3)):
                return True
            if all(b[j][i]["text"] == symbol for j in range(3)):
                return True
        if b[0][0]["text"] == b[1][1]["text"] == b[2][2]["text"] == symbol:
            return True
        if b[0][2]["text"] == b[1][1]["text"] == b[2][0]["text"] == symbol:
            return True
        return False

    def is_draw(self):
        return all(self.buttons[r][c]["text"] != "" for r in range(3) for c in range(3))

    def reset_game(self):
        for row in self.buttons:
            for button in row:
                button["text"] = ""

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop() 