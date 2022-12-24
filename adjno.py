#x,y = map(int, input().split())
a=input()
lis=a.split(" ")
int_lis = [int(each) for each in lis]
print(int_lis[0])
print(int_lis[1])
if(int_lis[0]>40 and int_lis[1]>40):
    print("pass")
else:
    print("fail,need to improve")

# you will get to give the x and y value adjacently and then the program goes on
#ValueError: not enough values to unpack (expected 2, got 0)-x,y = map(int, input().split())
#to overcome this error we will use lists and sublists
