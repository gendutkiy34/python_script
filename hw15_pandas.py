# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 17:29:42 2021

@author: gendutkiy
"""

import pandas as pd
import datetime

class data_csv():
    
    def __init__(self,dataset):
        #param=f"r'{dataset}"
        self.data=pd.read_csv(dataset,sep='	')
    
    def getdata(self):
        return self.data
    
    def getcolumn(self):
        return self.data.columns    
fileset='C:\Data Engineer- Digital Skola\homework\marketing_campaign.csv' 
data_source=data_csv(fileset)
data_pandas=data_source.getdata()
print('#Info Table')
print(data_pandas.info())
print('\n\n#Describe Table')
print(data_pandas.describe())
print('\n\n#Check empty value')
print(data_pandas[data_pandas['Income'].isnull()])
print('\n\n#Check unique value')
print(data_pandas['Marital_Status'].value_counts())
print(data_pandas['Education'].value_counts())
print('\n\n#Check min and max from Year_Birth')
print('Min Year Birth : ',data_pandas['Year_Birth'].min())
print('Max Year Birth : ',data_pandas['Year_Birth'].max())
print('\n\n#colum name lower case')
new_column={}
for cl in data_pandas.columns:
     new_column[cl]=cl.lower()
data_pandas=data_pandas.rename(columns=new_column)
print(data_pandas.columns)
print('\n\n#Fill NA value in Columns Income')
new_data_pandas=data_pandas.copy()
print('Average income : ',new_data_pandas['income'].mean())
new_data_pandas['income']= new_data_pandas['income'].fillna(new_data_pandas['income'].mean()) 
print(new_data_pandas.info())
print('\n\n#New Column AGE')
nw=datetime.datetime.now()
yr=int(nw.year)
data_age=[]
for x in new_data_pandas['year_birth']:
    n=yr-x
    data_age.append(n)
new_data_pandas['age']=data_age
print(new_data_pandas.head())
print('\n\n#New Column AGE-Group')
data_agegroup=[]
for x in new_data_pandas['age']:
    if x < 21 :
        cat = 'teenager'
    elif x >= 21 and x <50:
        cat = 'worker'
    else :
        cat = 'boomer'
    data_agegroup.append(cat)
new_data_pandas['age_group']=data_agegroup
new_data_pandas['dt_customer']= pd.to_datetime(new_data_pandas['dt_customer'])
print(new_data_pandas.head())
new_data_pandas=new_data_pandas.sort_values(by=['dt_customer','income'], ascending=False)
print(new_data_pandas.head())
map={'Married':'together',
     'Together':'together',
     'Single':'alone',
     'Divorced':'alone',
     'Widow':'alone',
     'Alone':'alone',
     'YOLO':'alone',
     'Absurd':'alone'}
def maritalcat(marital_status):
    if marital_status in map.keys():
        new_sts=maritalcat[marital_status]
    else :
        new_sts=none
    return new_sts
new_data_pandas['marital_status']=new_data_pandas['marital_status'].apply(lambda x : maritalcat(x))
        
new_data_pandas.reset_index(inplace=True)
new_data_pandas.to_excel('C:\Data Engineer- Digital Skola\homework\data_pandas_customer.xlsx',sheet_name='output', index=False)
