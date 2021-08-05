import os
import time


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


game_is_on = True
player1_win = False
player2_win = False

choices = ["11","12","13","21","22","23","31","32","33"]

winning_pattern = {
  "row1":["11","12","13"],
  "row2":["21","22","23"],
  "row3":["31","32","33"],
  "col1":["11","21","31"],
  "col2":["12","22","32"],
  "col3":["13","23","33"],
  "dia1":["11","22","33"],
  "dia2":["13","22","31"]
  }

 
def game():
  global game_is_on
  global player1_win
  global player2_win
  global time

  row1 = ["◻️","◻️","◻️"]
  row2 = ["◻️","◻️","◻️"]
  row3 = ["◻️","◻️","◻️"]
  
  grid = [row1,row2,row3]


  def show():
    print((' _|_ '.join(row1)))
    print((' _|_ '.join(row2)))
    print(('  |  '.join(row3)))


  count = 0
  already_taken_tile =[]
  player1_tile =[]
  player2_tile = []
  while game_is_on == True:
    if count == 9:
      cls()
      show()
      print("draw")
      replay = input("you wanted to replay or end game? ").lower()
      if replay == "replay":
        game()
      elif replay == "end":
        game_is_on = False
        print(player1_tile)
      else:
        print("please choose correct input")
        time.sleep(3)
    else:
      cls()
      show()
      if count % 2 == 0:
        player1_choice = input("Player1:select row and column where you wanted to add your mark: ")
        if player1_choice in choices:
          if player1_choice in already_taken_tile:
            print("please choose an empty tile")
            time.sleep(3)
          else:
            grid[int(player1_choice[0])-1][int(player1_choice[1])-1] = "✔️"
            count+=1
            already_taken_tile.append(player1_choice)
            player1_tile.append(player1_choice)
            for pattern in winning_pattern:
              win = 0
              for position in winning_pattern[pattern]:
                print(position)
                if position in player1_tile:
                  win+=1
                if win == 3:
                  cls()
                  show()
                  print("player1 win")
                  game_is_on == False
                  exit()
        else:
          print("please enter correct value row and column")
          time.sleep(3)
      else:
        player2_choice = input("Player2:select row and column where you wanted to add your mark: ")
        if player2_choice in choices:
          if player2_choice in already_taken_tile:
            print("please choose an empty tile")
            time.sleep(3)
          else:
            grid[int(player2_choice[0])-1][int(player2_choice[1])-1] = "🎚️"
            count+=1
            already_taken_tile.append(player2_choice)
            player2_tile.append(player2_choice)
            for pattern in winning_pattern:
              win = 0
              for position in winning_pattern[pattern]:
                print(position)
                if position in player2_tile:
                  win+=1
                if win == 3:
                  cls()
                  show()
                  print("player2 win")
                  game_is_on == False
                  exit()
        else:
          print("please enter correct value of row and column")
          time.sleep(3)

game()
