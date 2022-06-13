number=int(input("Введите количество раундов \n"))
pointsMishka=0
pointsChris=0
for i in range(number):
    a,b=map(int,input("Результаты раунда: ").split())
    pointsMishka+=a
    pointsChris+=b
if pointsMishka==pointsChris:
    print("Friendship is magic!^^")
elif pointsMishka>pointsChris:
    print("Mishka")
else:
    print("Chris")



    

