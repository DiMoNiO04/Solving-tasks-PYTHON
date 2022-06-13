m = input()  #Ввод кол-ва элем-ов
a = list(str(input()))  #Сами элементы
while '1' in a and '0' in a:  # Пока 1 и 0 есть в списке
    a.remove('1')  #Убираем 1
    a.remove('0')  # Убираем 0
print(len(a))  # Выводим
