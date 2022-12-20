n=int(input("Enter a year"))
if(n%4==0 or n%400==0 and n%100!=0):
    print("The given year is a leap year")
else:
    print("the given year is not a leap year")