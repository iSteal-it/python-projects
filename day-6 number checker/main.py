number_to_check = int(input("please enter a number to check: "))


def check(number_to_check):
  factors = []
  for x in range(number_to_check):
    if number_to_check % (x+1) == 0:
      factors.append(x+1)
  print(factors)
  if len(factors) == 2:
    print("number is prime")

check(number_to_check)
