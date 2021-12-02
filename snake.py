from turtle import Turtle


class Snake:
    def __init__(self):
        self.length = 3
        self.turt_list = []  # list of names of turtles
        xcord1 = 0
        ycord1 = 0
        for i in range(1, 4):
            turt_name = "turtle" + str(i)
            turt_name = Turtle()
            turt_name.shape("square")
            turt_name.penup()
            turt_name.color("white")
            turt_name.goto(xcord1, ycord1)
            xcord1 -= 20
            self.turt_list.append(turt_name)

    def move_forward(self):  # move snake forward in a shuffle fashion that will work regardless of direction
        for turt_num in range(len(self.turt_list) - 1, 0, -1):
            new_x = self.turt_list[turt_num - 1].xcor()
            new_y = self.turt_list[turt_num - 1].ycor()
            self.turt_list[turt_num].goto(new_x, new_y)
        self.turt_list[0].forward(20)

    def add_snake(self):   # add a section to the snake based on the position and direction of last turtle
        heading1 = self.turt_list[-1].heading()
        xcord_b = self.turt_list[-1].xcor()
        ycord_b =self.turt_list[-1].ycor()
        turt_name_b = "turtle" + str(len(self.turt_list))
        turt_name_b = Turtle()
        self.turt_list.append(turt_name_b)

        if heading1 == 0:
            turt_name_b.shape("square")
            turt_name_b.penup()
            turt_name_b.color("white")
            turt_name_b.goto(xcord_b-20, ycord_b)

        elif heading1 == 90:
            turt_name_b.shape("square")
            turt_name_b.penup()
            turt_name_b.color("white")
            turt_name_b.goto(xcord_b, ycord_b-20)

        elif heading1 == 180:
            turt_name_b.shape("square")
            turt_name_b.penup()
            turt_name_b.color("white")
            turt_name_b.goto(xcord_b+20, ycord_b)

        elif heading1 == 270:
            turt_name_b.shape("square")
            turt_name_b.penup()
            turt_name_b.color("white")
            turt_name_b.goto(xcord_b, ycord_b+20)


    def move_left(self):
        if self.turt_list[0].heading() == 0:  # dont want to let snake go in opposite direction, would cross itself
            pass
        else:
            self.turt_list[0].setheading(180)

    def move_right(self):
        if self.turt_list[0].heading() == 180:  # dont want to let snake go in opposite direction, would cross itself
            pass
        else:
            self.turt_list[0].setheading(0)

    def move_up(self):
        if self.turt_list[0].heading() == 270:  # dont want to let snake go in opposite direction, would cross itself
            pass
        else:
            self.turt_list[0].setheading(90)

    def move_down(self):
        if self.turt_list[0].heading() == 90:  # dont want to let snake go in opposite direction, would cross itself
            pass
        else:
            self.turt_list[0].setheading(270)
