x,y=map(int.input().split())
if(x%2==0 and y%2==0):
    print("EVEN")
elif(x%2!=0 and y%2!=0):
    print("ODD")
else:
    print("MIXED")