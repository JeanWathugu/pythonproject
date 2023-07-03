class vehicles:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def printout(self):
        print(f"This vehicle was made by ", {self.brand}, " in the year ", {self.year})

class motorbike(vehicles):
    def __init__(self, brand, year, color):
        super().__init__(brand, year)
        self.color = color

    def color (self):
        print(f"The motorbike is ", {self.color}, " in color.")

class ship(vehicles) :
    def __init__(self, brand, year, capacity):
        super().__init__(brand, year)
        self.capacity = capacity

    def capacity(self):
        print(f"The capacity of this ship has a capacity of ", {self.capacity})

class cars(vehicles):
    def __init__(self, brand, year, top):
       super().__init__(brand, year)
       self.top = top

    def top(self):
        print("This car has a {self.top}  roof.")

motorbike= motorbike("BMW", 1970, "Ruby")
print(motorbike.brand,motorbike.year)
print(motorbike.color)

ship=ship ("Ford", 1950, "Navy blue")
print(ship.brand, ship.year)
print(ship.capacity)

cars=cars ("Peugeuot", 2010, "Convertible")
print(cars.brand,cars.year)
print(cars.top)



