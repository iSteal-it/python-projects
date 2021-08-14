import tkinter

operator = ""
num1 = ""
num2 = ""


def clear():
    number_1.delete(0, tkinter.END)
    number_2.delete(0, tkinter.END)
    answer.configure(text="")

def addition():
    global operator
    operator = "add"


def subtract():
    global operator
    operator = "sub"


def multiply():
    global operator
    operator = "mul"


def divide():
    global operator
    operator = "div"


def add(num1, num2):
    return (num1 + num2)


def sub(num1, num2):
    return (num1 - num2)


def mul(num1, num2):
    return (num1 * num2)


def div(num1, num2):
    return (num1 / num2)


def cal():
    global operator
    if operator == "add":
        result = (add(int(number_1.get()), int(number_2.get())))
    if operator == "sub":
        result = (sub(int(number_1.get()), int(number_2.get())))
    if operator == "mul":
        result = (mul(int(number_1.get()), int(number_2.get())))
    if operator == "div":
        result = (div(int(number_1.get()), int(number_2.get())))
    answer.configure(text=result)


window = tkinter.Tk()
window.title("calculator")
window.geometry("180x180")
window.configure(padx=20, pady=20)

number_1 = tkinter.Entry(width=14, justify="right")
number_1.grid(column=0, row=0, columnspan=2)
number_1.focus()

add_button = tkinter.Button(width=7)
add_button.configure(text="add", command=addition)
add_button.grid(row=1, column=0)

subtract_button = tkinter.Button(width=7)
subtract_button.configure(text="subtract", command=subtract)
subtract_button.grid(row=1, column=1)

multiplay_button = tkinter.Button(width=7)
multiplay_button.configure(text="multiply", command=multiply)
multiplay_button.grid(row=2, column=0)

divide_button = tkinter.Button(width=7)
divide_button.configure(text="divide", command=divide)
divide_button.grid(row=2, column=1)

number_2 = tkinter.Entry(width=14, justify="right")
number_2.grid(column=0, row=3, columnspan=2)

calculate = tkinter.Button(width=7)
calculate.configure(text="calculate", command=cal)
calculate.grid(row=4, column=0)

reset = tkinter.Button(width=7)
reset.configure(text="reset", command=clear)
reset.grid(row=4, column=1)

answer = tkinter.Label(width=14)
answer.configure(text="")
answer.grid(column=0, row=5, columnspan=2)

window.mainloop()
