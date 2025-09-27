n=int(input())
n=n*2-1
for row in range(1,n+1):
    for col in range(1,n+1):
        if(row+col==n+1 or row==1 or row==n or col==1 or col==n or row==col):
            print("*",end="")
        else:
            print(" ",end="")
    print()