auction={
    
}
def input_char():
    print("""
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\ 
                         `'-------'`
                       .-------------.
                      /_______________\ 

""")
    print("Welcome in silent auction sign to our auction: ")
    end_while=False

    while end_while==False:
            name=input("Your name: ")
            if not verify(name):
                  continue

            sum=int(input("How big sum do you want put into auction? : "))

            auction[name]=sum
            Q=input("Anybody else? or end program?enter/end ").lower()
            if Q=="end":
                  evaluation()

def verify(name):
      if name in auction:
        print("You have the same name as someone before you, please change it!")
        return False  
      return True
      #pro příště
      #return rovnou všechno zastaví 
      #                 
                        

def evaluation():
      
      winner=max(auction,key=auction.get)
      if len(auction)==1:
            print(f"There was only one contestant but the winner is {winner}")
      else:
            print(f"The winner is {winner}")
      quit()
input_char()