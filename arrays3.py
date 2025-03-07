l=list(map(int,input().split()))
e=int(input())
f=0
for i in range(len(l)):
    if l[i]==e:
        print(i,end=' ')
        f=1
if f==0:
    print(e,'is not the list')