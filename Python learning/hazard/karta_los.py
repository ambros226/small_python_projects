import random
import time
name=[]
repeater=1
while repeater==1:
      pocet=int(input("Kolik vás tady je? "))
      if pocet>=2:
            repeater=2
            i=0
            while i!=pocet:
               
                  question=input(f"Vlož jméno {i+1}. uživatele ")
                  
                  if question.isnumeric()==False:
                    name.append(question)
                    i+=1
                  else:
                    print("Neplatné jméno")
                    
                    
      
      else:
            print("Je vás málo, lituji")
time.sleep(3)
repeater=0

for i in range(pocet):
   if i !=0:
     print(f" a {name[repeater]}") 
   
   else:
     print(f'Dobře takže {name[repeater]}',end='') 
   repeater= repeater+1

time.sleep(3)
print("Karty jsou v losu!")

for i in range(pocet):
    print(f"Karta číslo {i+1}")

fin_quest=int(input("Jakou kartu si chceš vybrat? "))

answ=random.randint(0,pocet-1)
time.sleep(3)
print(f"A na kartě je {name[answ]}")
