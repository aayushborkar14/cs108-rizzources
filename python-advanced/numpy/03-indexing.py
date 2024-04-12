import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
#second element in the array, index starts at 0
print("0", arr[1]) 
#Slicing elements
print("1", arr[1:5]) 
#negative index means start from end
print("2", arr[-3:-1])
#stepping by 2
print("3", arr[1:5:2]) 
print("4", arr[::2])

#2D array
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print("5", 'The array is:')
print(arr)
#1 --> second row; 4 --> 5th element in that row, hence prints 10 
print("6", '5th element on 2nd row: ', arr[1, 4]) 
#Slicing example
print("7", 'slice row 1,2 and columns 2-4')
print(arr[0:2, 1:4]) 

#returns array of items in the second column 
# ... is a shorthand notation that means "take all other dimensions".
# In this case, it means "take all rows"
x = arr[...,1]
print("8", 'The items in the second column are:')
# shape output will show 1 dimensional array with 2 elements!
print(x, x.shape) 
print('\n')  
#If you want to retain dimensions, you need to do something like this
y = arr[:, 1:2]
#shape output will show 2 dimensional array, 1st dimension - 2 elements,
#2nd deimension, 1 element i.e. 2x1 array 
print(y, y.shape) 
print('\n')  

#returns array of items in the second row 
print("9", 'The items in the second row are:') 
print(arr[1,...]) 
print('\n')  

#3D array, prints the element 6
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("10")
print("Array is \n ", arr)
print(arr[0, 1, 2])
print('\n')  

#printing matrices of 3-D
#iterates over the first dimension of the array
#Each iteration assigns x to a slice of the array along the first dimension.
print("prints along first dimension")
for x in arr:
  print(x) 

#printing rows in the matrix
print("prints rows in the matrix")
for x in arr:
  for y in x:
    print(y) 
    

#iterating through elements  
print("prints elements in the array")   
for x in arr:
  for y in x:
    for z in y:
      print(z)
      
#ndenumerate gives index information of every element
print("ndenumerate")
for idx, x in np.ndenumerate(arr):
  print(idx, x) 
  
