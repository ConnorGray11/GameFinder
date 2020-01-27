#!/usr/bin/python3
# GameFinder.py
# Connor Gray
# 1/27/2020

"""this program is used to organize a game library of sorts"""
import pickle

def edit():
    print("hey there, sorry there nothing here yet, thanks for checking out my program,this one will add stuff")
def show_all():
    print("hey there, sorry there nothing here yet, thanks for checking out my program, this one will show all")
def title_search():
    print("hey there, sorry there nothing here yet, thanks for checking out my program, this one will search titles")
def remove():
    print("hey there, sorry there nothing here yet, thanks for checking out my program, this will remove stuff")
def save_data():
    print("hey there, sorry there nothing here yet, thanks for checking out my program, this will save the data")

keep_going = True

while keep_going:
    print("""
    Welcome to The GameFinder™ Program
    ---------------------------
    
    MAIN MENU
    1) Add/Edit Game
    2) Print All Games
    3) Search by Title
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
        title_search()
        
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
        
