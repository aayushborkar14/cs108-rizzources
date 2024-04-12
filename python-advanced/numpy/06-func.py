import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print("concatenate\n", arr) 

#2D along axis1
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=0)
print("concatenate along axis 0\n", arr)
print("shape is", arr.shape)
arr = np.concatenate((arr1, arr2), axis=1)
print("concatenate along axis 1 \n", arr)
print("shape is ", arr.shape)

#stack one on top of another
print("\n stacking axis=0")
arr = np.stack((arr1, arr2), axis=0)
print(arr)
print("shape is ", arr.shape)
print("\n stacking axis=1")
arr = np.stack((arr1, arr2), axis=1)
print(arr)
print("shape is ", arr.shape)

#splitting 1-D arrays
#split() function splits an array into multiple sub-arrays along a given axis
print('\n splitting 1D array \n')
arr = np.array([1, 2, 3, 4, 5, 6])
newarr=np.split(arr,3);
print(newarr)
#access each array
print(newarr[0])
#split method will fail here, hence used array_split
newarr1 = np.array_split(arr, 4)
print(newarr1)

#splitting 2D arrays, note only printing teh first array after split
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print('\n splitting 2D array \n')
print(newarr[0]) 

#searching arrays; returns index where that element is
print("\nsearching")
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print("element eqs 4", x) 
#values are odd
x = np.where(arr%2 == 1)
print("odd", x) 

#sorting; returns a copy leaving original array unchanged

arr = np.array([[3, 2, 4], [5, 0, 1]])
print("\n sorting\n", np.sort(arr)) 

#filtering based on a boolean index list (x in below example)
#filter only elements > 42
arr = np.array([41, 42, 43, 44])
x = [False, False, True, True]
newarr = arr[x]
print("\nfiltering", newarr) 

#Another way
x = arr > 42
newarr = arr[x]
print(x)
print(newarr) 
