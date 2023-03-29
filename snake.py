from turtle import Screen, Turtle
screen = Screen()
import random
import time
up = 90
down = 270
left = 180
right = 0
starting_positions = [(0,0),(-20,0),(-40,0)]
class snake:
    
    
    def __init__(self):
        self.starting_positions = starting_positions
        self.segments = []
        self.screen()
        self.starting_pos()
        self.head = self.segments[0]
    
    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        screen.update()    
        
    def add_segment_new(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
       
        screen.update()   
        
    def extend(self):
        self.add_segment_new(self.segments[-1].position())

    
    def tracer(self):
        screen.tracer(0)
    
    def starting_pos(self):
        for position in self.starting_positions:
            self.add_segment(position)
            
            
    def update(self):
        screen.update()
        time.sleep(0.1)
    
    def go_forward(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            self.segments[seg_num].goto(self.segments[seg_num-1].xcor(),self.segments[seg_num-1].ycor())
        self.segments[0].forward(20)

    def screen(self):

        screen.setup(width = 600, height = 600)
        screen.title("Snake Game")
        screen.bgcolor("black") 
    
    def screen_click(self):
        screen.exitonclick()
        
    def detect_key(self):
        screen.onkey(key = "Up",fun=self.move_up)
        screen.onkey(key = "Left",fun=self.rotate_left)
        screen.onkey(key = "Right",fun=self.rotate_right)
        screen.onkey(key = "Down",fun=self.move_back)
    def move_up(self):
        if self.segments[0].heading()!= down:
            self.segments[0].setheading(90)

    def move_back(self):
        if self.segments[0].heading()!= up:
            self.segments[0].setheading(270)

    
    def rotate_left(self):
        if self.segments[0].heading()!= right:
            self.segments[0].setheading(180)

    def rotate_right(self):
        if self.segments[0].heading()!= left:
            self.segments[0].setheading(0)
    
    def detect_wall(self):
        x = self.segments[0].pos()[0]
        y = self.segments[0].pos()[1]
        if x == 300 or x == -300:
            self.segments[0].goto(-x,y)
        elif y == 300 or y == -300:
            self.segments[0].goto(x,-y)

    def check_collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment)<10:
                return(0)
                