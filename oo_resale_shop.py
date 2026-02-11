from computer import *

class ResaleShop:
    # this class needs to: keep track of the store's inventory, sell a computer , buy a computer , and refurbish a computer
    # The only attribute ResaleShop needs is an inventory to store all of its computers
    inventory = []

    def __init__(self, inv:list):
        #The constructor innitializes the Resale Shop's inventory, the inventory type is a list since we are listing a bunch of computers
        self.inventory = inv

    def buy(self, comp:Computer):
        #This first method needed in the ResaleShop is a function that allows us to add a computer to a Resale Shop's inventory
        #The first argument is self because I am adding computers to our attribute: the inventory
        #The second argument is of the type Computer which is the class created in computer.py
        self.inventory.append(comp)
        print("Computer added to inventory")

    def sell(self, comp:Computer):
        #The second method is to remove a computer from a Resale Shop's inventory
        #I used the same arguments as the buy method (same reasoning)
        # if statement is used to check if the instance of our Computer class is in the inventory
        # and then .remove removes computer from list, if computer not found we print not found.
        if comp in self.inventory:
            self.inventory.remove(comp)
            print("Computer removed from inventory")
        else: 
            print("Computer not found. Please select another item to sell.")
    
    def print_inventory(self):
        # This function is needed because if we were to run in main this command: 
        # print(myResaleShop.inventory)   # the program would then return:
        # >>>>[<computer.Computer object at 0x1008e8a50>]
        # Which means we need to find a different way to retreive information about our computer object
        # Which is why this function is necessary to print the ResaleShop's inventory
        if self.inventory:  # If the inventory is not empty
            # For each item
            for item in self.inventory:   # For each item Print its details
                print(f'{item.description} -- Processor Type: {item.processor_type}, Hard Drive Capacity: {item.hard_drive_capacity}, Memory: {item.memory}, Operating System: {item.operating_system}, Year Made: {item.year_made}, Price:  {item.price}')
        else:
            print("No inventory to display.")

    def refurbish(self, computer: Computer, new_os: str):
        #This function takes in 3 arguments, so when running it in main we need to make sure we passed both a Computer and a string or None
        #This function looks at a computer instance and then goes through a series of IF statements to then make the adequate refurbish 
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

def main(): #test if code is working 
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

       
