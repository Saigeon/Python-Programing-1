#! /user/bin/env python3
import db
from business import Item, Shelf
from datetime import date, datetime

def add_item(itemList):
    itemID = 0
    itemName = input("Food Name:")
    itemEnd = input("Expiration Date (YYYY-MM-DD):")
    dateFormat = "%Y-%m-%d"
    now = datetime.now()
    currentDate = datetime(now.year, now.month, now.day)
    itemStart = currentDate.strftime(dateFormat)

    item = Item(itemID, itemName, itemEnd, itemStart)
    itemList.add(item)
    db.save_item(item)
    print(f"{item.itemName} added to fridge.\n")

def trash_item(itemList):
    number = int(input("Item Number:"))
    item = itemList.remove(number)
    db.delete_item(item)
    print(f"{item.itemName} was trashed.\n")

def print_line(length):
    print("-"*length)
    
def display_shelf(itemList):
    print("\tFood\tExpiration\tAdded")
    print_line(50)
    for item in itemList:
        print(f"{item.itemID}\t{item.itemName}\t{item.itemEnd}\t{item.itemStart}\n")

def display_menu():
    print_line(50)
    print("\tDigital Fridge")
    print("Options:")
    print("1. Look in Fridge")
    print("2. Add Food")
    print("3. Trash Food")
    print("4. Exit program\n")
    print_line(50)

def main():
    display_menu()
    
    db.connect()
    itemList = db.get_items()
    if itemList == None:
        itemList = Shelf()
        
    while True:
        option = int(input("Select Option: "))
        if option == 1:
            display_shelf(itemList)
        elif option == 2:
            add_item(itemList)
            itemList = db.get_items()
        elif option == 3:
            trash_item(itemList)
        elif option == 4:
            print("You close the fridge, for now.")
            break
        else:
            print
            display_menu()

main()
            
    

