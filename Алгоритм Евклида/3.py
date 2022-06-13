a,b=map(int,input().split())
p=a*b
while b>0:
    c=a%b
    a=b
    b=c
NOK=p//a
print(NOK)
