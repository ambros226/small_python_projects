import os
welcome=1
a=None
action=None
b=None
suma=False
def welcoming():
    global welcome
    if welcome==1:
        print("Welcome to calculator")
    welcome=2
def main_screen():
    global a,b,action,suma
    welcoming()
    if suma==a:
        a=suma
    else:
        a=int(input("First number: > < "))
        
    print("+,-,/,*")

    action=input("Action: > < ")
    while welcome==2:
        b=int(input("Second number: > < "))
        if action=="/" and b==0:
            print("There can't 0 ")
        else:
            break
    counting(action=action,a=a,b=b)
    suma=counting(action,a,b)
    print(f"Výsledek je {suma}")
    end_screen()

def counting(action,a,b):
    if action=="+":
        return a+b
    elif action=="-":
        return a-b
    elif action=="/":
        return a/b
    else:
        return a*b
    
def end_screen():
    global suma
    q=input("Chcete to ukončit ?Y/enter ").lower()
    if q=="y":
        quit()
    else:
        suma=a
        main_screen()
        
main_screen()