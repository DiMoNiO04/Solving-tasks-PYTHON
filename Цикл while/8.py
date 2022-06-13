number=int(input())
i=-1
two=2**i
while two<number:
    i=i+1
    two=2**i
if two==number:
    print(i)
else:
    print("НЕТ")
