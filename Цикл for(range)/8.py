number=int(input("Введите натуральное целое число \n"))
if(number<=0):
    print("Неверный числовой ввод")
else:
    summa=0
    for i in range(number-1, 2, -1):
         if(i%3==0 or i%5==0):
             summa=summa+i
    print("Сумма чисел кратных 3 или 5 = " , summa)
