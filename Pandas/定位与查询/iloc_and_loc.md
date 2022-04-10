

[toc]

## 原数据

```   python
import pandas as pd
import numpy as np
PATH = './Data.csv'
DATA = pd.read_csv(PATH)
print(DATA)
>>> DATA
   Country   Age   Salary Purchased
0   France  44.0  72000.0        No
1    Spain  27.0  48000.0       Yes
2  Germany  30.0  54000.0        No
3    Spain  38.0  61000.0        No
4  Germany  40.0      NaN       Yes
5   France  35.0  58000.0       Yes
6    Spain   NaN  52000.0        No
7   France  48.0  79000.0       Yes
8  Germany  50.0  83000.0        No
9   France  37.0  67000.0       Yes
--------
```

## 一、iloc[	]

iloc[]通过代数位置来进行定位

```python
#	定位第1个元素
print(DATA.iloc[0,0])
#	定位第1行	
print(DATA.iloc[0,:])
#	定位第1行	
print(DATA.iloc[[0]])
#	定位第1列
print(DATA.iloc[:,0])
#	定位多行多列
print(DATA.iloc[[1,2],[1,2]])
#	定位多行多列
print(DATA.iloc[0:2,1:3])
```

## 二、loc[	]

loc[]需要先设置索引,按索引定位

```python
DATA = pd.read_csv(PATH,index_col='Country')
#	或
DATA.set_index('Country',inplace=True)
#	定位'Spain'行
print(DATA.loc['Spain',:])
>>>
          Age   Salary Purchased
Country                         
Spain    27.0  48000.0       Yes
Spain    38.0  61000.0        No
Spain     NaN  52000.0        No
#	定位'Age'列 索引会一直跟着的
Country
France     44.0
Spain      27.0
Germany    30.0
Spain      38.0
Germany    40.0
France     35.0
Spain       NaN
France     48.0
Germany    50.0
France     37.0
Name: Age, dtype: float64
#	bool选择
print(DATA.loc[DATA['Age']>40,:])
>>>
          Age   Salary Purchased
Country                         
France   44.0  72000.0        No
France   48.0  79000.0       Yes
Germany  50.0  83000.0        No
```

