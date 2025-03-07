def average(l):
    s=0
    c=0
    for i in l:
        s+=i
        c+=1
    return(s/c)
l=list(map(int,input().split()))
print(average(l))