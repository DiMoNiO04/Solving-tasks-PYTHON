number_1,number_2=map(int,input().split())
while number_2>0:
    c=number_1%number_2
    number_1=number_2
    number_2=c
print(number_1)
