ax=input().split()
a=list(ax[0])
b=list(ax[1])
c=[]
for i in range(0,len(ax[1])):
    c.append(a[i])
d=c+b
for i in d:
    print(i,end="")
