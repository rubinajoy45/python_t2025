a=int(input())
if(a%2==1):
    for i in range(1,a+1):
        for j in range(1,a+1):
            if(i==(a//2)+1 and j==(a//2)+1):
                print("0",end="")
            else:
                print("1",end="")
        print()
else:
    b=a//2
    for i in range(1,a+1):
        for j in range(1,a+1):
            if(b==i and b==j or (b==i and b+1==j) or (b+1==i and b==j) or (b+1==i and b+1==j)):
                print("0",end="")
            else:
                print("1",end="")
        print()