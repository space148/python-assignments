l=list(map(int,input().split()))
f1=0
f2=0
for i in l:
    if i==12:
        f1+=1
    if i==23:
        f2+=1
    if f1>0 and f2>0:
        print('array contains 12 and 23')
        break
if f1==0 or f2==0:
    print('array doesnot contains 12,23')