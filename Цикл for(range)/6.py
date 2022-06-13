numberFirst=int(input("Введите первое число \n"))
numberSecond=int(input("Введите второе число \n"))
a=1
b=1
if(numberFirst>numberSecond):
    print("Неверный числовой ввод")
else:
    for i in range(numberFirst, numberSecond+1):
        text='''Число {0}; его квадрат = {1}; его куб = {2}'''.format(i,i**2,i**3)
        print(text)
