import random
import os
import time

game = True


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


row1 = ["❔","❔","❔"]
row2 = ["❔","❔","❔"]
row3 = ["❔","❔","❔"]

choices = ["11","12","13","21","22","23","31","32","33"]

grid = [row1,row2,row3]


def show():
  print('      '.join(row1))
  print('      '.join(row2))
  print('      '.join(row3))


bomb = random.choice(choices)
guess = 8

while game == True:
  cls()
  show()
  if guess == 0:
    cls()
    show()
    print("Win")
    game = False
  else:
    choice =input("choose a tile to reveal input in form of row and column: ")
    if choice in choices:
      if choice == bomb:
        row = int(bomb[0])
        column = int(bomb[1])
        grid[row-1][column-1] = "💣"
        cls()
        show()
        print("Lose")
        game = False
      else:
        row = int(choice[0])
        column = int(choice[1]) 
        grid[row - 1][column - 1] = "x"
        guess -= 1
    else:
      print("please choose correct row and column")
      time.sleep(3)
