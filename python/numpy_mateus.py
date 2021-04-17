import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,10]])
a_inv = np.linalg.inv(a)

print(a)
print(a_inv)

print(np.dot(a,a_inv))