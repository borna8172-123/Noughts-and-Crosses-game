import os


try:
    import tkinter as tk
except ModuleNotFoundError:
    answer = input("sorry the modules are not installed, would you like to install them? (y/n)")
    if answer.lower() == "y":
        os.system("pip install tkinter")
    else:
        print("exiting...")
        exit()


Board = []
window = tk.Tk()
window.title("bornas noughts and crosses game")

class Player:

    def __init__(self, name, symbol,xp):
        self.name = name
        self.symbol = symbol
        self.xp = xp

player1 = Player("Player 1", "X", 0)
player2 = Player("Player 2", "O", 0)
HasWon = False
current_player = player1

title_label = tk.Label(window, text=f"Player turn: {current_player.name} symbol: {current_player.symbol} xp: {current_player.xp}", font=("Arial", 10))

def title():
    global title_label
    print(f"Player turn: {current_player.name} symbol: {current_player.symbol} xp: {current_player.xp}")
    title_label = tk.Label(window, text=f"Player turn: {current_player.name} symbol: {current_player.symbol} xp: {current_player.xp}", font=("Arial", 10))
    title_label.grid(row=3, column=0, columnspan=3)


def checkwinner():
    for row in range(3):
        if Board[row][0]["text"] == Board[row][1]["text"] == Board[row][2]["text"] != "":
            return True
    for column in range(3):
        if Board[0][column]["text"] == Board[1][column]["text"] == Board[2][column]["text"] != "":
            return True
    if Board[0][0]["text"] == Board[1][1]["text"] == Board[2][2]["text"] != "":
        return True
    if Board[0][2]["text"] == Board[1][1]["text"] == Board[2][0]["text"] != "":
        return True
    return False

def reset():
    for row in range(3):
        for column in range(3):
            Board[row][column].config(text="")


def givexp():
    global title_label
    if HasWon == True:
        
        if current_player == player1:
            player1.xp += 10
        else:
            player2.xp += 10
    print(f"{current_player.name} won and has {current_player.xp} xp")
    title_label.config(text=f" {current_player.name} won and  has {current_player.xp} xp")
    reset()

def clicked(row,column):
    global current_player,HasWon
    title()
    if Board[row][column]["text"] == "":
       Board[row][column].config(text=current_player.symbol)
       winner = checkwinner()
       if winner == True:
         
         HasWon = True
         givexp()
         reset()



       if current_player == player1:
        current_player = player2
       else:
         current_player = player1






def maingrid():
  for row in range(3):
      Board.append([])
      for column in range(3):

       button= tk.Button(
            
       window,width =5,height=2,font=("Arial", 30),command=lambda r=row, c=column: clicked(r, c)
            )

     

       button.grid(row=row,column=column)
       Board[row].append(button)
   




maingrid()
title()
window.mainloop()
