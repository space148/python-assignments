n=int(input())
temp=n
s=0
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
if s==temp:
    print("Palindrome")
else:
    print("Not a palindrome")