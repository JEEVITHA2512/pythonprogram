ch1,ch2,ch3=map(str,input().split())
if((ch1!=ch3)and(ch1==ch2)or(ch1==ch3)):
    print("SAME")
else:
    print("DIFFERENT")