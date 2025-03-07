def slarge(l):
    large=0
    for i in range(len(l)):
        if(l[i]>large):
            large=l[i]
    for i in range(len(l)):
        if l[i]==large:
            l[i]=0
    for i in range(len(l)):
        if(l[i]>large):
            large=l[i]
    return large
l=list(map(int,input().split()))
print(slarge(l))