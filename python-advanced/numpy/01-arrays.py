import numpy as np
print("0", np.__version__)

# Can create a ndarray object by using the array() method
#Below passes list as an argument, can use tuple also, see commented line
arr = np.array([1, 2, 3, 4, 5])
#arr = np.array((1, 2, 3, 4, 5))
print("1", arr)
print("2", type(arr))
print("3", arr.dtype) 

#create array as 4 byte integer
arr = np.array([1, 2, 3, 4], dtype='i4')
print("4", arr)
print("5", arr.dtype) 
arr = np.array([1, 2, 3], dtype = complex) 
print("6", arr)
print("7", arr.dtype) 

#convery from one type to another via astype() method
#data types
'''
    i - integer
    b - boolean
    u - unsigned integer
    f - float
    c - complex float
    m - timedelta
    M - datetime
    O - object
    S - string
    U - unicode string
    V - fixed chunk of memory for other type ( void )
'''
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print("8", newarr)
print("9", newarr.dtype) 


#Dimensions of array
#0-D
arr = np.array(42)
print("10", arr.ndim) 
#1-D
arr = np.array([1, 2, 3, 4, 5])
print("11", arr.ndim) 
#2-D
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("12", arr.ndim) 
#3-D
arr= np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("13", arr.ndim) 

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print("14", 'number of dimensions :', arr.ndim) 

#copy (new array owns the data) vs view (presents just a view of the original array)
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
x[0]=10
y[1]=5
arr[2]=15
print("15", arr)
print("16",x)
print("17", y)
#base tells if the array owns the data or is just a view, 
#view will return the org array, else none will print
print("18", x.base)
print("19", y.base) 

