ax=list(input())
bx=ax[::-1]
a=0
for i in bx:
    print(i,end="")
    a=a+1
    if a<len(ax):
        print('-',end='')
