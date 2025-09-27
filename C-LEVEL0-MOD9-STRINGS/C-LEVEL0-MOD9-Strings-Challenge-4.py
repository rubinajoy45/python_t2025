a=input()
word=''
for i in a:
    if(i in "aeiou"):
        word=word+' '
    else:
        word=word+i
print(word)