a=input()
count=0
for i in a:
    if(count==-1):
        break
    if(i=="("):
        count=count+1
    elif(i==")"):
        count=count-1
if(count==0):
    print("Balanced")
elif(count==-1):
    print("Unbalanced")
else:
    print("Unbalanced")