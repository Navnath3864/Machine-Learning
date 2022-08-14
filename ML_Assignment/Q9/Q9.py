#Q9
import pandas as pd
#create dataframe (dictionary)
Student={'name':['Navnath','gulshan','abhishek','Hariom'],
         'rollno':[9009,9008,9011,9011],
         'marks':[90,80,70,60],
         'city':['pune','mumbai','banglore','hydrabad'],
        'state':['maharashtra','gujarat','UP','Maharashtra'],
        'fevsub':['ML','c','java','Ds']}
type(Student)

#convert dioconary into data frame
df=pd.DataFrame(Student)

#save this file into csv format

df.to_csv("/home/osboxes/Desktop/StudentDataFrame.csv")
print("After Loading the print Dataframe \n")

print(df)
#Apply describe function on the dataframe and analyse the result
print("After the use of describe function \n")
print(df.describe())

