#import pandas packege
import pandas as pd

#using execl means xlsx file
df=pd.read_excel("/home/osboxes/Desktop/pandas.xlsx")
print("the given DataFrame is : \n")
print(df)

#find minimum number of windspeed in DataFrame 
print("\nminimum windspeed is: ",df['windspeed'].min())

#find maximum number of windspeed in DataFrame 
print("\nmaximum windspeed is: ",df['windspeed'].max())

#find mean number of windspeed in DataFrame 
print("\nmean of windspeed is: ",df['windspeed'].mean())

#print those rows where "temp"is not 32
print("those rows where temp is not 32\n")
print(df[df['temp' ]!= 32])

#Print “temperature” when the event was sunny
print("Print “temperature” when the event was sunny\n")

print(df['temp'][df['event']=='sunny'])

#Print the top 5rows of the dataframe.
print("The top 5rows of the dataframe \n")
print(df.head(5))
