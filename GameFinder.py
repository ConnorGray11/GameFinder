#!/usr/bin/python3
# GameFinder.py
# Connor Gray
# 1/27/2020

"""this program is used to organize a game library of sorts"""
import pickle

def edit():
    print("hey there, sorry there nothing here yet, thanks for checking out my program,this one will add stuff")
    
def show_all():
   # print("hey there, sorry there nothing here yet, thanks for checking out my program, this one will show all")
    key_list = games.keys()
    for key in key_list:
        print()
        print("Game : ", key)
        print("Genre: ",games[key][0])
        print("Title: ", games[key][1])
        print("Developer: ", games[key][2])
        print("Publisher: ", games[key][3])
        print("System: ", games[key][4])
        print("Release Date: ", games[key][5])
        print("Personal Rating: ", games[key][6])
        print("Single or Multiplayer: ", games[key][7])
        print("Price: ", games[key][8])
        print("Beaten Campaign: ", games[key][9])
        print("Purchase Date: ", games[key][10])
        print("Notes on Game: ", games[key][11])
        print("----------------------")
def search():
    print("")
    key_list = games.keys()
    print("""
    Welcome to The GameFinder™ Program
    ---------------------------
    
    Search by
    G) Genre
    T) Title
    D) Developer
    P) Publisher
    S) System
    R) Release
    Ra) Rating
    M) Multi or single
    Pr) Price
    Be) Beaten
    PD) Purchase date
    B) Back
    
    """) 
    search_choice = input("what would you like to search today: ")
    if search_choice == "G" or search_choice == "g":
        genre()
        
    elif search_choice == "T" or search_choice == "t":
        title()
            
    elif search_choice == "D" or search_choice == "d":
        dev()
            
    elif search_choice == "P" or search_choice == "p":
        pub()
           
    elif search_choice == "S" or search_choice == "s":
        system()
   
    elif search_choice == "R" or search_choice == "r":
        release()
            
    elif search_choice == "Ra" or search_choice == "ra":
        rating()
    
    elif search_choice == "M" or search_choice == "m":
        multi()
            
    elif search_choice == "Pr" or search_choice == "pr":
        price()
    
    elif search_choice == "Be" or search_choice == "be":
        beaten()
            
    elif search_choice == "PD" or search_choice == "pd":
        purchase_date()
            
    elif search_choice == "B" or search_choice == "b":
        back()
        
    else:
        print("wrong choice pal, theres nothing here")

def remove():
    print("hey there, sorry there nothing here yet, thanks for checking out my program, this will remove stuff")
    
def save_data():
    #print("hey there, sorry there nothing here yet, thanks for checking out my program, this will save the data")
    pickle_file = open("game_lib.pickle", "wb")
    pickle.dump(games, pickle_file)
    pickle_file.close()   
    print("congrats it saved all your changes")
    
#these are search term def
def genre():
    found_one = False
    genre = input("  What is the Genre of the game you are looking for? ")
    for key in games.keys():
        if genre == games[key][0]:
            found_one = True
            print("Game : ", key)
            print("Genre: ",games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("System: ", games[key][4])
            print("Release Date: ", games[key][5])
            print("Personal Rating: ", games[key][6])
            print("Single or Multiplayer: ", games[key][7])
            print("Price: ", games[key][8])
            print("Beaten Campaign: ", games[key][9])
            print("Purchase Date: ", games[key][10])
            print("Notes on Game: ", games[key][11])
            print("----------------------")
def title():
    found_one = False
    title = input("  What is the title of the game you are looking for? ")
    for key in games.keys():
        if title == games[key][1]:
            print("Game : ", key)
            print("Genre: ",games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("System: ", games[key][4])
            print("Release Date: ", games[key][5])
            print("Personal Rating: ", games[key][6])
            print("Single or Multiplayer: ", games[key][7])
            print("Price: ", games[key][8])
            print("Beaten Campaign: ", games[key][9])
            print("Purchase Date: ", games[key][10])
            print("Notes on Game: ", games[key][11])
            print("----------------------")
def dev():
    found_one = False
    dev = input("  What is the Developer of the game you are looking for? ")
    for key in games.keys():
        if dev == games[key][2]:
            found_one = True
            print("Game : ", key)
            print("Genre: ",games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("System: ", games[key][4])
            print("Release Date: ", games[key][5])
            print("Personal Rating: ", games[key][6])
            print("Single or Multiplayer: ", games[key][7])
            print("Price: ", games[key][8])
            print("Beaten Campaign: ", games[key][9])
            print("Purchase Date: ", games[key][10])
            print("Notes on Game: ", games[key][11])
            print("----------------------")
            
def pub():
    found_one = False
    pub = input("  What is the Publisher of the game you are looking for? ")
    for key in games.keys():
        if pub == games[key][3]:
            found_one = True
            print("Game : ", key)
            print("Genre: ",games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("System: ", games[key][4])
            print("Release Date: ", games[key][5])
            print("Personal Rating: ", games[key][6])
            print("Single or Multiplayer: ", games[key][7])
            print("Price: ", games[key][8])
            print("Beaten Campaign: ", games[key][9])
            print("Purchase Date: ", games[key][10])
            print("Notes on Game: ", games[key][11])
            print("----------------------")
            
def system():
    found_one = False
    sytstem = input("  What is the system your game is on? ")
    for key in games.keys():
        if genre == games[key][4]:
            found_one = True
            print("Game : ", key)
            print("Genre: ",games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("System: ", games[key][4])
            print("Release Date: ", games[key][5])
            print("Personal Rating: ", games[key][6])
            print("Single or Multiplayer: ", games[key][7])
            print("Price: ", games[key][8])
            print("Beaten Campaign: ", games[key][9])
            print("Purchase Date: ", games[key][10])
            print("Notes on Game: ", games[key][11])
            print("----------------------")
            
def release():
    found_one = False
    release = input("  What is the release date of the game you are looking for? ")
    for key in games.keys():
        if release == games[key][5]:
            found_one = True
            print("Game : ", key)
            print("Genre: ",games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("System: ", games[key][4])
            print("Release Date: ", games[key][5])
            print("Personal Rating: ", games[key][6])
            print("Single or Multiplayer: ", games[key][7])
            print("Price: ", games[key][8])
            print("Beaten Campaign: ", games[key][9])
            print("Purchase Date: ", games[key][10])
            print("Notes on Game: ", games[key][11])
            print("----------------------")
            
def rating():
    found_one = False
    rating = input("  What is the rating of the game you're looking for? ")
    for key in games.keys():
        if rating == games[key][6]:
            found_one = True
        print("Game : ", key)
        print("Genre: ",games[key][0])
        print("Title: ", games[key][1])
        print("Developer: ", games[key][2])
        print("Publisher: ", games[key][3])
        print("System: ", games[key][4])
        print("Release Date: ", games[key][5])
        print("Personal Rating: ", games[key][6])
        print("Single or Multiplayer: ", games[key][7])
        print("Price: ", games[key][8])
        print("Beaten Campaign: ", games[key][9])
        print("Purchase Date: ", games[key][10])
        print("Notes on Game: ", games[key][11])
        print("----------------------") 
            
def multi():
    found_one = False
    multi = input("  Would you like to search for Multiplayer singleplayer or either? ")
    for key in games.keys():
        if multi == games[key][7]:
            found_one = True
            print("Game : ", key)
            print("Genre: ",games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("System: ", games[key][4])
            print("Release Date: ", games[key][5])
            print("Personal Rating: ", games[key][6])
            print("Single or Multiplayer: ", games[key][7])
            print("Price: ", games[key][8])
            print("Beaten Campaign: ", games[key][9])
            print("Purchase Date: ", games[key][10])
            print("Notes on Game: ", games[key][11])
            print("----------------------")
            
def price():
    found_one = False
    price = input("  How much did it cost? ")
    for key in games.keys():
        if price == games[key][8]:
            found_one = True
            print("Game : ", key)
            print("Genre: ",games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("System: ", games[key][4])
            print("Release Date: ", games[key][5])
            print("Personal Rating: ", games[key][6])
            print("Single or Multiplayer: ", games[key][7])
            print("Price: ", games[key][8])
            print("Beaten Campaign: ", games[key][9])
            print("Purchase Date: ", games[key][10])
            print("Notes on Game: ", games[key][11])
            print("----------------------")
            
def beaten():
    found_one = False
    beaten = input("  Have you beaten the game? ")
    for key in games.keys():
        if beaten == games[key][9]:
            found_one = True
            print("Game : ", key)
            print("Genre: ",games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("System: ", games[key][4])
            print("Release Date: ", games[key][5])
            print("Personal Rating: ", games[key][6])
            print("Single or Multiplayer: ", games[key][7])
            print("Price: ", games[key][8])
            print("Beaten Campaign: ", games[key][9])
            print("Purchase Date: ", games[key][10])
            print("Notes on Game: ", games[key][11])
            print("----------------------")
            
def purchase_date():
    found_one = False
    purchase_date = input("  When did you purchase the game? ")
    for key in games.keys():
        if purchase_date == games[key][10]:
            found_one = True
        print("Game : ", key)
        print("Genre: ",games[key][0])
        print("Title: ", games[key][1])
        print("Developer: ", games[key][2])
        print("Publisher: ", games[key][3])
        print("System: ", games[key][4])
        print("Release Date: ", games[key][5])
        print("Personal Rating: ", games[key][6])
        print("Single or Multiplayer: ", games[key][7])
        print("Price: ", games[key][8])
        print("Beaten Campaign: ", games[key][9])
        print("Purchase Date: ", games[key][10])
        print("Notes on Game: ", games[key][11])
        print("----------------------")  
        
def back():
    search = False

    

pickle_file = open("game_lib.pickle", "rb")
games = pickle.load(pickle_file)
pickle_file.close()

keep_going = True

while keep_going:
    print("""
    Welcome to The GameFinder™ Program
    ---------------------------
    
    MAIN MENU
    1) Add/Edit Game
    2) Print All Games
    3) Search
    4) Remove a Game
    5) Save Current Database
    
    Q) Quit
    
    """)
    
    choice = input("What would you like to do? ")
    if choice == "1":
        edit()
        
    elif choice == "2":
        show_all()
        
    elif choice == "3":
        search()

        
    elif choice == "4":
        remove()
        
    elif choice == "5":
        save_data()

    elif choice == "Q" or choice == "q":
        print("yeah i get it, theres nothin here yet, come back soon.") 
        quit()
        keep_going = False
       
    else:
        print("*** NOT A VALID CHOICE ***\n")


                            
                                                          
                    
        
