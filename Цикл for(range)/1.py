number=int(input("Введите натуральное целое число "))
if(number<=0):
    print("Неверный числовой ввод")
else:
     for i in range(1, number+1):
         print(i)
