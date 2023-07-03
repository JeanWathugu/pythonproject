class Animal:
    def __init__(self, name, color):
        self.name=name
        self.color=color

    def speak(self):
        raise NotImplementedError("Child class must implement this")


class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

class Horse(Animal):
    def speak(self):
        return "Neigh"

dog=Dog("Bolt", "brown")
print(dog.name)
print(dog.speak())

cat=Cat("Kitkat", "Brown")
print(cat.name)
print(cat.speak())

horse= Horse("Whitney", "Black")
print(horse.name)
print(horse.color)
print(horse.speak())