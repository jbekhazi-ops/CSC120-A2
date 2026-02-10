"""
   Filename: procedural_resale_shop.py
Description: an example of procedural code to run a small computer resale shop,
             part of A2: Object-ification, CSC120: Object-Oriented Programming
             as taught at Smith College in Spring 2025. Based on an example by Sami Islam.
     Author: R. Jordan Crouser (@jcrouser)
       Date: 1 February 2024
     Edited: Ab Mosca 25 September 2025
       
       Note: YOU DO NOT NEED TO MODIFY THIS FILE
"""
# Import a few useful containers from the typing module
from typing import Dict, Optional

""" inventory: a list where we'll store our inventory """
inventory : list = []

"""
Takes in a Dict containing all the information about a computer,
adds it to the inventory
"""
def buy(computer: Dict):
    inventory.append(computer)

"""
Takes in a Dict containing all the information about a computer 
and a new price, updates the price of the computer if it is the inventory, 
prints error message otherwise
"""
def update_price(computer: Dict, new_price: int):
    if computer in inventory:
        computer["price"] = new_price
    else:
        print("Computer not found. Cannot update price.")

"""
Takes in an item_id, removes the associated computer if it is the inventory, 
prints error message otherwise
"""
def sell(computer: Dict):
    if computer in inventory:
        inventory.remove(computer)
    else: 
        print("Computer not found. Please select another item to sell.")

# """
# prints all the items in the inventory (if it isn't empty), prints error otherwise
# """
def print_inventory():
    # If the inventory is not empty
    if inventory:
        # For each item
        for item in inventory:
            # Print its details
            print(f'{item["description"]} -- Processor Type: {item["processor_type"]} Hard Drive Capacity: {item["hard_drive_capacity"]} Memory: {item["memory"]} Operating System: {item["operating_system"]} Year Made: {item["year_made"]} Price:  {item["price"]}')
    else:
        print("No inventory to display.")

def refurbish(computer: Dict, new_os: Optional[str] = None):
    if computer in inventory:
        if int(computer["year_made"]) < 2000:
            computer["price"] = 0 # too old to sell, donation only
        elif int(computer["year_made"]) < 2012:
            computer["price"] = 250 # heavily-discounted price on machines 10+ years old
        elif int(computer["year_made"]) < 2018:
            computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
        else:
            computer["price"] = 1000 # recent stuff

        if new_os is not None:
            computer["operating_system"] = new_os # update details after installing new OS
    else:
        print("Computer not found. Please select another item to refurbish.")

def main():
    myComputer = {"description":"2019 MacBook Pro", "processor_type":"Intel", "hard_drive_capacity":256, "memory":16, "operating_system":"Sequoia", "year_made":2019, "price":1000}
    otherComputer = {"description":"2000 MacBook Air", "processor_type":"Intel", "hard_drive_capacity":256, "memory":16, "operating_system":"High Sierra", "year_made":2010, "price":500}
    buy(myComputer)
    buy(otherComputer)
    print_inventory()


if __name__ == "__main__": 
    main()