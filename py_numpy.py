import numpy as np

my_list = [1,2,3]

arr = np.array(my_list)
print(arr)

arr = np.arange(0,10).reshape(5,2)
print(arr)

arr = np.random.rand(10)
print(arr)

arr = np.random.randint(0, 100, 7)
print(arr)
print('max value: {}'.format(arr.max()))


