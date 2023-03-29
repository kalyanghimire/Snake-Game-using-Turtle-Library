from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,270)
        self.write(f'Score: {self.score}',align = "center", font=("Arial",20,"normal"))
        
    def change_score(self):
        self.clear()
        self.score +=1
        self.write(f'Score: {self.score}',align = "center", font=("Arial",20,"normal"))
        
    def lost(self):
        self.goto(0,0)
        self.write(f'Game Over',align = "center", font=("Arial",20,"normal"))
        