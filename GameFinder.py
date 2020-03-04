#!/usr/bin/python3
# GameFinder.py        self.genre_var = BooleanVar(self)       self.tkvar.set(self.games[0])
# Connor Gray
# 1/27/2020

"""this program is used to organize a game library of sorts"""
import pickle

def add():
    new_key = len(games) + 1
    entry = []
    valid = False
    while not valid:
        entry.append(input("What is the game Genre: "))
        entry.append(input("What is the Title of the Game: "))
        entry.append(input("What is the Developer of the game: "))
        entry.append(input("What is the Publisher of the game: "))
        entry.append(input("What System is the game on: "))
        entry.append(input("What year did the game release: "))
        entry.append(input("What is your personal rating of the game: "))
        entry.append(input("Is the game multiplayer singleplayer or either: "))
        entry.append(input("How much did you pay for it: "))
        entry.append(input("Have you beaten the game: "))
        entry.append(input("When did you buy the game(MM/DD/YYYY: "))
        entry.append(input("Any notes on the game: "))
        answer = input("is this correct?: ")
        if answer in ("Yes","Y","yes","y"):
            valid = True
    
    games[new_key] = entry
        
def edit():
    key_list = games.keys()
    valid = False
    for key in key_list:
        print("")
        print("Current Games: ", games[key][0]+ ", " +games[key][1])   
    
    game = int(input("What game would you like to edit: "))
    if game in games:
        print("this is stupid")
        answer = input("is this correct?: ")
        if answer in ("Yes","Y","yes","y"):
            valid = True        




def edit_new():
    keys = games.keys()
    valid = False
    while not valid:
        for key in keys: 
            print(key, games[key][1])
        change = int(input("which number game would you like to edit? "))
        editing = games[change]
        
        print("Current Genre: ", editing[0])
        editing[0] = input("New genre: ")
        
        print("Current Title: ", editing[1])
        editing[1] = input("New genre: ")
        
        print("Current Developer: ", editing[2])
        editing[2] = input("New Developer: ")
        
        print("Current Publisher: ", editing[3])
        editing[3] = input("New Publisher: ")
        
        print("Current System: ", editing[4])
        editing[4] = input("New System: ")
        
        print("Current Release Date: ", editing[5])
        editing[5] = input("New Release Date: ")
        
        print("Current Personal Rating: ", editing[6])
        editing[6] = input("New Rating: ")
        
        print("Current SP/MP/Either : ", editing[7])
        editing[7] = input("New SP/MP/Either: ")
        
        print("Current Price: ", editing[8])
        editing[8] = input("New Price: ")
        
        print("Current Game Beaten Status: ", editing[9])
        editing[9] = input("New Game Beaten Status: ")
        
        print("Current Purchase Date: ", editing[10])
        editing[10] = input("New Purchase Date: ")
        
        print("Current Notes on game: ", editing[11])
        editing[11] = input("New notes on game: ")
        
        answer = input("is this correct?: ")
        if answer in ("Yes","Y","yes","y"):        
            valid = True  

    games[change] = editing

    
   

    #input("what is the name of the game you'd like to edit? ")
    
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
    #print("hey there, sorry there nothing here yet, thanks for checking out my program, this will remove stuff")
    keys = games.keys()
    valid = False
    while not valid:
        for key in keys: 
            print(key, games[key][1])
        delete = int(input("which  game would you like to Remove? "))
        if delete in games:
            for key in range(1,len(games)+1):
                if key >= delete and key != len(games):
                    print("copied!")
                    games[key] = games[key + 1]
                if key == len(games):
                    games.pop(key)
                valid = True
                
            #games.pop(delete)
            
        else:
            print("ENTRY DOESNT EXIST")
            valid = True
        
        

    
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
    1) Add Game
    2) Edit Game
    3) Print All Games
    4) Search
    5) Remove a Game
    6) Save Current Database
    
    Q) Quit
    
    """)
    
    choice = input("What would you like to do? ")
    if choice == "1":
        add()
        
    elif choice == "2":
        edit_new()
           
    elif choice == "3":
        show_all()
        
    elif choice == "4":
        search()
        search = True

        
    elif choice == "5":
        remove()
        
    elif choice == "6":
        save_data()

    elif choice == "Q" or choice == "q":
        option = input("Would you like to save your changes?(Y/N): ")
        if option == "Y":
            print("Saving and exiting the program, have a nice day")
            pickle_file = open("game_lib.pickle", "wb")
            pickle.dump(games, pickle_file)
            pickle_file.close()          
            quit()
            keep_going = False
        else:
            print("quiting without saving")
            quit()
            keep_going = False            
       
    else:
        print("*** NOT A VALID CHOICE ***\n")
        



                            
                                                          
                    
        
