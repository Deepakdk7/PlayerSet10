ax=int(input())
a=list(map(int,input().split()))
b=a
b=sorted(b)
for i in b:
    print(a.index(i)+1,"",end="")
