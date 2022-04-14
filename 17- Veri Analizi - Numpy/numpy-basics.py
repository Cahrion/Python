import numpy as np


#Python list
py_list = [1,2,3,4,5,6,7,8,9]

# Numpy array(Dizi)
np_array = np.array([1,2,3,4,5,6,7,8,9])

print(type(py_list))
print(type(np_array))

py_multi = [[1,2,3],[4,5,6],[7,8,9]]
np_multi = np_array.reshape(9,1) # Parçalar.
print(np_multi)
print(py_multi)


print(np_array.ndim) # Kaç boyutlu oldugunu sööyler
print(np_multi.ndim)


print(np_array.shape) # Kaça kaçlık oldugunu söyler
print(np_multi.shape)