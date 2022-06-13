number=int(input())
i=1
count=0
while i*i<=number:
    if number%i==0:
        if i==number//i:
            count+=1
        else:
            count+=2
    i+=1
if count !=2:
    print("No")
else:
    print("Yes")
