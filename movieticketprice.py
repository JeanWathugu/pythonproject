age=int(input("Enter your age"))

if age>=0 and age<=5:
    print("Your ticket is free")

elif age>=6 and age<=12:
    print("Your ticket is 500")

elif age>=13 and age<=17:
    print("Your ticket price is 1000")

elif age>=18:
    print("Your ticket price is 1500")
elif age<0:
    print("Invalid age")

