l=list(map(int,input().split()))
a={}
s=[]
for i in l:
    if i in s:
        a[i]+=1
    else:
        s.append(i)
        a[i]=1
for i in s:
    if a[i]>1:
        print(i,end=' ')