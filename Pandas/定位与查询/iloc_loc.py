
import pandas as pd
import numpy as np
PATH = 'Data.csv'
DATA = pd.read_csv(PATH)
# print(DATA.iloc[0])
# print(DATA.iloc[:,0])

# print(type(DATA.iloc[[2]]))
# DATA.set_index(['Country','Age','Salary','Purchased'],inplace=True)
DATA.set_index('Country',inplace=True)

# print(DATA.loc[['Spain']])
# print(DATA.loc[:,['Age']])
# print(DATA.loc[['France','Spain'],['Age','Salary']])
# print(DATA.loc[(DATA['Age']>40),:])