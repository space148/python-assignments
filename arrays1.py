def addArrayElements(l):
    s=0
    for i in l:
        s+=i
    return s
l=list(map(int,input().split()))
print(addArrayElements(l))