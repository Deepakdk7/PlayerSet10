ax=input().split()
k=int(ax[1])
c=0
a=list(map(int,ax[0]))
a=list(dict.fromkeys(a))
a.sort()
for i in a:
    for j in range(0,k):
        if j==i:
            c=c+1
if c==k:
    print('yes')
else:
    print('no')
