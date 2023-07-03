#list data structures, it is ordered and changeable

cars= ["Peugeout","Mercedes Benz", "Nissan", "Toyota", "Jeep"]
print(cars)

cars[1]= "Subaru"
print(cars)

cars.append("Mitsubishi")
print(cars)

cars.insert(3, "Ford")
print(cars)

cars.pop(4)
print(cars)

cars.sort()
print(cars)

cars.copy()
print(cars)



#this is a tuple, ordered and unchangeable
fruits=("Pineapple","Banana","Apples","Grape")
for x in fruits:
    print(x)

    #A set is unordered
countries={"Kenya", "Germany", "Tanzania", "Mozambique", "Rwanda"}
print(countries)

#dictionaries are

Jean = {"Age: 18  "
        "Class:Safari  "
        "Height: 5 foot 4  "
        "Eye colour:Brown  "}
print(Jean)
Jean.pop()
