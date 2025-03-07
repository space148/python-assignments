def nonDup(l):
    a={}
    s=[]
    ans=[]
    for i in l:
        if i in s:
            a[i]+=1
        else:
            s.append(i)
            a[i]=1
    for i in l:
        if a[i]==1:
            ans.append(i)
    return ans
l=list(map(int,input().split()))
print(nonDup(l))