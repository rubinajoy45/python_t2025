a=int(input())
if(a%2==1):
    for i in range(1,a+1):
        for j in range(1,a+1):
            if(i==(a//2)+1 or j==(a//2)+1):
                print("0",end="")
            else:
                print("1",end="")
        print()
else:
    for i in range(1,a+1):
        for j in range(1,a+1):
            if(i==(a/2)+1 or j==(a/2)+1 or i==a/2 or j==a/2):
                print("0",end="")
            else:
                print("1",end="")
        print()