#Q10
import pandas as pd
df=pd.read_excel("/home/osboxes/Desktop/pandasCopy.xlsx")
print("the given DataFrame is : \n")
print(df)

print("\n")
#using isnull function we can check the missing value

print("using isnull() function we check the missing value \n")
checkNull=pd.isnull(df)
print(checkNull)

print("\n")
#using notnull function we can check the missing value

print("using notnull() function we check the missing value \n")
checkNull=pd.notnull(df)
print(checkNull)

#we can handle the missing value using three functions fillna() ,replace() and interpolate()

#use fillna()
print("after fillna ()")
print(df.fillna(0))

print("\n")

#use replacement()
print("print replace()")
print(df.replace())
