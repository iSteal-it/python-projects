import ascii
import board
import os
import computerai
import random


p_win = 0
c_win = 0

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

computerAI = computerai.Computer_AI()
computer_ship= random.sample(computerAI.possible_positions,5)

game = True
ships = ["⚔️","⚔️","⚔️","⚔️","⚔️"]
count = 0

player_ship = []

player_board = board.Board()
computer_board = board.Board()

for ship in ships:
  player_board.show_board()
  co_ordinate = input("please give co ordinates of box where you wanted to place your ship: ")
  player_board.grid[int(co_ordinate[0])-1][int(co_ordinate[1])-1] = "⚔️"
  player_ship.append(co_ordinate)
  cls()

print(player_ship)
def player():
   global p_win
   player_choice = input("give us co_ordinates to attack: ")
   if player_choice in computer_ship:
     cls()
     computer_board.grid[int(player_choice[0])-1][int(player_choice[1])-1] = "🪦"
     computer_board.show_board()
     print(ascii.VS)
     player_board.show_board()
     p_win  +=1
     player()
   else:
     computer_board.grid[int(player_choice[0])-1][int(player_choice[1])-1] = "✔️"

def c():
  global c_win
  computer_choice = str(random.choice(computerAI.possible_positions))
  if computer_choice in player_ship:
    cls()
    player_board.grid[int(computer_choice[0])-1][int(computer_choice[1])-1] = "🪦"
    computerAI.possible_positions.remove(computer_choice)
    computer_board.show_board()
    print(ascii.VS)
    player_board.show_board()
    c_win += 1
    c()

  else:

    player_board.grid[int(computer_choice[0])-1][int(computer_choice[1])-1] = "✔️"
    computerAI.possible_positions.remove(computer_choice)
while game:
  if p_win == 5 or c_win == 5:
    game=False
    cls()

  computer_board.show_board()
  print(ascii.VS)
  player_board.show_board()
  if count % 2 == 0:
    player()
  else :
    c()
  count += 1
  cls()

if p_win == 5:
  print(ascii.WIN)
else:
  print(ascii.LOSE)
