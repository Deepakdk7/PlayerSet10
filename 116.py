ax=int(input())
a=input().split()
b=[]
c=[]
d=[]
e=[]
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    c.append(i)
    c.append(a.count(i))
    d.append(a.count(i))
d.sort()
for i in range(0,len(d)):
    for j in range(0,len(c)):
        if d[i]==c[j] and c[j-1] not in e:
            e.append(c[j-1])
e=e[::-1]
print(*e,sep=' ')
