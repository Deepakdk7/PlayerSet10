ax=int(input())
a=list(map(int,input().split()))
a.sort()
c=0
for i in range(1,len(a)):
    c=c+a[i]
print(c)
