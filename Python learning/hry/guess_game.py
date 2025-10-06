import random
import time
#characters=["harry","hermiona","ron","draco","snape","albus"]
#answ=random.choice(characters)
#guess=""
#while answ != guess:
    #guess=input("?").lower()
#print("great")
clues=5
level=1
tries=5
#hair
beld=["holly","kryton"]

long=["penny","amy","bernadet","rachel","monika","feebe"
      ,"many","kočanská","dave","kocour","francis","iva","ozák"
      ,"saša","simona","marcelka","robin","lily"]

short=["sheldon","leonard","rajesh","howard","stuart"
       ,"ross","chandler","joey","rimmer","bernard","lexa"
       ,"tomáš","horvi","barney","ted","marshall","ranjit"]

blond=["bernadet","feebe","marcelka","barney"]
darkblond=["rachel","penny"]
brunet=["sheldon","leonard","rajesh","amy","howard","stuart","ross","monika","chandler","joey","dave","rimmer","kocour","kočanská","many","bernard","francis","lexa","iva","tomáš","ozák","saša","simona","horvi","ted","robin","marshall","lily","ranjit"]

#hair
#gender
men=["sheldon","leonard","rajesh","howard","stuart","ross"
     ,"chandler","joey","dave","rimmer","kocour","many","bernard"
     ,"lexa","tomáš","ozák","horvi","barney","ted","marshall","ranjit"]

women=["penny","amy","bernadet","rachel","monika","feebe"
       ,"kočanská","francis","iva","saša","simona","marcelka","robin","lily",]
robot=["kryton","holly"]
#gender

#character

tease=["howard","chandler","dave","holly","lexa","barney","penny","joey"]
psychopat=["sheldon","amy","bernard","tomáš","ozák","barney","simona"]
proutník=["barney","ted","joey","howard","rajesh"]
nice=["leonard","rajesh","penny","bernadet","feebe","rachel","monika"
      ,"kočanská","holly","many","francis","iva","saša","simona","horvi","marcelka","ted","robin","marshall","lily","ranjit"]

hysterical=["leonard","rajesh","stuart","ross","rachel","monika"
            ,"kryton","ted","kočanská","bernard","iva","marcelka","lily"]

#character

big_bang_teory=["sheldon","leonard","rajesh","penny","amy","bernadet","howard","stuart"]
friends=["ross","rachel","monika","chandler","feebe","joey"]
red_dwarf=["kryton","dave","rimmer","kocour","holly","kočanská"]
black_books=["many","bernard","francis"]
come_back=["lexa","iva","tomáš","ozák","saša","simona","horvi","marcelka"]
hym=["barney","ted","robin","marshall","lily","ranjit"]
characters=[big_bang_teory,friends,red_dwarf,black_books,come_back,hym]
#Here are the lists with a names

print("################################\n\nVýtejte ve hře Sitcome guessname\n\n################################")
print("Pravidla jsou následovné:\n Máš 5 životů!\n Jen křestní jména popřípadě přezdívky!\n Je tady 5 levelů v každém máš míň nápověd!\n Postavy jsou z Přátel, Teorie velkého třesku, Červeného trpaslíka, \n Black books, Comebacku, Dva a půl chlapa a Jak jsem poznal vaši matku")
#this belong to main screen bad becouse of repeating i had to close it
def difficulty():
    global dif
    if level==1:
        dif="Easy"
    elif level==2:
        dif="Normal"
    elif level==3:
        dif="Medium" 
    elif level==4:
        dif="Hard"
    elif level==5:
        dif="Imposible" 
#Only levels essy things 

def clue_process():
    global count
    count=0
    if level>=1 and level<5:
        print("Nápovědy:")
    if level==1:
        count+=1
        print(f"{count}. Seriál: ",end="")
        if choice in big_bang_teory:
            print("Teorie velkého třesku")
        if choice in friends:
            print("Přátelé")
        if choice in red_dwarf:
            print("Červený trpaslík")
        if choice in black_books:
            print("Black books")
        if choice in come_back:
            print("Comeback")
        if choice in hym:
            print("Jak jsem poznal vaši matku!")
    if level>=1 and level<3:
        count+=1
        print(f"{count}. Vlasy: ",end="")
        if choice in long:
            print("spíše delší a ",end="")
        if choice in short:
            print("spíše kratší a ",end="")
        if choice in beld:
            print("Má spíše plešššššššš!")
        if choice in blond:
            print("spíše blonďatý",end="")
        if choice in darkblond:
            print("Má spíše špinavý blond",end="")
        if choice in short:
            print("spíše tmavší",end="")
        print("")
    if level>=1 and level<5:
        count+=1
        print(f"{count}. Charakter: ",end="")
        if choice in psychopat:
            print("Je dost nevšední/á a výstřední/á ",end="")
        if choice in tease:
            print("Je vtipálek je závný/á",end="")
        if choice in nice:
            print("Je pohodový/á a hodný/á ",end="")
        if choice in proutník:
            print("Je to proutník/čka(Měl/a hodně partnerů)  ",end="")
        if choice in hysterical:
            print("Často dělá scény (jak se má špatně) a lituje se ",end="")
        print("")
    if level>=1 and level<4:
        count+=1
        if choice in robot:
            print(f"{count}. Gender: Stroj")
        if choice in men:
            print(f"{count}. Gender: Muž")
        if choice in women:
            print(f"{count}. Gender: Žena")
    
        
            
def guessing_proces():
    global choice,choice2,guess,tries,level

    choice2=random.choice(characters)
    choice=random.choice(choice2)
    clue_process()
    
    while i==False:
        print(choice)
        print(choice)
        print(choice2)
        if tries ==0:
            print("Je mi líto vypadl si!")
            end_screen()
        print(f"Máš ještě {tries} životů")
        guess=input("Tak teda hádej: ").lower()

        if guess==choice:
            print("Uhodl jsi správně\nPokračuješ do dalšího levelu")
            level+=1
            break
            #there will be part to a end level screen or main screen i am not still sure but it is not too important
        else:
            tries-=1
            if tries==0:
                print("Jaaaaj")
            else:
                print("Ne to je špatně\nHádej dál")
    main_screen()

def main_screen():
    global i
    time.sleep(1)
    i=False
    difficulty()
    print(f"\n################################\nLevel: {level}({dif})")
    if level==6:
        end_screen()
    elif level!=1:
        print(f"Dobře level {level} si zvládl, ale u levelu {level+1} nemáš šanci!")
        guessing_proces()
    else:
        guessing_proces()
    #maybe i will expand becouse of coreect answer

def end_screen():
    if level==6:
        print("!!! Gratuluji dokázal jsi to !!!")
    
    elif level==1:
        print(f"To je hrůzaa!\n vypadl si na Level: {level}")
    
    else:
        print(f"Nevadí, i tak ses dostal daleko!\nvypadl si na Level: {level}")
    quit()

    
main_screen()