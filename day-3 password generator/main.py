import random
import string_utils
#install python_string_utils
letters_low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters_up =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = ""
password_real = ""

def random_gen(char,list):
  global password
  for x in range(char):
    character = random.choice(list)
    password = password + character

upper_case = int(input("how many upper case character you want? type 0 for none: "))
lower_case = int(input("how many lower case character you want? type 0 for none: "))
numbersq = int(input("how many numbers you want? type 0 for none: "))
symbolsq = int(input("how many symbols you want? type 0 for none: "))

if upper_case != 0:
  random_gen(upper_case,letters_up)

if lower_case != 0:
  random_gen(lower_case,letters_low)

if numbersq != 0:
  random_gen(numbersq,numbers)

if symbolsq != 0:
  random_gen(symbolsq,symbols)

print(string_utils.shuffle(password))
