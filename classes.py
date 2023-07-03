class Magari:
    def __init__(self, model, colour, year, tyre ):
        self.model=model
        self.mycolour=colour
        self.myyear =year
        self.mytyre= tyre
    def onyesha(self):
        print(self.model, self.mycolour, self.myyear, self.mytyre)

#create an object

myobj=Magari("Jeep", "Pink", 2023, "Black")
myobj.onyesha()

myobj=Magari("Ferrari", "Red", 1950, "Black")
myobj.onyesha()