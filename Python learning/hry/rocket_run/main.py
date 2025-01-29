from turtle import Turtle,Screen
import time
import random
level=1
field_size=16
last_time=0
rockets_list=[]
game_over=False
#screen základní nastavení
screen=Screen()
screen.bgcolor("black")
screen.title("Rocket_run")
screen.setup(width=600, height=600)
screen.tracer(False)
#

#level_end
def level_end():

    time_end=time.time()
    if round(time_end-time_start)>=60:
        time.sleep(2)
        rocket_man.goto(0,0)
        print("level_end")
        rocket.hideturtle()
        return True
#  

#   
#spawning rockets
def spawning_beforeset():
    global last_time
    time_end=time.time()
    if round(time_end-time_start)%2==0:
        if last_time !=round(time_end-time_start):
            spawning()
            last_time=round(time_end-time_start)

def spawning():
    global y_rocket,x_rocket,rocket
    q=random.randint(0,1)
    choice_list=[290,-290]

    rocket=Turtle("square")
    rocket.penup()
    rocket.color("red")
    rocket.shapesize(stretch_wid=2, stretch_len=2)

    if q==1:
        y_rocket=random.choice(choice_list)
        rocket.org_dir=["y",y_rocket]
        x_rocket=random.randrange(int(-((field_size * 20) /2)),int(((field_size * 20) /2)))

        if x_rocket>=int(-((field_size * 20) /2)) and x_rocket<=int(-((field_size * 20) /2))+20:
            x_rocket+=30

        elif x_rocket<=int(((field_size * 20) /2)) and x_rocket>=int(((field_size * 20) /2))-20:
            x_rocket-=30
    else:
        y_rocket=random.randrange(int(-((field_size * 20) /2)),int(((field_size * 20) /2)))
        if y_rocket>=int(-((field_size * 20) /2)) and y_rocket<=int(-((field_size * 20) /2))+20:
            y_rocket+=30

        elif y_rocket<=int(((field_size * 20) /2)) and y_rocket>=int(((field_size * 20) /2))-20:
            y_rocket-=30

        x_rocket=random.choice(choice_list)
        rocket.org_dir=["x",x_rocket]
    
    
    rocket.goto(x_rocket,y_rocket)
    rockets_list.append(rocket)




#
#rocket move
def rocket_moving():

    for object in rockets_list[:]:

        if object.org_dir[0]=="x":
            if object.org_dir[1]==-290:
                object.goto(object.xcor()+30,object.ycor())
            else:
                object.goto(object.xcor()-30,object.ycor())
            
        else:
            if object.org_dir[1]==-290:
                object.goto(object.xcor(),object.ycor()+30)
            else:
                object.goto(object.xcor(),object.ycor()-30)


        if object.xcor()>=290 or object.ycor()<=-290 or object.xcor()>=290 or object.ycor()<=-290:
            rockets_list.remove(object)


#
#level printer settings and function
level_print = Turtle("square")
level_print.speed(0)
level_print.color("white")
level_print.penup()
level_print.hideturtle()
level_print.goto(0, 265)

def print_level_def():
    level_print.clear()
    level_print.write(f"Level: {level}", align="center", font=("Arial", 18))

print_level_def()   
#
#man death
def man_death():
    for object in rockets_list:
        if object.distance(rocket_man)<35:
            rocket.hideturtle()
            playing_field.hideturtle()
            screen.bgcolor("red")
            level_print.clear()
            level_print.goto(0,50)
            level_print.write(f"GAME OVER\n",align="center", font=("Arial", 30))
            level_print.write(f"Level: {level}", align="center", font=("Arial", 18))
            return True
            
#field
playing_field=Turtle("square")
playing_field.color("#7EE62E")
playing_field.penup()
playing_field.goto(0,0)
playing_field.shapesize(stretch_wid=15.5, stretch_len=15.5)
playing_field.stamp()
#
#rocket_man
rocket_man=Turtle("square")
rocket_man.color("blue")
rocket_man.penup()
rocket_man.goto(0,0)
rocket_man.shapesize(stretch_wid=1.5, stretch_len=1.5)
rocket_man.direction="stop"

#
#move
def move():
    if rocket_man.direction == "up":
        y=rocket_man.ycor()+20
        if y<((field_size * 20) /2):
            rocket_man.sety(y)

    elif rocket_man.direction== "down":
        y=rocket_man.ycor()-20
        if y>-((field_size * 20) /2):
            rocket_man.sety(y)
    elif rocket_man.direction== "left":
        x=rocket_man.xcor()-20
        if x> -((field_size * 20) /2):
            rocket_man.setx(x)
        
    elif rocket_man.direction== "right":
        x=rocket_man.xcor()+20
        if x<((field_size * 20) /2):
            rocket_man.setx(x)
    screen.update()

def move_up():
    rocket_man.direction="up"
    
def move_down():
    rocket_man.direction="down"

def move_left():
    rocket_man.direction="left"
def move_right():
    rocket_man.direction="right"
    
   

screen.listen()
screen.onkeypress(move_up,"w")
screen.onkeypress(move_down,"s")
screen.onkeypress(move_left,"a")
screen.onkeypress(move_right,"d")
#
#
def level_changer():
    
    if level==2:
        field_size=13.5
    elif level==3:
        field_size=11.5
    elif level==4:
        field_size=9.5
    elif level==5:
        field_size=7.5
    else:
        field_size=30
        level_print.goto(0,50)
        screen.bgcolor("blue")
        level_print.write(f"WIN WELL DONE\n",align="center", font=("Arial", 35))
        level_print.write(f"Level: {level}", align="center", font=("Arial", 18))
        screen.update()
        time.sleep(5)
        return True



    playing_field.clearstamps()
    playing_field.shapesize(stretch_wid=field_size, stretch_len=field_size)
    playing_field.stamp()

#
#engine
while game_over==False:
    time_start=time.time()
    if level>1:
        if level_changer():
            break

    while True:
        print_level_def()
        screen.update()
        if level_end():
            level+=1
            screen.update()
            break
        spawning_beforeset()
        rocket_moving()
        move()
        time.sleep(0.1)
        rocket_man.direction="stop"
        if man_death():
            screen.update()
            time.sleep(4)
            game_over=True
            break

screen.exitonclick()
