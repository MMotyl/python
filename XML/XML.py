import pandas as pd


path = 'D:\\Programowanie\\GIT_Python\\python\\XML\\lista.xlsx'
df = pd.read_excel(path,  engine='openpyxl') 

# print(df.columns) # lista kolumn 

#print(df[df.columns[0]])
#print(df[df.columns[1]])

for index, contents in df.iterrows():
    for co in df.columns:
       print('row {:d} col name: {}={}'.format(index, co, contents[co] ) )

       
