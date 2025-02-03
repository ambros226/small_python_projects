from turtle import *
import random
import time
from copy import deepcopy
global points
points=0
ground_list=[]
alive=True
timer=False
tube_list_move=[]
point_tube_list=[]
#screen settings
screen=Screen()
screen.bgcolor("#A1E3F9")
screen.title("Flappy bird")
screen.setup(width=600, height=600)
screen.tracer(False)
#

#flapy bird character
flappy_bird=Turtle("square")
flappy_bird.color("yellow")
flappy_bird.shapesize(stretch_wid=2,stretch_len=2)
flappy_bird.penup()
flappy_bird.goto(-140,0)

#
#ground and top
for i in range (2):
    ground=Turtle("square")
    ground.color("#CBA35C")
    ground.shapesize(stretch_wid=5,stretch_len=30)
    ground.penup()
    if i>0:
        ground.goto(0,-250)
    else:
        ground.goto(0,250)
    ground.stamp()
    ground.hideturtle()
    ground_list.append(ground)
#
    
#point sign
points_print = Turtle("square")
points_print.color("white")
points_print.penup()
points_print.hideturtle()
points_print.goto(0,265)

def print_points_def():
    points_print.clear()
    points_print.write(f"Points: {int(points)}", align="center", font=("Arial", 30,"bold"))

print_points_def()
#  
#tubes
def tubes_spawning_set(start_timer):
    global timer
    end_timer=time.time()
    if end_timer-start_timer>=4:
        timer=False
        tubes_spawning()

def tubes_spawning():
    global tube
    tube=Turtle("square")
    tube.color("#3E7B27")
    tube.penup()

    tube.kind=random.randint(1,3)
    if tube.kind==1:
        tube.kind=1
        size=random.randint(160,320)
        tube.shapesize(stretch_wid=size/20,stretch_len=3)
        tube.org_size=size
        tube.goto(300,-200+(size/2))

    elif tube.kind==2:
        tube.kind=2
        size=random.randint(160,320)
        tube.shapesize(stretch_wid=size/20,stretch_len=3)
        tube.org_size=size
        tube.goto(300,200-(size/2))
        
    else:
        for _ in range(2):
            if _ ==0:
                size=random.randint(80,240)
                tube.shapesize(stretch_wid=size/20,stretch_len=3)
                tube.org_size=size
                tube.kind=3
                tube.goto(300,-200+(size/2))
                tube_list_move.append(tube)
                point_tube_list.append(tube)
                  
            else:
                tube=Turtle("square")
                tube.color("#3E7B27")
                tube.penup()
                size=(400-size)-160
                tube.kind=3
                tube.shapesize(stretch_wid=size/20,stretch_len=3)
                tube.org_size=size
                tube.goto(300,200-(size/2))
    print(tube.kind)
    tube_list_move.append(tube)
    point_tube_list.append(tube)
    
#
            
#
#
#death and objecting tubes
def death():
    global tube_list_move,point_tube_list,timer,tube_move_time,alive
    tube_list_move=[]
    point_tube_list=[]
    timer=0
    tube_move_time=0
    flappy_bird.direction="stop"
    alive=False
    points_print.clear()
    points_print.goto(0,50)
    points_print.write(f"GAME OVER\n",align="center", font=("Arial", 30))
    points_print.write(f"Points: {int(points)}", align="center", font=("Arial", 18))

#
#           
#move
def jump():
     flappy_bird.direction="jump"

def move():
    global tube_move_time


    if flappy_bird.direction=="jump":
          y=flappy_bird.ycor()+20
          for i in ground_list:
            if y<200:
                flappy_bird.sety(y)
                y=flappy_bird.ycor()+20
                screen.update()
                
    else:
        y=flappy_bird.ycor()-20
        for i in ground_list:
            if y>-200:
                flappy_bird.sety(y)
                
    time.sleep(0.1)
    
# tubes movent 
def tube_moving(tube_time): 
    global tube_move_time

    end_tube_move_time=time.time()
    if (end_tube_move_time-tube_time)>=0.5:
        tube_move_time=time.time()
        for tube in tube_list_move[:]:
            x=tube.xcor()-30
            if flappy_bird.xcor()>=x-30 and flappy_bird.xcor()<=x+30:
                if flappy_bird.ycor()-20<tube.ycor()+(tube.org_size/2) and flappy_bird.ycor()+20>tube.ycor()-(tube.org_size/2):
                    death()
                else:
                    tube.goto(tube.xcor()-40,tube.ycor())
            else:      
                tube.goto(tube.xcor()-40,tube.ycor())

            if tube.xcor()<-300:
                tube.clear()
                tube_list_move.remove(tube)
    time.sleep(0.1)


def point_counter():
    global points
    for tube in point_tube_list[:]:
        if tube.xcor()<flappy_bird.xcor():
            if tube.kind==3:
                points+=0.5
            else:
                points+=1
            print(points)
            print_points_def()
            point_tube_list.remove(tube)


#
#core of a game
screen.listen()
screen.onkeypress(jump,"w")

flappy_bird.direction="stop"
tube_move_time=time.time()

print(tube_move_time)
while alive:
    screen.update()
    if flappy_bird.direction!="stop":

        if timer==False:
            timer=time.time()

        tubes_spawning_set(timer)



        move()
        if len(tube_list_move)>0:
            tube_moving(tube_move_time)
            point_counter()

        flappy_bird.direction="fall"    
    #


screen.exitonclick()