def copy(l,m):
    l+=m
    return(l)
l=list(map(int,input().split()))
m=list(map(int,input().split()))
print(copy(l,m))