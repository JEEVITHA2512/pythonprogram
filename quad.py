import math
def quad(a,b,c):
    d= (b**2-4*a*c)
    sqrt_val=math.sqrt(abs(d))
    if d > 0: 
        print(" real and different roots ") 
        print((-b + sqrt_val)/(2 * a)) 
        print((-b - sqrt_val)/(2 * a)) 
      
    elif d == 0: 
        print(" real and same roots") 
        print(-b / (2 * a)) 
      
    else:
        print("Complex Roots") 
        print(- b / (2 * a), " + i", sqrt_val) 
        print(- b / (2 * a), " - i", sqrt_val) 
#drivercode
a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
if(a==0):
    print("Incorrect equation")
else:
    quad(a,b,c)