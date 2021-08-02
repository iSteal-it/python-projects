choice = int(input("Which number you think will come in die roll?"))
num = random.randint(1,6)

if num == choice:
  print("you won")
else:
  print("you lose")
