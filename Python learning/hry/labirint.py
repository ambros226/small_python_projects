heart=3
heart_calcurator=0
p=0
l=0
i=11

while i>10:
      
    if heart==0:
        print("Game over!")
        import sys
        sys.exit()
    if heart_calcurator==0:
      if heart==1:
         print(f"Máš {heart} život.")
      else:
         print(f"Máš {heart} životy.")
    elif heart_calcurator!=0:
      if heart==1:
         print(f"Máš stále {heart} život.")
      else:
         print(f"Máš stále {heart} životy.")
    heart_calcurator += 1
#Tohle si odděluji pro přehlednost ale ve zkratce tam je počítač životů a pracování s životy
    
    if p==0 and l==0:
        print("Jseš ve vchodu labirintu")
        odpoved=input("Chceš jít doprava, či doleva?(P/L) ")
        odpoved=odpoved.lower()
        if odpoved=="p":
           p= p+1
        elif odpoved=="l":
           l= l+1
        else:
            print("Odpověď je nepochopitelná,tak ještě jednou")

    elif (p!=3 and l==3) or (p==3 and l!=3):
        print("Slepá ulice! Ztácíš život")
        heart-=1
        heart_calcurator=0
        p=0
        l=0
   
    if p==3 and l==3:
        print("Gratuluji jseš v cíli")
        i=2
    #tady to funguje bez problému,podmínky fungují pozor na and (0 v modulu je nula!)
          # ještě podpodmínky
           
    elif p%2==0 and p!=0:
        odpoved=input("Šipka ukazuje doprava, poslechneš jí? (A/N) ")
        odpoved=odpoved.lower()
        print(f"{odpoved}")
        if odpoved=="a" or "ano" or"jo":
            p+=1
        elif odpoved=="n" or "ne":
            l+=1
        else:
            print("Odpověď je nepochopitelná,tak ještě jednou")
    
    elif l%2==0 and l!=0 :
        odpoved=input("Šipka ukazuje doleva, poslechneš jí? (A/N) ")
        odpoved=odpoved.lower()
        if odpoved=="a" or "ano" or"jo":
            l= l+1
        elif odpoved=="n" or "ne":
            p+=1
        else:
            print("Odpověď je nepochopitelná,tak ještě jednou")    
    
    elif p==1:
        odpoved=input("Je tam kobra která ukazuje hlavou doleva,poslechneš jí? (A/N)")
        odpoved=odpoved.lower()
        if odpoved=="a" or "ano" or"jo":
            l+=1
        elif odpoved=="n" or "ne":
            p+=1
        else:
            print("Odpověď je nepochopitelná,tak ještě jednou") 
    elif l==1:
        odpoved=input("Je tam sokol který ukazuje hlavou doleva,poslechneš ho? (A/N)")
        odpoved=odpoved.lower()
        if odpoved=="a" or "ano" or"jo":
            p= p+1
        elif odpoved=="n" or "ne":
            l+=1
        else:
            print("Odpověď je nepochopitelná,tak ještě jednou")    

        
