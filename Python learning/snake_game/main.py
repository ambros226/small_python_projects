from turtle import Turtle,Screen
import time
import random
score = 0
highest_score = 0


screen=Screen()
screen.bgcolor("#7EE62E")
screen.title("Snake game")
screen.setup(600,600)
screen.tracer(False)
body_parts = []

score_sign = Turtle("square")
score_sign.speed(0)
score_sign.color("white")
score_sign.penup()
score_sign.hideturtle()
score_sign.goto(0, 265)
score_sign.write("Skóre: 0  Nejvyšší skóre: 0", align="center", font=("Arial", 18))


squere1=Turtle("square")
squere1.penup()
squere1.goto(0,0)
screen.update()
head_direction="stop"

food=Turtle("square")
food.penup()
food.color("red")

def food_position():
    x=random.randint(-290,290)
    y=random.randint(-290,290)
    food.goto(x,y)

def move_up():
    global head_direction
    if head_direction!="down":
        head_direction="up"
def move_down():
    global head_direction
    if head_direction!="up":
        head_direction="down"
def move_left():
    global head_direction
    if head_direction!="right":
        head_direction= "left"
def move_right():
    global head_direction
    if head_direction!="left":
        head_direction="right"

def move():
    if head_direction== "up":
        y=squere1.ycor()
        squere1.sety(y+20)

    elif head_direction== "down":
        y=squere1.ycor()
        squere1.sety(y-20)
    elif head_direction== "left":
        x=squere1.xcor()
        squere1.setx(x-20)
        
    elif head_direction== "right":
        x=squere1.xcor()
        squere1.setx(x+20)

def dead():
    global head_direction
    time.sleep(2)
    head_direction="stop"
    squere1.goto(0,0)

    for one_body_part in body_parts:
        one_body_part.goto(1500, 1500)

    body_parts.clear()
def vypis_score():
    score_sign.clear()
    score_sign.write(f"Skóre: {score}  Nejvyšší skóre: {highest_score}", align="center", font=("Arial", 18))

screen.listen()
screen.onkeypress(move_up,"w")
screen.onkeypress(move_down,"s")
screen.onkeypress(move_left,"a")
screen.onkeypress(move_right,"d")

food_position()
while True:
    screen.update()

    if squere1.xcor()>290 or squere1.xcor()<-290 or squere1.ycor()>290 or squere1.ycor()<-290:
        dead()        
        score=0
        vypis_score()
        
    for i in body_parts:
        if i.distance(squere1)<20:
        
            dead()

        vypis_score()
         

    if squere1.distance(food)<20:
        food_position()
        new_body_part = Turtle("square")
        new_body_part.speed(0)
        new_body_part.color("grey")
        new_body_part.penup()
        body_parts.append(new_body_part)

        score += 10

        if score > highest_score:
            highest_score = score
       




    for index in range(len(body_parts) - 1, 0, -1):
       x = body_parts[index - 1].xcor()
       y = body_parts[index - 1].ycor()
       body_parts[index].goto(x, y)

    if len(body_parts) > 0:

        x = squere1.xcor()
        y = squere1.ycor()
        body_parts[0].goto(x,y)

    move()
    time.sleep(0.1)
    


screen.exitonclick()
