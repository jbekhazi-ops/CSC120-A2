class Computer:
    # this class needs to : store information about a specific computer, update a computer's price and its OS.
    
    # These are all the attributes that it needs (basically all the specs disbribing the computer)
    description: str = ""
    processor_type: str = ""
    hard_drive_capacity: int = 0
    memory: int = 0
    operating_system: str = ""
    year_made: int = 0
    price: int = 0

    def __init__(self, desc: str, type:str, cap: int, memo: int ,os: str, year: int, price:int):
        #this is the constructor, helps us initialize every attribute and store information about computer 
        self.description = desc
        self.processor_type = type
        self.hard_drive_capacity = cap
        self.memory = memo
        self.operating_system = os
        self.year_made = year
        self.price = price

    # methods:
    def update_price(self, price: int):
        #this method helps update the price of a computer
        # The first argument is self to refer to the instance of the class
        # The second argument is the new price we are giving our price attribute 
        self.price = price 
        return ("Price updated")
    
    def update_os(self, os:str):
        #this method helps update the OS of a computer
        # The first argument is self to refer to the instance of the class
        # The second argument is the new OS we are giving our operating_system attribute 
        self.operating_system = os
        return ("OS updated")


