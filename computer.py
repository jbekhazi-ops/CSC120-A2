class Computer:
    # What attributes will it need?
    description: str = ""
    processor_type: str = ""
    hard_drive_capacity: int = 0
    memory: int = 0
    operating_system: str = ""
    year_made: int = 0
    price: int = 0

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, desc: str, type:str, cap: int, memo: int ,os: str, year: int, price:int):
        self.description = desc
        self.processor_type = type
        self.hard_drive_capacity = cap
        self.memory = memo
        self.operating_system = os
        self.year_made = year
        self.price = price

    # What methods will you need?

    def update_price(self, price: int):
        self.price = price 
        return ("Price updated")
    
    def update_os(self, os:str):
        self.operating_system = os
        return ("OS updated")



    # this file needs to :
    # store information about a specific computer (which operating system does it have, whats the cost etc), 
    # update a computer's price 
    # and OS,

