ax = int(input())
a = list(map(int,input().split()))
a = sorted(a)
c = []
i = 0
j = ax//4
for i in range(0,j) :
    c.append(a[i])
    c.append(a[-i-1])
if ax%2==1 :
    c.append(a[ax//2])
    for i in range(j,ax//2) :
        c.append(a[-i-1])
        c.append(a[i])
else :
    for i in range(j,ax//2) :
        c.append(a[-i-1])
        c.append(a[i])
s = 0
for i in range(0,ax-1) :
    a = max(c[i],c[i+1])
    s += a
print(s)
