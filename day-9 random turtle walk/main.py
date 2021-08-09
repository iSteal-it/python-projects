import turtle
import random

colours = ["red","green","yellow","blue","green","black","white","pink","orange","violet","brown","grey"]

game = True
tim = turtle.Turtle()
screen = turtle.Screen()
screen.screensize(450,450)
tim.shape("turtle")
tim.pensize(3)
while game:
  tim.color(random.choice(colours))
  count = random.randint(0,11)
  if count % 2 == 0:
    tim.left(45)
  else:
    tim.right(45)
  tim.forward(10) 
screen.exitonclick()
