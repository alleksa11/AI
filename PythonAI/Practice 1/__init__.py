# print("Якушов А.А. группа 090304-РПИа-о23. 25 в списке по журналу")
# for i in range (2, 25):
#    square = i ** 2
#    print (square)
import numpy as np
shape = (25,25,25)
random_array = np.random.randint(1,101,size = shape)
print(random_array)
