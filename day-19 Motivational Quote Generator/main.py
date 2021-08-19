from tkinter import *
import pandas as pd
import random

window = Tk()
window.minsize(width=200, height=200)
window.title("Quotes")

quotess = pd.read_csv("quotes.csv").to_dict(orient="records")
rand = random.choice(quotess)

auth = Label(text=f"By:{rand['AUTHOR']}")
auth.grid(row=0,column=0)

text = Text(height=5, width=30)
text.insert(END, f"{rand['QUOTE']}")
text.grid(row=1,column=0,columnspan=2)
window.mainloop()
