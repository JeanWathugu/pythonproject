class People:
    def __init__(self, Name, Gender, Age):
        self.name=Name
        self.gender=Gender
        self.age=Age

    def printing(self):
        print(self.name, self.gender, self.age)

myobj=People("Sharleen", "Female", 18)
myobj.printing()

myobj=People("Ndanu", "Female", 18)
myobj.printing()

myobj=People("Charles", "Male", 19 )
myobj.printing()

myobj= People("MJ", "Female", 18)
myobj.printing()