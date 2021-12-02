from turtle import Screen, Turtle
from snake import Snake
import time
from food import Food


def create_scoreboard(turtles2, score):
    turtles2.penup()
    turtles2.hideturtle()
    turtles2.goto(0, 450)
    turtles2.color("red")
    turtles2.write(f"Score is {score}", font=("Verdana", 20, "normal"), align="center")


def add_to_scoreboard(turtles2, score):
    turtles2.clear()
    turtles2.write(f"Score is {score}", font=("Verdana", 20, "normal"), align="center")


def main():
    screen = Screen()
    screen.setup(width=950, height=950)
    screen.bgcolor("black")
    screen.title("My Snake Game-by Squid")
    screen.tracer(0)  # Turn turtle animation on/off and set delay for update drawings.

    snake1 = Snake()  # call initialize snake function and save the list of turtle names
    food1 = Food()
    score1 = 0
    scoreboard1 = Turtle()
    create_scoreboard(scoreboard1, score1)

    screen.listen()  # want to "listen" for arrow keys
    screen.onkey(snake1.move_up, "Up")
    screen.onkey(snake1.move_down, "Down")
    screen.onkey(snake1.move_left, "Left")
    screen.onkey(snake1.move_right, "Right")

    game_on = True
    while game_on:
        screen.update()  # signals screen to update since with tracer set to zero it wont on its own
        time.sleep(0.1)  # set a delay here by amount in sleep function call
        snake1.move_forward()

        if food1.distance(snake1.turt_list[0]) <= 15:  # detect a collision between snake and food
            score1 += 1
            print(F"Collision! +1 to your score. Score is now: {score1}")
            food1.move_rand()
            snake1.add_snake()
            add_to_scoreboard(scoreboard1, score1)
        if snake1.turt_list[0].xcor() > 500 or snake1.turt_list[0].xcor() < -500 or snake1.turt_list[0].ycor() > 500 or snake1.turt_list[0].ycor() < -500:
            game_on = False
            print("You hit a wall, game over")
        for i in range(1, len(snake1.turt_list) - 1):  # see if snake hits any turtle in snake except first one
            if snake1.turt_list[0].distance(snake1.turt_list[i]) <= 15:
                game_on = False
                print("You hit the snake, game over")

    print(f"Your final score is {score1}")
    screen.exitonclick()


main()
