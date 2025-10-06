import random
import time
import os
high_score=0
second_data=0
first_data=0
score=0
data=[
     {
        'name': 'Instagram',
        'follower_count': 501,
        'description': 'Sociální platforma',
        'country': 'USA'
    },
    {
        'name': 'Facebook',
        'follower_count': 4,
        'description': 'Sociální platforma',
        'country': 'USA'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 436,
        'description': 'Fotbalový hráč',
        'country': 'Portugal'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 161,
        'description': 'Herec a wrestler',
        'country': 'USA'
    },
    {
        'name': 'Harry Potter film',
        'follower_count': 8,
        'description': 'Film',
        'country': 'USA'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 307,
        'description': 'Podnikatelka',
        'country': 'USA'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 324,
           'description': 'Fotbalista',
        'country': 'Argentina'
    },
    {
        'name': 'Neymar',
        'follower_count': 158,
        'description': 'Fotbalista',
        'country': 'Brazilie'
    },
    {
        'name': 'Eminem',
        'follower_count': 40,
        'description': 'Hudebník',
        'country': 'USA'
    },
    {
        'name': 'Justin Bieber',
        'follower_count': 193,
        'description': 'Hudebník',
        'country': 'Canada'
    },
    {
        'name': 'Emma Watson',
        'follower_count': 111,
        'description': 'Herečka',
        'country': 'Francie'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 430,
        'description': 'Hudebnice a herečka',
        'country': 'USA'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 400,
        'description': 'Podnikatelka a influencerka',
        'country': 'USA'
    },
    {
        'name': 'Taylor Swift',
        'follower_count': 280,
        'description': 'Hudebnice',
        'country': 'USA'
    },
    {
        'name': 'Billie Eilish',
        'follower_count': 110,
        'description': 'Hudebnice',
        'country': 'USA'
    },
    {
        'name': 'Shakira',
        'follower_count': 88,
        'description': 'Hudebnice',
        'country': 'Kolumbie'
    },
    {
        'name': 'Tom Holland',
        'follower_count': 87,
        'description': 'Herec',
        'country': 'UK'
    },
    {
        'name': 'Zendaya',
        'follower_count': 185,
        'description': 'Herečka',
        'country': 'USA'
    },
    {
        'name': 'NASA',
        'follower_count': 104,
        'description': 'Vědecká organizace',
        'country': 'USA'
    },
    {
        'name': 'Elon Musk',
        'follower_count': 158,
        'description': 'Podnikatel',
        'country': 'USA'
    },
    {
        'name': 'Oprah Winfrey',
        'follower_count': 43,
        'description': 'Moderátorka a producentka',
        'country': 'USA'
    },
    {
    'name': 'LeBron James',
    'follower_count': 162,
    'description': 'Basketbalista',
    'country': 'USA'
    },
    {
        'name': 'Rihanna',
        'follower_count': 158,
        'description': 'Hudebnice a podnikatelka',
        'country': 'Barbados'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 370,
        'description': 'Hudebnice',
        'country': 'USA'
    },
    {
        'name': 'The Rock (Dwayne Johnson)',
        'follower_count': 390,
        'description': 'Herec a wrestler',
        'country': 'USA'
    },
    {
        'name': 'Virat Kohli',
        'follower_count': 260,
        'description': 'Kriketista',
        'country': 'Indie'
    },
    {
        'name': 'NASA Webb Telescope',
        'follower_count': 5,
        'description': 'Vědecký projekt',
        'country': 'USA'
    },
    {
        'name': 'Cristiano Ronaldo Jr.',
        'follower_count': 6,
        'description': 'Dítě známého sportovce',
        'country': 'Portugal'
    },
    {
        'name': 'Bill Gates',
        'follower_count': 50,
        'description': 'Podnikatel a filantrop',
        'country': 'USA'
    },
    {
        'name': 'Jeff Bezos',
        'follower_count': 35,
        'description': 'Podnikatel',
        'country': 'USA'
    },
    {
        'name': 'National Geographic',
        'follower_count': 290,
        'description': 'Mediální společnost',
        'country': 'USA'
    },
    {
        'name': 'David Beckham',
        'follower_count': 82,
        'description': 'Fotbalista',
        'country': 'UK'
    },
    {
        'name': 'Katy Perry',
        'follower_count': 110,
        'description': 'Hudebnice',
        'country': 'USA'
    },
    {
        'name': 'Gigi Hadid',
        'follower_count': 78,
        'description': 'Modelka',
        'country': 'USA'
    },
    {
        'name': 'Shawn Mendes',
        'follower_count': 72,
        'description': 'Hudebník',
        'country': 'Canada'
    },
    {
        'name': 'Chris Hemsworth',
        'follower_count': 60,
        'description': 'Herec',
        'country': 'Australia'
    }
]
def high_score_evaluation():
    global high_score,score
    if score>high_score:
        high_score=score

def welcoming_screen():
    print("""
##############################
 Welcome in game Higher Lower
##############################     
""")
    print(f"         High score: {high_score}")
    Q=input("If you wanna play push ENTER if you wanna leave write END. ").lower()
    if Q=="end":
        quit()
    main()
def extract(name,description,country,type): 
    print(f"Type {type}:{name},{description},{country}")
def answ_cal():
    if first_data["follower_count"] > second_data["follower_count"]:
        return "less"
    else:
        return "more"
def evaluation():
    if guess==answ:
        return 1
    else:
        return 2
    
def main():
    global first_data,second_data,guess,answ,posib,score
    print(f"Score:{score}")
    first_data=random.choice(data)
    second_data=random.choice(data)

    if first_data==second_data:
        while first_data==second_data:
            second_data=random.choice(data)


    extract(first_data["name"],first_data["description"],first_data["country"],"A")
    extract(second_data["name"],second_data["description"],second_data["country"],"B")

    guess=input("Do you think that has B more or less followers. more/less: ").lower()
    answ=answ_cal()
    posib=evaluation()
    if posib==1:
        print(f"Corectly {guess}")
        score+=1
    else:
        print("It's not corectly")
        print(f"Corectly is {answ}")

    print(f"Type A followers: {first_data["follower_count"]}")
    print(f"Type B followers: {second_data["follower_count"]}")
    time.sleep(3)
    middle_screen()

def middle_screen():
    if posib==1:
        print("Well done you are continuing")
        high_score_evaluation()
        print(f"Score: {score}")
        time.sleep(3)
        os.system('clear')
        main()
    else:
        print("""
              __________________
              YAAAAAY You failed
              __________________
              """)
        print(f"Score: {score}")
        time.sleep(3)
        os.system('clear')
        welcoming_screen()
welcoming_screen()