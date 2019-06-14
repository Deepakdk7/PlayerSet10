ax=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,ax-1):
    c=c+(a[i]+a[i+1])
print(c)
