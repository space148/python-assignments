def remove(l,n):
    for i in range(l.count(n)):
        l.remove(n)
    return l
l=list(map(int,input().split()))
n=int(input())
print(remove(l,n))