import random
import os
def picture():
    print("""""")
def welcoming_screen():
    print("Welcome in !guess number!1-100")
    Q=input("Choose a dificulty and after that push ENTER: easy/hard ").lower()
    input(">>ENTER<<")
    if Q=="easy":
        return 6
    else:
        return 3
def evaluation():
    if guess<0  or guess>100:
        return "out"
    elif guess==answ:
        return True 
    elif guess > answ:
        return "less"
    
    else:
        return "more"
    
def main():
    global answ,tries,guess,evaluation,welcoming_screen,max_tries
    tries=welcoming_screen()
    max_tries=tries
    answ=random.randint(1,100)
    print(answ)

    while tries>0:
        print(f"Máš {tries} pokusů")
        guess=int(input("Your guess: "))
        eval=evaluation()
        print(eval)
        if eval==True:
            end_screen()

        elif eval== "out":
            print("You are out of range 1-100")
            continue

        elif eval=="less":
            tries-=1
            print("The number is smaller")

        else :
            tries-=1
            print("The number is bigger")
        #here a more ifs
            
    end_screen()
def end_screen():
    if eval==True:
        
        if tries==6:
            Q=input(f"Well done you missing {max_tries-tries} tries.\nDo you want to try a hard this time? Y/N").lower()
            if Q=="y":
                os.system('cls')
                main()  
            else:
                quit   
        else:
            print(f"You are really goodyou missing {max_tries-tries} tries.You are winner bye!")
            quit()
    else:
        print(f"Nahhh that's pitty you were close,but the answer was {answ}.")
        Q=input("Do you wanna try it again?Y/N").lower()
        if Q=="y":
            os.system('cls')
            main()
        else:
            quit()
        #here write a repeater after come back
main()
