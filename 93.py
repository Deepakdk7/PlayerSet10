ax=int(input())
a=list(map(int,input().split()))
if ax%2==0:
    for  i in range(0,len(a)-1):
        if i%2==0:
            t=a[i]
            a[i]=a[i+1]
            a[i+1]=t
else:
    for i in range(0,len(a)-2):
        if i%2==0:
            t=a[i]
            a[i]=a[i+1]
            a[i+1]=t
print(*a)
