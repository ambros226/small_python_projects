import random


print("\nGenerátor hesla \n")
num=["1","2","3","4","5","6","7","8","9","0"]
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
others=["/",".","!","?","%","*","&","#","@"]

ask=int(input("Kolik písmen do hesla chceš? "))

ask2=int(input("Kolik čísel do hesla chceš? "))

ask3=int(input("Kolik zvláštních znaků do hesla chceš? "))

count=ask+ask2+ask3
heslo_list=[]
for i in range (count):
    
    if ask > 0:
        ask=ask-1
        udaj=random.randint(0,9)
        print(num[udaj], end=" ")
        heslo_list.append(num[udaj])

    
    elif ask2 > 0:
        ask2=ask2-1
        udaj=random.randint(0,25)
        print(letters[udaj], end=" ")
        heslo_list.append(letters[udaj])
    
    elif ask3 > 0:
        ask3=ask3-1
        udaj=random.randint(0,8)
        print(others[udaj], end=" ")
        heslo_list.append(others[udaj])

print("\n###############")
size=len(heslo_list)

for i in range (size):
    udaj=random.randint(0,size-1)
    temperature=heslo_list[i]
    heslo_list[i]=heslo_list[udaj]
    heslo_list[udaj]=temperature

#
#Pro příště
#my_list = [1, 2, 3, 4, 5]
#random.shuffle(my_list)
#print(my_list)
#

for i in heslo_list:
    print(i,end=" ")
#fin_pasw=""
#for i in heslo_list:
    #fin_pasw+=i

