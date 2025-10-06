from resources import MENU
from resources import resource
import os
import time
cap=["capucino","cappucino","cappuccino","capuccino"]
lat=["latte","latté","laté","late"]
esp=["espresso","ecspreso","ekspreso","espreso"]
def welcoming_screen():
    print("""
    ----------------------
           CoffeeMat
    ----------------------
    """)
    input("")
    main()
def main():
    cyclus=True
    while cyclus==True:
        print("Menu:")
        print(" 1.Cappuccino(60Kč)\n 2.latte(50Kč)\n 3.espresso(40Kč)\n")
        question=input("Choose a drink: ").lower()
    # here are the drinks they are quiet same,finish a paying and i think that's everything willbe fine
        if question in cap:
            material=mater_controller("cappuccino")
            if material==False:
                print("We don't have enough ingredients")
                continue
            else:
                Pay_ment()
                cyclus=False

        elif question in lat:
            material=mater_controller("latte")
            if material==False:
                print("We don't have enough ingredients")
                continue
            else:
                Pay_ment()
                cyclus=False


        elif question in esp:
            material=mater_controller("espresso")
            if material==False:
                print("We don't have enough ingredients")
                continue
            else:
                Pay_ment()
                cyclus=False

        elif question =="return":
            print(f"Water: {resource["water"]},Milk: {resource["milk"]},Coffee: {resource["coffee"]}")

        else:
            print("Wrong input\nTRY AGAIN")
    os.system("clear")
    welcoming_screen()

def Pay_ment():
    print("You can pay with 1,2,5,10,20,50 crowns")
    paid=0
    crowns=[1,2,5,10,20,50]
    for i in crowns:
        if cost <= paid:
            cash_back=paid-cost
            print(f"We are giving back you: {cash_back}")
            print("The drink is making!")
            time.sleep(5)
            break
        print(f"Missing: {cost-paid}") 
        quest_int=int(input(f"With how many {i} crowns you will pay: "))
        paid+=i*quest_int
    if cost > paid:
        print("Not enough money.Do it again please!")
    


def mater_controller(now_resource):
    global cost 
    
    if (resource["water"]-MENU[now_resource]["ingredients"]["water"])<0 or (resource["milk"]-MENU[now_resource]["ingredients"]["milk"])<0 or (resource["coffee"]-MENU[now_resource]["ingredients"]["coffee"])<0:
        return False
    else:
        resource["water"]-=MENU[now_resource]["ingredients"]["water"]
        resource["milk"]-=MENU[now_resource]["ingredients"]["milk"]
        resource["coffee"]-=MENU[now_resource]["ingredients"]["coffee"]
        cost=MENU[now_resource]["cost"]

welcoming_screen()
