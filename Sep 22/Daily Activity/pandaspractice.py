import pandas as pd
import numpy as np

data = {
    "Name":["Rahul","Priya","Bipin","Mansi","Malhar"],
    "Age":[20,27,35,23,21],
    "Course":["AI","ML","AI","DS","ML"]
}

df = pd.DataFrame(data)
# print(df)

print("----Single Column----")
print(df["Name"])
print("----Multiple Column----")
print(df[["Name","Age"]])
print("----Single Record----")
print(df.iloc[0])
print("----Single Value in Record----")
print(df.loc[2,"Name"])

senior = df[df["Age"] >= 30]
print(senior)

df["Category"]=np.where(df["Age"] >= 30,"Senior","Junior")
print(df)

df.loc[df["Name"]=="Rahul","Age"]=30
print(df)