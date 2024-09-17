import numpy as np 


main_array = np.arange(1,9)
matirx_array = np.array([[2,3],[4,3],[3,32]])
emty_array = np.ones((3,3))
eye_array = np.eye(3, k = 1) #k is used for the diagonal postion on the 1 in the matrix

#filtering of arrays
eye_array[eye_array == 0] = 2 #To change the the Zeros in the array to specific number
eye_array[eye_array < 2] = 9#it is a filtering command where the numbers less than the 2 is changed to 9
eye_array[0] = 3#command to change the first rows to 3 or any desired values

#slicing Of Arrays
eye_array[:2] = 3# if we see ":" in the square braket it will take the all numbers between it.
eye_array[:,0] = 4 #To select the coloum 
eye_array[1:, :2] = 8
sorted_array = np.sort(eye_array)# sorting the row of array
sorted_array = np.sort(eye_array,axis = 0, kind="heapsort")# sorting the columes of array ( the axis = 0 is rows and the axis = -1 is colums)
#kind is used for specify the sorting algorithum

#copy arrays
my_view = sorted_array.view()
my_copy = sorted_array.copy()# the purpose of copy array is to preserve the main array from the expirmental changes done in the array.and


my_view[:] = 4

#print(main_array)
print(my_view)
print(my_copy)
#print(sorted_array)