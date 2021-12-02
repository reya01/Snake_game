from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super(Food, self).__init__()  # writing food as a subclass of turtle so all turtle methods can be used
        xcord2 = randint(-20, 20) * 20  # multiplying by 20 to get a round number in increments of 20
        ycord2 = randint(-20, 20) * 20
        self.shape("square")
        self.penup()
        self.color("pink")
        self.goto(xcord2, ycord2)

    def move_rand(self):
        xcord2 = randint(-20, 20) * 20  # multiplying by 20 to get a round number in increments of 20
        ycord2 = randint(-20, 20) * 20
        self.goto(xcord2, ycord2)
