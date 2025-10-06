import string

alphabet=list(string.ascii_lowercase)
fin_list=[]
first_half=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
sec_half=[ 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def welcoming_screen():
    quest=input("Do you want to decode or ecode or ceaar code?? De/Ec/Ceas ").lower()
   
    if quest =="de":
        
        decode()

    elif quest=="ceas":
        ceasar_code()

    else:
        print("hh")
        ecode()

def ecode_proces(shift):
    global index,fin_answ
    for i in message:

        if i not in alphabet:
            fin_list.append(i)
        else:
            index=alphabet.index(i)
            fin_list.append(alphabet[index+shift])

    fin_answ="".join(fin_list)
    print(f"{fin_answ}")


def ceasar_code():
    global message
    message=input("Put your message to translate: ").lower()
    ceasar_proces()
    end_screen()

def ceasar_proces():
    global index
    for i in message:
        if i in first_half:
            index=first_half.index(i)
            fin_list.append(sec_half[index])
        elif i in sec_half:
            index=sec_half.index(i)
            fin_list.append(first_half[index])
        else:
            fin_list.append(i)
    fin_answ="".join(fin_list)
    print(f"{fin_answ}")

def ecode():
      global quest2,message
      message=input("Write a message, that do you want ecode: ").lower()
      quest2=int(input("How many shifts.Do you want?? "))
      ecode_proces(shift=quest2)
      end_screen()

def decode():
    global quest2,message
    message=input("Write a message, that do you want decode: ").lower()
    quest2=int(input("How many shifts.Does it have?? "))
    quest2=quest2*-1
    ecode_proces(shift=quest2)
    end_screen()

def end_screen():
    global quest,fin_list
    quest=input("Chceš ještě jednou? A/N").lower()
    
    if quest=="a":
        fin_list=[]
        welcoming_screen()
    else:
        quit()
welcoming_screen()


