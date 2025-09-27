n=int(input())
val = 1
for row in range (1,n+1):
    if(row%2==0):
        val=2
    else:
        val=1
    for col in range(1,row+1):
        print(val,end="")
        val=val+2
    print()