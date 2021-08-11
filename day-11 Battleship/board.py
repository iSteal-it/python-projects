
class Board:
    def __init__(self):
        self.row1 = ["◻️","◻️","◻️","◻️","◻️"]
        self.row2 = ["◻️","◻️","◻️","◻️","◻️"]
        self.row3 = ["◻️","◻️","◻️","◻️","◻️"]
        self.row4 = ["◻️","◻️","◻️","◻️","◻️"]
        self.row5 = ["◻️","◻️","◻️","◻️","◻️"]
        self.grid = [self.row1,self.row2,self.row3,self.row4,self.row5]

    def show_board(self):
        print((' _|_ '.join(self.row1)))
        print((' _|_ '.join(self.row2)))
        print((' _|_ '.join(self.row3)))
        print((' _|_ '.join(self.row4)))
        print((' _|_ '.join(self.row5)))
        return ""
