from turtle import Turtle
import random
class food(Turtle):
    def __init__(self) -> None:

        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.speed("fastest")
        self.new_position()
    
    def new_position(self):
        self.random_x = random.randint(-280,280)
        self.random_y = random.randint(-280,280)      
        self.goto(self.random_x,self.random_y)
    