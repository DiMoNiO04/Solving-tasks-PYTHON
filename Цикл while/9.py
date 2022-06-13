a=int(input())
a=list(map(int,input().split()))
b=int(input())
b=list(map(int,input().split()))
count=0

a.sort()
b.sort()

while a and b:
    if a[0]==b[0] or a[0]==b[0]+1 or a[0]==b[0]-1:
        count+=1
        a=a[1:]
        b=b[1:]
    elif a[0]!=b[0]+1 or a[0]!=b[0]-1:
        a=a[1:]
        b=b[1:]
print(count)






 
