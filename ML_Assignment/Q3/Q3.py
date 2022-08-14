#Q3
import numpy as np
#create 3-D array 
threeDarray=np.arange(9).reshape(3,3)
#print 3-D array
print("three diamentional array:\n",threeDarray)

#convert 3-D array into 1-D array
oneDarray = threeDarray.reshape(-1)
print("after conversion of 3-D into 1-D array")
print(oneDarray)
