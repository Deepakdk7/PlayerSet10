ax=input()
c=0
for i in range(0,len(ax)):
    for j in range(i+1,len(ax)):
        if ax[i]==ax[j]:
            c=1
            break
if c==1:
    print('yes')
else:
    print('no')
