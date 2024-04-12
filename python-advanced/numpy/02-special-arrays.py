import numpy as np

#Special types of arrays
#array with ones on the main diagonal and zeros elsewhere.
arr = np.eye(3)
print("0", arr)

#array with zeros everywhere
arr = np.zeros((2,3))
print("1", arr)

#array with ones everywhere
arr = np.ones((3,4))
print("2", arr)

#an array with evenly spaced values via step within a specified interval.
arr = np.arange(10,20,2, dtype=float)
print("3", arr)
#evenly spaced values between the interval as specified.
arr = np.linspace(10,20,5) 
print("4", arr)

print('\n Random values \n')
#random with 3x2 matrix
arr=np.random.rand(3,2)
print("5", arr)
#random integers from 0 to 50, 2-D with size 3x5
x = np.random.randint(50, size=(3, 5))
print("6", x) 


