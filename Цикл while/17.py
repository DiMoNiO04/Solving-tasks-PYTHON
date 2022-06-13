number=int(input("Enter a natural integer\n"))
cout=0
if(number<=0):
    print("Invalid numeric input")
else:
    while(number>0):
        if number%10==7:
            cout+=1
        number//=10
    print("Cout of sevens in a number = ",cout)
