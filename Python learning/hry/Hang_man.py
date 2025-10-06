import random
words_guess=["auto","ryba","kolo","krk","mortis","kniha","savec"]
guessing_word=[]
secret_word=[]
bad=0
win=False
whl=1
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#There are words for guess:3
def welcoming_screen():
    print("################################\n\nVýtejte ve hře Hangman\n\n################################")
    input(">>>>>> Až budeš připraven stiskni ENTER <<<<<<")
    mainscreen()
#here is a some start screen just for visual.We don't need to coment it anymore!
def letters_output():
    global count,i
    count=0
    for i in letters:
        if count%10==0:
            print("")
        print(i,end=" ")
        count+=1
    
def mainscreen():
    global i,answer,win,bad
    making_word()
    while whl==1:
        hangman_graph()
        print("                   ",end="")
        for i in secret_word:
            print(i,end=" ")
        print("")
        if guessing_word == secret_word:
            win=True
            break
        elif bad==7:
            break
        letters_output()
        print("")
        #Here are graps and decide of wins or loses


        answer=input("Jaké písmeno tedy?: ")
        if answer in guessing_word:
            print("Trefil jsi to!")
            detecting()
            letters_servis()
        else:
            print("Špatně")
            bad+=1
            letters_servis()

    end_screen()

def detecting():
    global i,word_len
    word_len=len(guessing_word)
    for i in range (0,word_len):
        if answer == guessing_word[i]:
            secret_word[i]=answer
            
def letters_servis():
    global i,word_len
    word_len=len(letters)
    for i in range (0,word_len-1):
        if answer == letters[i]:
            letters[i]="#"
def making_word():
    global random_choice,i
    random_choice=random.choice(words_guess)
    for i in random_choice:
        guessing_word.append(i)
    for i in random_choice:
        secret_word.append("_")
#there is a cutter a word

def hangman_graph():

    if bad==0:
        print("""
        # # # # # # # # # # # # #
        #                       #
        #                       #
        #                       #
        #                       #
        #                       # 
        #                       #
        #                       #
        # # # # # # # # # # # # #                           
        """)
    if bad==1:
        print("""
        # # # # # # # # # # # # #
        #                       #
        #                       #
        #                       #
        #                       #
        #                       # 
        #                       #
        #     _____________     #
        # # # # # # # # # # # # #                           
        """)
    if bad==2:
        print("""
        # # # # # # # # # # # # #
        #                       #
        #                       #
        #          |            #
        #          |            #
        #          |            # 
        #          |            #
        #     _____|_____       #
        # # # # # # # # # # # # #                           
        """)
    if bad==3:
        print("""
        # # # # # # # # # # # # #
        #                       #
        #          ________     #
        #          |            #
        #          |            #
        #          |            # 
        #          |            #
        #     _____|_____       #
        # # # # # # # # # # # # #                           
        """)
    if bad==4:
        print("""
        # # # # # # # # # # # # #
        #                       #
        #          ________     #
        #          | /          #
        #          |            #
        #          |            # 
        #          |            #
        #     _____|_____       #
        # # # # # # # # # # # # #                           
        """)
    if bad==5:
        print("""
        # # # # # # # # # # # # #
        #                       #
        #          ________     #
        #          | /    |     #
        #          |            #
        #          |            # 
        #          |            #
        #     _____|_____       #
        # # # # # # # # # # # # #                           
        """)
    if bad==6:
        print("""
        # # # # # # # # # # # # #
        #                       #
        #          ________     #
        #          | /    |     #
        #          |      O     #
        #          |            # 
        #          |            #
        #     _____|_____       #
        # # # # # # # # # # # # #                           
        """)
    if bad==7:
        print("""
        # # # # # # # # # # # # #
        #                       #
        #          ________     #
        #          | /    |     #
        #          |      O     #
        #          |      ^     # 
        #          |            #
        #     _____|_____       #
        # # # # # # # # # # # # #                           
        """)
    if bad==7:
        print("""
        # # # # # # # # # # # # #
        #                       #
        #          ________     #
        #          | /    |     #
        #          |      O     #
        #          |      ^     # 
        #          |      ^     #
        #     _____|_____       #
        # # # # # # # # # # # # #                           
        """)
    #
#Sooooooo there are a graphs with a gelatine
def end_screen():

    print("########################################")
    if win==True:
        print("Jsi opravdu dobrý,Hezky")
        print(f"Zbývalo ti pokusů:{7-bad}")
        print("""
            _________
            \       /
             \  1  /
              \   /
               | |
            ___| |___
        """)

    else:
        print("Nevadí snad to vyjde příště!")
        print(f"Odpověď byla {random_choice}!")
#Just end scren that's all
welcoming_screen()