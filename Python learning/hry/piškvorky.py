import random
import time

AI=["pc","ai"]
kam=["kam","kamarad","friend","kamarád"]
Quest_1=input("Chceš hrát proti AI nebo proti kamarádovi? ").lower()
rada0=["#","#","#"]
rada1=["#","#","#"]
rada2=["#","#","#"]
pole=[rada0,rada1,rada2]
x=["X","X","X"]
Ovalue=["O","O","O"]


if Quest_1 in AI:
    print("Losování  toho kdo začíná \nzačíná :D !")
    
    los=random.randint(4,15)
    start=random.randint(1,2)
    
    for i in range (los):
        
        if i%2==0:
            time.sleep(1)
            print("TY ai")
        
        else:
             time.sleep(1)
             print("ty AI")
    
    
    if start == 1:
        print("ty AI")
        time.sleep(1)
        print("AI začíná")
        count=2
    
    else:
        print("TY ai")
        time.sleep(1)
        print("Začínáš!")
        count=1
    
    tomi_nekoukej_sem="-"
    
    while tomi_nekoukej_sem=="-":
        time.sleep(1)
        print("________________________")
        time.sleep(2)
        print(rada0)
        print(rada1)
        print(rada2)
        ai_count=1
        you_count=1

        if (x==rada0) or (x==rada1) or (x==rada2):
            print("Prohra")
            tomi_nekoukej_sem="Prohra"
            continue
        
        
        elif (Ovalue==rada0) or (Ovalue==rada1) or (Ovalue==rada2):
            print("Vyhra")
            tomi_nekoukej_sem="Výhra"
            continue
        
        
        elif (("#" not in rada0) and ("#" not in rada1)and ("#" not in rada2)) and count>2:
            print("Remíza")
            tomi_nekoukej_sem="Remíza"
            continue

        
        elif (rada0[0]=="X"and rada1[1]=="X" and rada2[2]=="X") or (rada0[2]=="X"and rada1[1]=="X" and rada2[0]=="X"):
            print("Prohra")
            tomi_nekoukej_sem="Prohra"
            continue


        elif (rada0[0]=="O"and rada1[1]=="O" and rada2[2]=="O") or (rada0[2]=="O"and rada1[1]=="O" and rada2[0]=="O"):
            print("Vyhra")
            tomi_nekoukej_sem="Výhra"
            continue
        
        elif (rada0[0]=="X"and rada1[0]=="X" and rada2[0]=="X") or (rada0[1]=="X"and rada1[1]=="X" and rada2[1]=="X") or (rada0[2]=="X"and rada1[2]=="X" and rada2[2]=="X"):
            print("Prohra")
            tomi_nekoukej_sem="Prohra"
            continue


        elif (rada0[0]=="O"and rada1[0]=="O" and rada2[0]=="O") or (rada0[1]=="O"and rada1[1]=="O" and rada2[1]=="O") or (rada0[2]=="O"and rada1[2]=="O" and rada2[2]=="O"):
            print("Vyhra")
            tomi_nekoukej_sem="Výhra"
            continue

        
        
        
        
        
        
        if count%2==0:
            while ai_count==1:
                udaj1=random.randint(0,2)
                udaj2=random.randint(0,2)

                if pole[udaj1][udaj2]=="X" or pole[udaj1][udaj2]=="O":
                    print("nothing")
                else:
                    pole[udaj1][udaj2]="X"
                    count+=1
                    ai_count+=1



        else: 
           while you_count==1:
             blbost=1
             while blbost==1:
                print("Teď zapíšeš souřanice, kde chceš zahrát")
                udaj1=int(input("Řada: "))
                udaj2=int(input("Sloupec: "))
               
                
            
                if pole[udaj1][udaj2]=="X" or pole[udaj1][udaj2]=="O":

                    print("Toto políčko je už zaplněné!")
                else:
                    pole[udaj1][udaj2]="O"
                    you_count+=1
                    count+=1

elif Quest_1 in kam:
    print("Není v tuto chvíli funkční!")


else:
    print("Dobře tak nic")



