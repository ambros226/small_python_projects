import time
import random
money=1000
i2=11
red_nums=[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
black_nums=[2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
befmoney=money
while i2>10:
    
    print("Ruleta je připravena.červené čísla:1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36\n/černé čísla:2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35\n ")
    
    while i2==11:
      quest=input("Chceš vsadit na číslo nebo na jen barvu? ")
      quest=quest.lower()
      
      if quest=="číslo":
         i2+=1
         číslo=int(input("Na kolikátku vsázíš? "))
         
         if číslo in red_nums:
            barva="červená"
            print(f"Dobrá vsázíš na {číslo} barvy {barva}")
         
         elif číslo in black_nums: #číslo==2 or 4 or 6 or 8 or 10 or 11 or 13 or 15 or 17 or 20 or 22 or 24 or 26 or 28 or 29 or 31 or 33 or 35:
            barva="černá"
            print(f"Dobrá vsázíš na {číslo} barvy {barva}")
      
      elif quest=="barva":
         i2+=1
         číslo=0
         while i2==12:
           colquest=input("Vsázíš na červenou nebo na černou? ")
           colquest=colquest.lower()
           
           if colquest=="černá":
            i2+=1
            barva="černá"
            print(f"Vsázíš na {barva}")
           
           elif colquest=="červená":
            i2+=1
            barva="červená"
            print(f"Vsázíš na {barva}")
           
           else:
            print("Chyba v zápisu zkus to jinak.")
      
      else:
         print("Chyba v zápisu zkus to jinak.")  
    
      i3=11
      
    while i3>10:
        bet=int(input("Kolik chcete vsadit?"))
        
        if befmoney-bet<0 :
          print("Moc velká sázka buď kvůli nedostatku peněz nebo kvůli velikosti vsázky.")
          print("Vložte znova!")
          print(f"{befmoney}{barva}")
        elif bet==befmoney and barva=="červená":
            i3 = 1
            mira=input("Nejsi ty náhodou mirek?:D ")
            mira=mira.lower()
            mira_answ=["jj","ano","jo"]
            if mira in mira_answ:
              print("Já to věděl takhle ruleta nefunguje!!:D")
              time.sleep(2)
    
            else:
              print("Nodobře budu ti věřit.")
        
        else:
          i3=1    
    
    
    
    
    
    while i2>10:
          ready=input("Až budeš připraven hodit stiskni enter! ")
          
          if ready=="":
            i2=1
            print("Dobrá pomocník roztáčí ruletu.")
            time.sleep(2)
            print("Kulička se točí")
            time.sleep(2)
            print("Točí!")
            ball=random.randint(1,36)
            time.sleep(2)
            
            if ball in black_nums:
              legbarva="černá"
            
            elif ball in red_nums:
              legbarva="červená"
            
            print(f"a padá {ball} {legbarva}")
            
          else:
            print("Máš tam něco blbě stačí zmáčknou enter.")
    
    if ball==číslo:
      befmoney=befmoney + (bet *35)
    
    elif ball != číslo and legbarva==barva:
      befmoney=befmoney -  bet
    
    elif legbarva==barva:
      befmoney= befmoney + (bet*2)
    
    
    if (money-befmoney)<0:
      print(f"Prodělal si {(money+befmoney)*-1}")
    
    else:
      print(f"Vydělal si {money - befmoney}")
      
    




