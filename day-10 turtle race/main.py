import turtle
import random
game = True

colors = ["green","red","blue","yellow","violet","pink","cyan","brown","orange","peach puff"]
turtles = []
screen = turtle.Screen()
screen.screensize(450,450)
screen.title("turtle race")
tim = turtle.Turtle()
tim.shape("turtle")
tim.penup()
tim.goto(300,-300)
tim.pendown()
tim.pencolor("black")
tim.pensize(4)
tim.goto(300,300)
tim.right(90)
tim.color("grey")

print(colors)
choice = input("choose color of turtle you think will win from list above: ")
for x in range(10):
    turt = turtle.Turtle()
    turt.penup()
    turt.color(colors[x])
    turt.shape("turtle")
    turt.goto(-300,-200 + 40 * x)
    turtles.append(turt)

while game:
    for tur in turtles:
        tur.forward(random.randint(1,6))
        if tur.xcor() > 283:
            game = False
            winner = tur

if winner == choice:
    print("win")
else:
    print("loss")
screen.exitonclick()
