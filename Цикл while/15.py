number=int(input("Введите одно натуральное число: \n"))
sum=0
if(number<0):
    print("Неверный числовой ввод")
else:
    while(number>0):
         sum=sum+number%10
         number=number//10
    print("Сумма цифр данного числа =", sum)
    
