from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

# tim.colormode(255)
colors = ["deep sky blue", "lawn green", "dark orange"]
def randomcolours():
    tim.color(random.choice(colors))
    # r = random.randint(0, 255)
    # g = random.randint(0, 255)
    # b = random.randint(0, 255)
    # random_color = (r, g, b)
    # return random_color

def move_forwards():
    tim.forward(10)
    
def move_backwards():
    tim.backward(10)
    
def move_right():
    tim.right(90)
    
def move_left():
    tim.left(90)
    
def clear_screen():
    tim.reset()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="c", fun=clear_screen)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="space", fun=randomcolours)
screen.exitonclick()
