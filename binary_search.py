nums=[5,7,6,9,8,4,2,3,1]
nums.sort()
print(nums)

find_number=int(input("enrer the number "))
search_for=find_number

lowest=0
highest=len(nums)-1
index=None #Будущий индекс искомого элемента

while(lowest<=highest) and (index is None):
    #Повторяем пока не найдено
    mid=(lowest+highest)//2
    if nums[mid]==search_for:
        #Нашли по середине
        index=mid
    else:
        if search_for<nums[mid]:
            #Ищем в левой части списка(среза)
            highest=mid-1
        else:
            #Ищем в правой части списка(среза)
            lowest=mid+1
print("Искомый элемент", search_for,"находиться под индексом", index)
    
