# Q1 

import numpy as np #take np as alias name
def firstFun():
    four_dia_array = np.array([[[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]]]) #create an array using array function

    #print array element using
    print("print an array using array function\n")
    print(four_dia_array)
firstFun()
def secondFun():
    #craete array using arange function
    four_dia_array_arangeFun = np.arange(16).reshape(4,4)
    print("print an array using arange function\n")
    print(four_dia_array_arangeFun)
secondFun()
