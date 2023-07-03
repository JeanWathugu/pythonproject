leapyear=int(input("Enter the leap year"))

if leapyear%4==0 and leapyear %100!= 0 or leapyear%400==0:
    print("This is a leap year")
else:
    print("This is not a leap year")
 #write a python program to calculate the ticket price for a movie theatre based on the age of the customer;
 #0-5 yrs=free  6-12yrs=500  13-17 yrs=1000  18+yrs=1500