from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.configure(bg=THEME_COLOR)

        self.score = Label(text="Score: 0", fg="white")
        self.score.configure(bg=THEME_COLOR)
        self.score.grid(row=0, column=1, padx=20, pady=20)

        self.card = Canvas(self.window, height=250, width=300)
        self.card.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.question_text = self.card.create_text(150, 125, width=280, text="some text over here", fill=THEME_COLOR,
                                                   font=("Ariel", 20, "italic"))

        right = PhotoImage(file="images/true.png")
        wrong = PhotoImage(file="images/false.png")

        self.true = Button(image=right, highlightthickness=0, bg=THEME_COLOR,command=self.true_pressed)
        self.true.grid(row=2, column=0, padx=20, pady=20)

        self.false = Button(image=wrong, highlightthickness=0, bg=THEME_COLOR,command=self.false_pressed)
        self.false.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.card.configure(bg="white")
        if self.quiz.still_has_questions():
            self.score.configure(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.card.itemconfig(self.question_text, text=q_text)
        else:
            self.card.itemconfig(self.question_text,text="You have reached end of question")
            self.true.configure(state="disabled")
            self.false.configure(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feed(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feed(is_right)

    def give_feed(self,is_right):
        if is_right:
            self.card.configure(bg="green")
        else:
            self.card.configure(bg="red")
        self.window.after(1000,self.get_next_question)
