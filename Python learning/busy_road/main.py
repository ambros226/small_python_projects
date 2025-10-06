from turtle import *
import random
import time

enemy_car_running_move=True
enemy_car_running_spawn=True
strip_running=True
#screen settinggs(backround and settings)
screen=Screen()
screen.bgcolor("#85A947")
screen.title("Busy road ")
screen.setup(width=600, height=600)
screen.tracer(False)
#

#Road (decoration)
_road=Turtle("square")
_road.color("#3E7B27")
_road.shapesize(stretch_wid=22,stretch_len=30)
_road.stamp()
_road.color("#9AA6B2")
_road.shapesize(stretch_wid=20,stretch_len=30)
_road.stamp()
_road.hideturtle()

#

# white_stripes(decoration)
#
stripe_list=[]
for i in range(-200,300,200):
    for _ in range(2):
        if _==0:
            road_stripe=Turtle("square")
            road_stripe.color("white")
            road_stripe.penup()
            road_stripe.shapesize(stretch_wid=1,stretch_len=3.5)
            road_stripe.goto(i,-80)
        else:
            road_stripe=Turtle("square")
            road_stripe.color("white")
            road_stripe.penup()
            road_stripe.shapesize(stretch_wid=1,stretch_len=3.5)
            road_stripe.goto(i,80)

        stripe_list.append(road_stripe)

def strip_running_control():

    if strip_running==True:
        ontimer(stripe_move,200)


def stripe_move():
    for one_stripe in stripe_list:
        one_stripe.goto(one_stripe.xcor()-30,one_stripe.ycor())

        if one_stripe.xcor()+20<=-300:
            one_stripe.setx(300)

    screen.update()
    strip_running_control()

stripe_move()
#
#  
 
#
def main_car_front_move():
    main_car.setx(main_car.xcor()+40)
    main_car_glass.setx(main_car_glass.xcor()+40)

def ending(Win):
    global strip_running, enemy_car_running_move,enemy_car_running_spawn,alive,car_point_list


    if Win:
        print("O")
        enemy_car_running_spawn=False
        car_point_list=[]
        try:
            while car_move_list[-1][0].xcor()>-300:
                move()
                enemy_car_moving_control()
                screen.update()
        except IndexError:
            print("Pass")
            pass

        enemy_car_running_move=False
        
        for car in car_move_list[:]:
            car[0].clear()
            car[0].hideturtle()
            del car[0]
            car[0].clear()
            car[0].hideturtle()
            del car[0]
            car_move_list.remove(car)

        print("1")
        alive=False
        while main_car.xcor()<=300:
            print("2")
            ontimer(main_car_front_move(),200)
            screen.update()

        strip_running=False
        print("3")
        for object in screen.turtles():
            object.hideturtle()
            object.stamp()


        points_print.hideturtle()
        points_print.clear()
        points_print.color("#85A947")

        end_print = Turtle("square")
        end_print.penup()
        end_print.goto(0,0)
        end_print.color("black")
        end_print.hideturtle()
        end_print.write(f"Winner\n",align="center", font=("Arial", 80,"bold"))
        end_print.write(f"Points: {int(points)}", align="center", font=("Arial", 35,"bold"))
        screen.update()

    else:
        strip_running=False
        enemy_car_running_move=False
        enemy_car_running_spawn=False
        alive=False

        
        #explosion
        for layer in range(3):
            explosion=Turtle("square")
            explosion.penup()
            explosion.goto(main_car.xcor(),main_car.ycor())
            match layer:
                case 0:
                    explosion.color("#E52020")
                case 1:
                    explosion.color("#FFC145")
                case 2:
                    explosion.color("#ECE852")
            
            explosion_size=4
            for _ in range(3-layer):
                explosion_size+=4
                explosion.shapesize(stretch_wid=explosion_size,stretch_len=explosion_size)
                screen.update()
                time.sleep(0.05)

        points_print.hideturtle()
        points_print.clear()
        points_print.color("#85A947")

        for object in screen.turtles():
            object.hideturtle()
            object.stamp()
            

        end_print = Turtle("square")
        end_print.penup()
        end_print.goto(0,40)
        end_print.color("black")
        end_print.hideturtle()
        end_print.write(f"GAME OVER\n",align="center", font=("Arial", 70,"bold"))
        end_print.write(f"Points: {int(points)}", align="center", font=("Arial", 35,"bold"))
        screen.update()
        #explosion
        

#

#main_car/character
#
main_car=Turtle("square")
main_car.color("#A91D3A")
main_car.shapesize(stretch_wid=3.5,stretch_len=6)
main_car.penup()
main_car.goto(-140,0)

main_car_glass=Turtle("square")
main_car_glass.color("#98D8EF")
main_car_glass.shapesize(stretch_wid=3,stretch_len=2)
main_car_glass.penup()
main_car_glass.goto(-110,0)

main_car_list=[main_car,main_car_glass]

#car move
main_car.move_direction="!start"
def up_move():
    main_car.move_direction="up"

def up_down():
    main_car.move_direction="down"

def move():
    if main_car.move_direction == "up":
        y=main_car.ycor()+70
        if y<((20 * 20)/2):
            main_car_move(70)
            screen.update()
            ontimer(main_car_move(70),200)

    elif main_car.move_direction == "down":
        y=main_car.ycor()-70
        if y>((-20 * 20)/2):
            main_car_move(-70)
            screen.update()
            ontimer(main_car_move(-70),200)

def main_car_move(move_value):
    for object in main_car_list:
        object.sety(object.ycor()+move_value)



screen.listen()
screen.onkeypress(up_move,"w")
screen.onkeypress(up_down,"s")
#
#


#other cars
#

#spawn cars
car_spawn_time=4000
def enemy_car_spawning_control():

    if enemy_car_running_spawn==True:
        ontimer(car_spawn,car_spawn_time)




car_move_list=[]
car_point_list=[]
def car_spawn():
    for y in range(-140,141,140):
        if points>=100:
            dificulty_sys()
            break

        chance_enemy_spawn=[1,1,2]
        random_spawn=random.choice(chance_enemy_spawn)
        if random_spawn==2:
            try:
                if car_move_list[-1][0].xcor()!=300 and y==140:
                    random_spawn=1
            except IndexError:
                pass

        if random_spawn==1:
            try:
                if car_move_list[-2][0].xcor()==300:
                    continue
            except IndexError:
                pass


            enemy_car=Turtle("square")

            colors=["#35374B","#1D24CA","#F99417","#FFCF50","#77B254","#8E1616","#E82561","#4C585B"]
            enemy_car.color(random.choice(colors))

            enemy_car.shapesize(stretch_wid=3.5,stretch_len=6)
            enemy_car.penup()
            enemy_car.goto(300,y)

            enemy_car_glass=Turtle("square")
            enemy_car_glass.color("#98D8EF")
            enemy_car_glass.shapesize(stretch_wid=3,stretch_len=2)
            enemy_car_glass.penup()
            enemy_car_glass.goto(280,y)

            
            car_move_list.append([enemy_car,enemy_car_glass])
            car_point_list.append(enemy_car)

    enemy_car_spawning_control()    
#
#car move
car_speed_time=500

def enemy_car_moving_control():
    if enemy_car_running_move==True:
        ontimer(car_move,car_speed_time)

def car_move():
    for car in car_move_list[:]:
            if (main_car.xcor()+60>=car[0].xcor()-60 and main_car.xcor()-60<=car[0].xcor()-60) or (main_car.xcor()+40>=car[0].xcor()+60 and main_car.xcor()-40<=car[0].xcor()+60):
                 
                if main_car.ycor()==car[0].ycor():
                    ending(False)
                else:      
                    car[0].setx(car[0].xcor()-40)
                    car[1].setx(car[1].xcor()-40)
            else:      
                car[0].setx(car[0].xcor()-40)
                car[1].setx(car[1].xcor()-40)

            if car[0].xcor()<-340:
                car[0].clear()
                car[0].hideturtle()
                del car[0]
                car[0].clear()
                car[0].hideturtle()
                del car[0]
                car_move_list.remove(car)

            
    enemy_car_moving_control()

#
#

#level changer
level=0
levels={
    1:{
        "turning point" : 5,
        "car speed" : 300,
        "car spawn" : 3000
    },
    2:{
        "turning point" : 15,
        "car speed" : 200,
        "car spawn" : 2000
    },
    3:{
        "turning point" : 50,
        "car speed" : 150,
        "car spawn" : 1500
    },
    4:{
        "turning point" : 75,
        "car speed" : 100,
        "car spawn" : 1500
    },
    5:{
        "turning point" : 100,
        "car speed" : 100,
        "car spawn" : 1500
    }

}
def dificulty_sys():
    global level,car_speed_time,car_spawn_time
    try:
        if points>= levels[level+1]["turning point"]:
            level+=1

        
            car_speed_time=levels[level]["car speed"]
            car_spawn_time=levels[level]["car spawn"]


    except KeyError:
            print("win")
            ending(True)

#


#point_calculator
points=0
points_print = Turtle("square")
points_print.color("white")
points_print.penup()
points_print.hideturtle()
points_print.goto(0,255)  

def sign_points():
    points_print.clear()
    points_print.write(f"Points: {int(points)}", align="center", font=("Arial", 35,"bold"))
sign_points()

def point_calculator():
    global points
    for car in car_point_list:
        if car.xcor() <= main_car.xcor():
            print(car_point_list)
            points+=1
            sign_points()
            dificulty_sys()
            #deleting a cars from point list
            filtered_cars=[]
            for filtered_car in car_point_list:
                if filtered_car.xcor()==car.xcor():
                    filtered_cars.append(filtered_car)
                else:
                    break

            for deleted_car in filtered_cars:
                car_point_list.remove(deleted_car)
            #
            
        else:
            break
#

    
#
#
def begin():
    print(main_car.move_direction)
    while main_car.move_direction=="!start":
        move()
        screen.update()
        print(main_car.move_direction)

    print("out")
    game_play()


def game_play():
    alive=True
    ontimer(car_spawn,4000)
    enemy_car_moving_control()

    while alive==True:
        move()
        main_car.move_direction="stop"
        screen.update()
        point_calculator()
    #
#  
begin()
screen.exitonclick()