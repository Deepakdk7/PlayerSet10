ax=int(input())
a=list(map(int,input().split()))
c=0
b=[]
for i in range(0,ax):
    c=c+a[i]
    b.append(c)
d=b[::-1]
for i in range(0,ax):
    if ax>1:
        print(b[i]+d[i],'',end='')
    else:
        print(b[i])
