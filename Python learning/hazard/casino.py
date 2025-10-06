i=11
money=1000
while i<12:
    print(f"Máš {money} coinů")
    rozhodnutí=input("Chceš ruletu nebo kostky? nebo chceš jít pryč?")
    rozhodnutí=rozhodnutí.lower()
    if rozhodnutí=="kostky":
         print("ok")
    elif rozhodnutí=="ruleta":
         print("okk")
    elif rozhodnutí=="pryč":
        print("Přijdeš o miliony noalejak myslíš.")
        import sys
        sys.exit()
    elif rozhodnutí != "ruleta" or "kostky":
         print("Špatná odpověď zkus uadat znova.")