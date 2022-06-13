n=int(input())
count=0
kub=1
row=1

while n>0:
    row=row+1
    kub=kub+row
    n=n-kub
    count=count+1
print(count)
