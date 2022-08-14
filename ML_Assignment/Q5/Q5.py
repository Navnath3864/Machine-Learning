#Q5

#sin function using numpy and matplotlib packeges
import numpy as np
from matplotlib import pyplot as plt
def sinFun():
    print("First graph using sin function \n")
    x= np.arange(0,10,2.5) #(start ,end ,stepsize)
    y= np.sin(x)
    plt.plot(x,y)
    plt.title("sin chart")
    print(plt.show())
sinFun()

#create bar chart/graph
def barChart():
    print("second graph which is Bar chart\n")
    plt.bar([1,4],[5,7],label="ex1",color='r',width=1)
    plt.bar([3,6],[8,5],label="ex2",color='y',width=1)
    
    plt.legend()
    plt.xlabel("bar number")
    plt.ylabel("hight of bar")
    plt.title("bar graph")
    
    print(plt.show())
barChart()

#create histogram
def histogram():
    print("Third graph which is histogram \n")
    population_age=[22,55,62,45,21,22,34,42,100]
    bins=[0,10,20,30,40,50,60,70,80,90,100]
    plt.hist(population_age,bins,histtype="bar",rwidth=0.8,color='c')
    plt.xlabel('age number')
    plt.ylabel('number of people')
    plt.title('histogram')
    print(plt.show())
histogram()
