number=int(input("Print one integer natural number \n"))
m=1
if(number<=0):
    print("Invalid numeric input")
else:
    while(number>0):
                  m=m * number%10
                  number=number//10
    print("The product of the digits of a given number = ", m)
    
