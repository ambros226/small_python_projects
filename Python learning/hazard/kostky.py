#mirek háže kostkou
money=1000
i2=11
while i2>10:
    vsazka=int(input("Kolik chcete vsadit?(max.250)"))
    if vsazka>250 or money-vsazka<0 :
        print("Moc velká sázka buď kvůli nedostatku peněz nebo kvůli velikosti vsázky.")
        print("Vložte znova!")
    else:
       i2=1    
print("Už sedíš s druhým hráčem u stolu.Řekl ti ať začínáš!")
i2=11
while i2>10:
    ready=input("Až budeš připraven hodit stiskni enter!")
    if ready=="":
        i2=1
        print("Hážeš 1.kostkou a padla...")
        import random
        cube1=random.randint(1,6)
        import time
        time.sleep(5)
        print(f"{cube1}")
        print("Hážeš 2.kostkou a padla...")
        import random
        cube2=random.randint(1,6)
        import time
        time.sleep(5)
        print(f"{cube2}")
        toget1=cube1+cube2
        print(f"Hodil si {cube1} a {cube2},takže dohromady {toget1}.")
        print("Teď háže druhý hráč")
        print("Háže 1.kostkou a padla...")
        import random
        cube3=random.randint(1,6)
        import time
        time.sleep(5)
        print(f"{cube3}")
        print("Háže 2.kostkou a padla...")
        import random
        cube4=random.randint(1,6)
        import time
        time.sleep(5)
        print(f"{cube4}")
        toget2=cube3+cube4
        print(f"Hodil {cube3} a {cube4},takže dohromady {toget2}.")
        if toget1>toget2:
           print("Vyhrál si")
           money=money+vsazka
           print(f"Vyhrál si {vsazka} a teď máš {money}")
        else: 
            print("Vyhrál druhý hráč ")
            money=money-vsazka
            print(f"Prohrál si {vsazka} a teď máš {money} ")
        
    else:
        print("Máš tam něco blbě stačí zmáčknou enter.")

