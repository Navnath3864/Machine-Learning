#create histogram
import matplotlib.pyplot as plt

print("Third graph which is histogram \n")
bins=[22,55,62,45,21,22,34,42]
noofpeople=[0,1,2,3,4,5,6,7]
plt.barh(bins,noofpeople) #is used to print horizontal bar

plt.xlabel('age groups')
plt.ylabel('number of people')
plt.title('histogram')
print(plt.show())
