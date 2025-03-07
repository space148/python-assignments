#8. Write a program to find Armstrong number or not
i=int(input())
s=str(i)
l=len(s)
n=i
s=0
while n>0:
    r=n%10
    s=s+(r**l)
    n=n//10
if s==i:
    print("Armstrong")
else:
    print("Not An Armstrong")