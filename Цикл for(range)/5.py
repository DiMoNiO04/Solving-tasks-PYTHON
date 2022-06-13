numberFirst=int(input("Введите первое натуральное число: "))
numberSecond=int(input("Введите второе натуральное число: "))
if(numberFirst>numberSecond):
    print("Неверный числовой ввод:")
else:
     for i in range(numberFirst, numberSecond+1):
         if (i%3==0 and i%5==0):
             print("FizzBuzz")
         else: 
             if i%5==0:
                print("Buzz")
             else:  
                if(i%3==0):
                    print("Fizz")
                else:
                    print(i)
