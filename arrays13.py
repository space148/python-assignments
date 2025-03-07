def slarge(l):
    l.remove(max(l))
    return(max(l))
l=list(map(int,input().split()))
print(slarge(l))