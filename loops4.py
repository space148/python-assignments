#4. Write a program to print the odd and even numbers
n=int(input())
e=[]
o=[]
for i in range(1,n+1):
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
print('even \t: ', e)
print('odd \t: ',o)