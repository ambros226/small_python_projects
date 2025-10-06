import random
import time
tip_panna=["panna","pana","pavel"]
yes=["a","ano"]
no=["n","ne"]
i=1
count=0
while i==1:
  i2=1
  while i2==1:
     if count<1:
       tip=input("Panna nebo orel? ")
     else:
       tip=input("Takže ještě jednou panna nebo orel? ")

     tip=tip.lower()

     if tip in tip_panna :
      numtip=1
      i2=2
   
     elif tip =="orel" :
       numtip=2
       i2=2
   
     else:
       print("Špatný zápis!")
       continue
  
  time.sleep(3)
  potvrzení=input(f"Tvůj tip je {tip} jsi si jistý?, A/N ")
  potvrzení=potvrzení.lower()
  if potvrzení in yes:
    print("Dobře jdeme na to")
    i=2
    
  elif potvrzení in no:
    print("Tak si vyber znovu.")
    count+=1

time.sleep(3)
print("Mince je hozena!")

time.sleep(2)
print("Točí se točí!")
true=random.randint(1,2)

if true==1:
  answ="panna"

elif true ==2:
  answ="orel"

time.sleep(3)
print("A dopadá!")

time.sleep(1)
print(f"A je na ní {tip}!")

if true==numtip:
  time.sleep(1)
  print("Vyhrál si gratuluji!")

else:
  time.sleep(1)
  print("Prohrál si,jsi " )
  troll=random.randint(15,100)
  for i in range(troll):
   print( ' L' ,end='')









  