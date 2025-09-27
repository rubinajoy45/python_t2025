a=int(input())
for i in range(1,a+1):
    for j in range(1,a+1):
        if(i==1 or i==a or j==1 or j==a or i==j or i+j==a+1):
                print("1",end="")
        else:
                print("0",end="")
    print()