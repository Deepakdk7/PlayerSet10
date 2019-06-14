ax=int(input())
a=list(map(int,input().split()))
c=0
b=[]
for i in range(0,ax):
    c=c+a[i]
    b.append(c)
print(*b[::-1])
