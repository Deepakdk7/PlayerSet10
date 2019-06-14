a,b=list(map(int,input().split()))
ax=list(map(int,input().split()))
c=[]
for i in range(0,a):
    for j in range(a,len(ax)):
        if ax[i]==ax[j] and ax[i] not in range(i+1,a):
            c.append(ax[i])
c.sort()
print(*c)
