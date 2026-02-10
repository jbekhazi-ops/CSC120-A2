from computer import *

class ResaleShop:
    # What attributes will it need? 
    inventory = []

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inv:list):
        self.inventory = inv

    # What methods will you need?
    def buy(self, comp:Computer):
        # call Computer(...) constructor , to create a new computer instance 
        # call inventory.append(...) to add the new computer instance to the inventory 
        self.inventory.append(comp)
        print("Computer added to inventory")

    def sell(self, comp:Computer):
        if comp in self.inventory:
            self.inventory.remove(comp)
            print("Computer removed from inventory")
        else: 
            print("Computer not found. Please select another item to sell.")
    
    def print_inventory(self):
    # If the inventory is not empty
        if self.inventory:
            # For each item
            for item in self.inventory:
                # Print its details
                print(f'{item.description} -- Processor Type: {item.processor_type}, Hard Drive Capacity: {item.hard_drive_capacity}, Memory: {item.memory}, Operating System: {item.operating_system}, Year Made: {item.year_made}, Price:  {item.price}')
        else:
            print("No inventory to display.")

    def refurbish(self, computer: Computer, new_os: str):
        if computer in self.inventory:
            if int(computer.year_made) < 2000:
                computer.update_price(0) # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.update_price(250) # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.update_price(550) # discounted price on machines 4-to-10 year old machines
            else:
                computer.update_price(1000) # recent stuff

            if new_os is not None:
                computer.update_os(new_os) # update details after installing new OS
        else:
            print("Computer not found. Please select another item to refurbish.")

def main():
    print("Hello!")
    newList = []
    myResaleShop  : ResaleShop = ResaleShop(newList)
    print(myResaleShop.inventory)
    myComputer : Computer =  Computer("2019 MacBook Pro", "Intel", 256, 16, "Sequoia", 2019, 1000)
    otherComputer : Computer =  Computer("2000 MacBook Air", "Intel", 256, 16, "High Sierra", 2010, 500)
    myResaleShop.buy(myComputer)
    myResaleShop.buy(otherComputer)
    myResaleShop.refurbish(otherComputer, None)
    myResaleShop.print_inventory()
    myResaleShop.sell(myComputer)
    myResaleShop.print_inventory()



if __name__ == "__main__":
    main()

       
#### this file needs to :
    # keep track of the store's inventor (list of individual computer instances, create lots of computer from our computer blueprint and put them in the resale shop inventory ), 
    # buying a computer
    # selling a computer
    # refurbishing a computer

