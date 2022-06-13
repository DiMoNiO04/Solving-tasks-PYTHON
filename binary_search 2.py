from random import randint
import datetime
import numpy


def binary_search(array,key):
    lower_bound=0
    upper_bound= len(array)-1

    while lower_bound<=upper_bound:
        center=(lower_bound+upper_bound)//2

        if array[center] == key:
            return center
        elif array[center]>key:
            upper_bound = center-1
        elif array[center]<key:
            lower_bound = center+1

    return -1



x = numpy.random.randint(0,1000,100000)
print("Array sorted")
start = datetime.datetime.now()
print(binary_search (x,1023)) #or find_num
print("End time:", datetime.datetime.now()-start)

