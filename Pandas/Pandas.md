[toc]

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

## 一、产生 Pandas 对象

pandas 中有三种基本结构：

+ Series

    1D labeled homogeneously-typed array

+ DataFrame
    General 2D labeled, size-mutable tabular structure with potentially heterogeneously-typed columns

+ Panel
    General 3D labeled, also size-mutable array

### Series

一维 `Series` 可以用一维列表初始化：

```python
s = pd.Series([1,3,5,np.nan,6,8])
>>>
0     1
1     3
2     5
3   NaN
4     6
5     8
dtype: float64
```

### DataFrame

`DataFrame` 则是个二维结构，这里首先构造一组时间序列，作为我们第一维的下标：

```python
dates = pd.date_range('20200401',periods=6)
>>> dates
DatetimeIndex(['2020-04-01', '2020-04-02', '2020-04-03', '2020-04-04',
               '2020-04-05', '2020-04-06'],
              dtype='datetime64[ns]', freq='D')
```

然后创建一个 `DataFrame` 结构：

```python
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

>>> df
                   A         B         C         D
2020-04-01  0.654387 -0.753177 -0.670787 -0.081551
2020-04-02  2.008936 -1.370460 -0.413884 -0.229023
2020-04-03  0.097671 -0.185534 -0.122558 -0.459926
2020-04-04  0.608844  0.171862 -0.053438 -2.657727
2020-04-05 -0.840587 -1.091342 -1.331858 -1.667727
2020-04-06 -0.359167 -0.587902  1.886626 -0.448873
```

默认情况下，如果不指定 `index` 参数和 `columns`，那么他们的值将用从 `0` 开始的数字替代。

除了向 `DataFrame` 中传入二维数组，我们也可以使用字典传入数据：

```python
df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo' })

>>> df2
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
```

字典的每个 `key` 代表一列，其 `value` 可以是各种能够转化为 `Series` 的对象。

与 `Series` 要求所有的类型都一致不同，`DataFrame` 值要求每一列数据的格式相同：

```python
>>> df2.dtypes
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
```

## 二、查看数据

|            | A         | B         | C         | D         |
| ---------- | --------- | --------- | --------- | --------- |
| 2013-01-01 | -0.605936 | -0.861658 | -1.001924 | 1.528584  |
| 2013-01-02 | -0.165408 | 0.388338  | 1.187187  | 1.819818  |
| 2013-01-03 | 0.065255  | -1.608074 | -1.282331 | -0.286067 |
| 2013-01-04 | 1.289305  | 0.497115  | -0.225351 | 0.040239  |
| 2013-01-05 | 0.038232  | 0.875057  | -0.092526 | 0.934432  |
| 2013-01-06 | -2.163453 | -0.010279 | 1.699886  | 1.291653  |

### 头尾数据

`head` 和 `tail` 方法可以分别查看最前面几行和最后面几行的数据（默认为 5）：

```python
df.head()
```

最后 3 行：

```python
df.tail(3)
```

### 下标，列标，数据

下标使用 `index` 属性查看：

```python
df.index
```

```py
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
```

列标使用 `columns` 属性查看：

```py
df.columns
```

```py
Index([u'A', u'B', u'C', u'D'], dtype='object')
```

数据值使用 `values` 查看：

```py
df.values
```

```py
array([[-0.60593585, -0.86165752, -1.00192387,  1.52858443],
       [-0.16540784,  0.38833783,  1.18718697,  1.81981793],
       [ 0.06525454, -1.60807414, -1.2823306 , -0.28606716],
       [ 1.28930486,  0.49711531, -0.22535143,  0.04023897],
       [ 0.03823179,  0.87505664, -0.0925258 ,  0.93443212],
       [-2.16345271, -0.01027865,  1.69988608,  1.29165337]])
```

### 统计数据

查看简单的统计数据：

```py
df.describe()
```

|       | A         | B         | C         | D         |
| ----- | --------- | --------- | --------- | --------- |
| count | 6.000000  | 6.000000  | 6.000000  | 6.000000  |
| mean  | -0.257001 | -0.119917 | 0.047490  | 0.888110  |
| std   | 1.126657  | 0.938705  | 1.182629  | 0.841529  |
| min   | -2.163453 | -1.608074 | -1.282331 | -0.286067 |
| 25%   | -0.495804 | -0.648813 | -0.807781 | 0.263787  |
| 50%   | -0.063588 | 0.189030  | -0.158939 | 1.113043  |
| 75%   | 0.058499  | 0.469921  | 0.867259  | 1.469352  |
| max   | 1.289305  | 0.875057  | 1.699886  | 1.819818  |

### 转置

```py
df.T
```

|      | 2013-01-01 00:00:00 | 2013-01-02 00:00:00 | 2013-01-03 00:00:00 | 2013-01-04 00:00:00 | 2013-01-05 00:00:00 | 2013-01-06 00:00:00 |
| ---- | ------------------- | ------------------- | ------------------- | ------------------- | ------------------- | ------------------- |
| A    | -0.605936           | -0.165408           | 0.065255            | 1.289305            | 0.038232            | -2.163453           |
| B    | -0.861658           | 0.388338            | -1.608074           | 0.497115            | 0.875057            | -0.010279           |
| C    | -1.001924           | 1.187187            | -1.282331           | -0.225351           | -0.092526           | 1.699886            |
| D    | 1.528584            | 1.819818            | -0.286067           | 0.040239            | 0.934432            | 1.291653            |

## 三、排序

`sort_index(axis=0, ascending=True)` 方法按照下标大小进行排序，`axis=0` 表示按第 0 维进行排序。

```py
df.sort_index(ascending=False)
```

|            | A         | B         | C         | D         |
| ---------- | --------- | --------- | --------- | --------- |
| 2013-01-06 | -2.163453 | -0.010279 | 1.699886  | 1.291653  |
| 2013-01-05 | 0.038232  | 0.875057  | -0.092526 | 0.934432  |
| 2013-01-04 | 1.289305  | 0.497115  | -0.225351 | 0.040239  |
| 2013-01-03 | 0.065255  | -1.608074 | -1.282331 | -0.286067 |
| 2013-01-02 | -0.165408 | 0.388338  | 1.187187  | 1.819818  |
| 2013-01-01 | -0.605936 | -0.861658 | -1.001924 | 1.528584  |

```py
df.sort_index(axis=1, ascending=False)
```

|            | D         | C         | B         | A         |
| ---------- | --------- | --------- | --------- | --------- |
| 2013-01-01 | 1.528584  | -1.001924 | -0.861658 | -0.605936 |
| 2013-01-02 | 1.819818  | 1.187187  | 0.388338  | -0.165408 |
| 2013-01-03 | -0.286067 | -1.282331 | -1.608074 | 0.065255  |
| 2013-01-04 | 0.040239  | -0.225351 | 0.497115  | 1.289305  |
| 2013-01-05 | 0.934432  | -0.092526 | 0.875057  | 0.038232  |
| 2013-01-06 | 1.291653  | 1.699886  | -0.010279 | -2.163453 |

`sort_values(by, axis=0, ascending=True)` 方法按照 `by` 的值的大小进行排序，例如按照 `B` 列的大小：

```py
df.sort_values(by="B")
```

|            | A         | B         | C         | D         |
| ---------- | --------- | --------- | --------- | --------- |
| 2013-01-03 | 0.065255  | -1.608074 | -1.282331 | -0.286067 |
| 2013-01-01 | -0.605936 | -0.861658 | -1.001924 | 1.528584  |
| 2013-01-06 | -2.163453 | -0.010279 | 1.699886  | 1.291653  |
| 2013-01-02 | -0.165408 | 0.388338  | 1.187187  | 1.819818  |
| 2013-01-04 | 1.289305  | 0.497115  | -0.225351 | 0.040239  |
| 2013-01-05 | 0.038232  | 0.875057  | -0.092526 | 0.934432  |

## 四、索引

|            | A         | B         | C         | D         |
| ---------- | --------- | --------- | --------- | --------- |
| 2013-01-01 | -0.605936 | -0.861658 | -1.001924 | 1.528584  |
| 2013-01-02 | -0.165408 | 0.388338  | 1.187187  | 1.819818  |
| 2013-01-03 | 0.065255  | -1.608074 | -1.282331 | -0.286067 |
| 2013-01-04 | 1.289305  | 0.497115  | -0.225351 | 0.040239  |
| 2013-01-05 | 0.038232  | 0.875057  | -0.092526 | 0.934432  |
| 2013-01-06 | -2.163453 | -0.010279 | 1.699886  | 1.291653  |

虽然 `DataFrame` 支持 `Python/Numpy` 的索引语法，但是推荐使用 `.at, .iat, .loc, .iloc 和 .ix` 方法进行索引。

### 读取数据

选择单列数据：

```py
df["A"]
```

```py
2013-01-01   -0.605936
2013-01-02   -0.165408
2013-01-03    0.065255
2013-01-04    1.289305
2013-01-05    0.038232
2013-01-06   -2.163453
Freq: D, Name: A, dtype: float64
```

也可以用 `df.A`：

```py
df.A
```

```py
2013-01-01   -0.605936
2013-01-02   -0.165408
2013-01-03    0.065255
2013-01-04    1.289305
2013-01-05    0.038232
2013-01-06   -2.163453
Freq: D, Name: A, dtype: float64
```

使用切片读取多行：

```py
df[0:3]
```

|            | A         | B         | C         | D         |
| ---------- | --------- | --------- | --------- | --------- |
| 2013-01-01 | -0.605936 | -0.861658 | -1.001924 | 1.528584  |
| 2013-01-02 | -0.165408 | 0.388338  | 1.187187  | 1.819818  |
| 2013-01-03 | 0.065255  | -1.608074 | -1.282331 | -0.286067 |

`index` 名字也可以进行切片：

```py
df["20130101":"20130103"]
```

|            | A         | B         | C         | D         |
| ---------- | --------- | --------- | --------- | --------- |
| 2013-01-01 | -0.605936 | -0.861658 | -1.001924 | 1.528584  |
| 2013-01-02 | -0.165408 | 0.388338  | 1.187187  | 1.819818  |
| 2013-01-03 | 0.065255  | -1.608074 | -1.282331 | -0.286067 |

### 使用 `label` 索引

`loc` 可以方便的使用 `label` 进行索引：

```py
df.loc[dates[0]]
```

```py
A   -0.605936
B   -0.861658
C   -1.001924
D    1.528584
Name: 2013-01-01 00:00:00, dtype: float64
```

多列数据：

```py
df.loc[:,['A','B']]

```

|            | A         | B         |
| ---------- | --------- | --------- |
| 2013-01-01 | -0.605936 | -0.861658 |
| 2013-01-02 | -0.165408 | 0.388338  |
| 2013-01-03 | 0.065255  | -1.608074 |
| 2013-01-04 | 1.289305  | 0.497115  |
| 2013-01-05 | 0.038232  | 0.875057  |
| 2013-01-06 | -2.163453 | -0.010279 |

选择多行多列：

```py
df.loc['20130102':'20130104',['A','B']]
```

|            | A         | B         |
| ---------- | --------- | --------- |
| 2013-01-02 | -0.165408 | 0.388338  |
| 2013-01-03 | 0.065255  | -1.608074 |
| 2013-01-04 | 1.289305  | 0.497115  |

数据降维：

```py
df.loc['20130102',['A','B']]

```

```py
A   -0.165408
B    0.388338
Name: 2013-01-02 00:00:00, dtype: float64
```

得到标量值：

```py
df.loc[dates[0],'B']

```

```py
-0.86165751902832299
```

**不过得到标量值可以用** `at`，速度更快：

```py
%timeit -n100 df.loc[dates[0],'B']
%timeit -n100 df.at[dates[0],'B']
print df.at[dates[0],'B']
```

```py
100 loops, best of 3: 329 µs per loop
100 loops, best of 3: 31.1 µs per loop
-0.861657519028
```

### 使用位置索引

`iloc` 使用位置进行索引：

```py
df.iloc[3]
```

```py
A    1.289305
B    0.497115
C   -0.225351
D    0.040239
Name: 2013-01-04 00:00:00, dtype: float64
```

连续切片：

```py
df.iloc[3:5,0:2]
```

|            | A        | B        |
| ---------- | -------- | -------- |
| 2013-01-04 | 1.289305 | 0.497115 |
| 2013-01-05 | 0.038232 | 0.875057 |

索引不连续的部分：

```py
df.iloc[[1,2,4],[0,2]]
```

|            | A         | C         |
| ---------- | --------- | --------- |
| 2013-01-02 | -0.165408 | 1.187187  |
| 2013-01-03 | 0.065255  | -1.282331 |
| 2013-01-05 | 0.038232  | -0.092526 |

索引整行：

```py
df.iloc[1:3,:]
```

|            | A         | B         | C         | D         |
| ---------- | --------- | --------- | --------- | --------- |
| 2013-01-02 | -0.165408 | 0.388338  | 1.187187  | 1.819818  |
| 2013-01-03 | 0.065255  | -1.608074 | -1.282331 | -0.286067 |

整列：

```py
df.iloc[:, 1:3]
```

|            | B         | C         |
| ---------- | --------- | --------- |
| 2013-01-01 | -0.861658 | -1.001924 |
| 2013-01-02 | 0.388338  | 1.187187  |
| 2013-01-03 | -1.608074 | -1.282331 |
| 2013-01-04 | 0.497115  | -0.225351 |
| 2013-01-05 | 0.875057  | -0.092526 |
| 2013-01-06 | -0.010279 | 1.699886  |

标量值：

```py
df.iloc[1,1]
```

```py
0.3883378290420279
```

当然，使用 `iat` 索引标量值更快：

```py
%timeit -n100 df.iloc[1,1]
%timeit -n100 df.iat[1,1]
df.iat[1,1]
```

```py
100 loops, best of 3: 236 µs per loop
100 loops, best of 3: 14.5 µs per loop
```

```py
0.3883378290420279
```

### 布尔型索引

所有 `A` 列大于 0 的行：

In [34]:

```py
df[df.A > 0]
```

|            | A        | B         | C         | D         |
| ---------- | -------- | --------- | --------- | --------- |
| 2013-01-03 | 0.065255 | -1.608074 | -1.282331 | -0.286067 |
| 2013-01-04 | 1.289305 | 0.497115  | -0.225351 | 0.040239  |
| 2013-01-05 | 0.038232 | 0.875057  | -0.092526 | 0.934432  |

只留下所有大于 0 的数值：

```py
df[df > 0]
```

Out[35]:

|            | A        | B        | C        | D        |
| ---------- | -------- | -------- | -------- | -------- |
| 2013-01-01 | NaN      | NaN      | NaN      | 1.528584 |
| 2013-01-02 | NaN      | 0.388338 | 1.187187 | 1.819818 |
| 2013-01-03 | 0.065255 | NaN      | NaN      | NaN      |
| 2013-01-04 | 1.289305 | 0.497115 | NaN      | 0.040239 |
| 2013-01-05 | 0.038232 | 0.875057 | NaN      | 0.934432 |
| 2013-01-06 | NaN      | NaN      | 1.699886 | 1.291653 |

使用 `isin` 方法做 `filter` 过滤：

```py
df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']
df2
```

|            | A         | B         | C         | D         | E     |
| ---------- | --------- | --------- | --------- | --------- | ----- |
| 2013-01-01 | -0.605936 | -0.861658 | -1.001924 | 1.528584  | one   |
| 2013-01-02 | -0.165408 | 0.388338  | 1.187187  | 1.819818  | one   |
| 2013-01-03 | 0.065255  | -1.608074 | -1.282331 | -0.286067 | two   |
| 2013-01-04 | 1.289305  | 0.497115  | -0.225351 | 0.040239  | three |
| 2013-01-05 | 0.038232  | 0.875057  | -0.092526 | 0.934432  | four  |
| 2013-01-06 | -2.163453 | -0.010279 | 1.699886  | 1.291653  | three |

```py
df2[df2['E'].isin(['two','four'])]
```

Out[37]:

|            | A        | B         | C         | D         | E    |
| ---------- | -------- | --------- | --------- | --------- | ---- |
| 2013-01-03 | 0.065255 | -1.608074 | -1.282331 | -0.286067 | two  |
| 2013-01-05 | 0.038232 | 0.875057  | -0.092526 | 0.934432  | four |

### 设定数据的值

```py
s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))
s1
```

```py
2013-01-02    1
2013-01-03    2
2013-01-04    3
2013-01-05    4
2013-01-06    5
2013-01-07    6
Freq: D, dtype: int64
```

像字典一样，直接指定 `F` 列的值为 `s1`，此时以 `df` 已有的 `index` 为标准将二者进行合并，`s1` 中没有的 `index` 项设为 `NaN`，多余的项舍去：

```py
df['F'] = s1
df
```

|            | A         | B         | C         | D         | F    |
| ---------- | --------- | --------- | --------- | --------- | ---- |
| 2013-01-01 | -0.605936 | -0.861658 | -1.001924 | 1.528584  | NaN  |
| 2013-01-02 | -0.165408 | 0.388338  | 1.187187  | 1.819818  | 1    |
| 2013-01-03 | 0.065255  | -1.608074 | -1.282331 | -0.286067 | 2    |
| 2013-01-04 | 1.289305  | 0.497115  | -0.225351 | 0.040239  | 3    |
| 2013-01-05 | 0.038232  | 0.875057  | -0.092526 | 0.934432  | 4    |
| 2013-01-06 | -2.163453 | -0.010279 | 1.699886  | 1.291653  | 5    |

或者使用 `at` 或 `iat` 修改单个值：

```py
df.at[dates[0],'A'] = 0
df
```

|            | A         | B         | C         | D         | F    |
| ---------- | --------- | --------- | --------- | --------- | ---- |
| 2013-01-01 | 0.000000  | -0.861658 | -1.001924 | 1.528584  | NaN  |
| 2013-01-02 | -0.165408 | 0.388338  | 1.187187  | 1.819818  | 1    |
| 2013-01-03 | 0.065255  | -1.608074 | -1.282331 | -0.286067 | 2    |
| 2013-01-04 | 1.289305  | 0.497115  | -0.225351 | 0.040239  | 3    |
| 2013-01-05 | 0.038232  | 0.875057  | -0.092526 | 0.934432  | 4    |
| 2013-01-06 | -2.163453 | -0.010279 | 1.699886  | 1.291653  | 5    |

```py
df.iat[0, 1] = 0
df
```

Out[41]:

|            | A         | B         | C         | D         | F    |
| ---------- | --------- | --------- | --------- | --------- | ---- |
| 2013-01-01 | 0.000000  | 0.000000  | -1.001924 | 1.528584  | NaN  |
| 2013-01-02 | -0.165408 | 0.388338  | 1.187187  | 1.819818  | 1    |
| 2013-01-03 | 0.065255  | -1.608074 | -1.282331 | -0.286067 | 2    |
| 2013-01-04 | 1.289305  | 0.497115  | -0.225351 | 0.040239  | 3    |
| 2013-01-05 | 0.038232  | 0.875057  | -0.092526 | 0.934432  | 4    |
| 2013-01-06 | -2.163453 | -0.010279 | 1.699886  | 1.291653  | 5    |

设定一整列：

```py
df.loc[:,'D'] = np.array([5] * len(df))
df
```

|            | A         | B         | C         | D    | F    |
| ---------- | --------- | --------- | --------- | ---- | ---- |
| 2013-01-01 | 0.000000  | 0.000000  | -1.001924 | 5    | NaN  |
| 2013-01-02 | -0.165408 | 0.388338  | 1.187187  | 5    | 1    |
| 2013-01-03 | 0.065255  | -1.608074 | -1.282331 | 5    | 2    |
| 2013-01-04 | 1.289305  | 0.497115  | -0.225351 | 5    | 3    |
| 2013-01-05 | 0.038232  | 0.875057  | -0.092526 | 5    | 4    |
| 2013-01-06 | -2.163453 | -0.010279 | 1.699886  | 5    | 5    |

设定满足条件的数值：

```py
df2 = df.copy()

df2[df2 > 0] = -df2

df2
```

|            | A         | B         | C         | D    | F    |
| ---------- | --------- | --------- | --------- | ---- | ---- |
| 2013-01-01 | 0.000000  | 0.000000  | -1.001924 | -5   | NaN  |
| 2013-01-02 | -0.165408 | -0.388338 | -1.187187 | -5   | -1   |
| 2013-01-03 | -0.065255 | -1.608074 | -1.282331 | -5   | -2   |
| 2013-01-04 | -1.289305 | -0.497115 | -0.225351 | -5   | -3   |
| 2013-01-05 | -0.038232 | -0.875057 | -0.092526 | -5   | -4   |
| 2013-01-06 | -2.163453 | -0.010279 | -1.699886 | -5   | -5   |

## 五、缺失数据

调用reindex将会重新排序，缺失值则用NaN填补,后面的项目也要跟着调整

```py
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1],'E'] = 1

df1

```

|            | A         | B         | C         | D    | F    | E    |
| ---------- | --------- | --------- | --------- | ---- | ---- | ---- |
| 2013-01-01 | 0.000000  | 0.000000  | -1.001924 | 5    | NaN  | 1    |
| 2013-01-02 | -0.165408 | 0.388338  | 1.187187  | 5    | 1    | 1    |
| 2013-01-03 | 0.065255  | -1.608074 | -1.282331 | 5    | 2    | NaN  |
| 2013-01-04 | 1.289305  | 0.497115  | -0.225351 | 5    | 3    | NaN  |

丢弃所有缺失数据的行得到的新数据：

```py
df1.dropna(how='any')
```

|            | A         | B        | C        | D    | F    | E    |
| ---------- | --------- | -------- | -------- | ---- | ---- | ---- |
| 2013-01-02 | -0.165408 | 0.388338 | 1.187187 | 5    | 1    | 1    |

填充缺失数据：

```py
df1.fillna(value=5)

```

|            | A         | B         | C         | D    | F    | E    |
| ---------- | --------- | --------- | --------- | ---- | ---- | ---- |
| 2013-01-01 | 0.000000  | 0.000000  | -1.001924 | 5    | 5    | 1    |
| 2013-01-02 | -0.165408 | 0.388338  | 1.187187  | 5    | 1    | 1    |
| 2013-01-03 | 0.065255  | -1.608074 | -1.282331 | 5    | 2    | 5    |
| 2013-01-04 | 1.289305  | 0.497115  | -0.225351 | 5    | 3    | 5    |

检查缺失数据的位置：

```py
pd.isnull(df1)
```

|            | A     | B     | C     | D     | F     | E     |
| ---------- | ----- | ----- | ----- | ----- | ----- | ----- |
| 2013-01-01 | False | False | False | False | True  | False |
| 2013-01-02 | False | False | False | False | False | False |
| 2013-01-03 | False | False | False | False | False | True  |
| 2013-01-04 | False | False | False | False | False | True  |

## 六、计算操作

### 统计信息

每一列的均值：

```py
df.mean()
```

```py
A   -0.156012
B    0.023693
C    0.047490
D    5.000000
F    3.000000
dtype: float64
```

每一行的均值：

```py
df.mean(1)
```

```py
2013-01-01    0.999519
2013-01-02    1.482023
2013-01-03    0.834970
2013-01-04    1.912214
2013-01-05    1.964153
2013-01-06    1.905231
Freq: D, dtype: float64
```

多个对象之间的操作，如果维度不对，`pandas` 会自动调用 `broadcasting` 机制：

`shift(2)`意为index向下偏移`2`

```py
s = pd.Series([1,3,5,np.nan,6,8], index=dates).shift(2)

print s

```

```py
2013-01-01   NaN
2013-01-02   NaN
2013-01-03     1
2013-01-04     3
2013-01-05     5
2013-01-06   NaN
Freq: D, dtype: float64
```

相减 `df - s`：

In [51]:

```py
df.sub(s, axis='index')
```

Out[51]:

|            | A         | B         | C         | D    | F    |
| ---------- | --------- | --------- | --------- | ---- | ---- |
| 2013-01-01 | NaN       | NaN       | NaN       | NaN  | NaN  |
| 2013-01-02 | NaN       | NaN       | NaN       | NaN  | NaN  |
| 2013-01-03 | -0.934745 | -2.608074 | -2.282331 | 4    | 1    |
| 2013-01-04 | -1.710695 | -2.502885 | -3.225351 | 2    | 0    |
| 2013-01-05 | -4.961768 | -4.124943 | -5.092526 | 0    | -1   |
| 2013-01-06 | NaN       | NaN       | NaN       | NaN  | NaN  |

### `apply` 操作

与 `python 中的 `apply` 操作类似，接收一个函数，默认是对将函数作用到每一列上：

```py
df.apply(np.cumsum)
```

|            | A         | B         | C         | D    | F    |
| ---------- | --------- | --------- | --------- | ---- | ---- |
| 2013-01-01 | 0.000000  | 0.000000  | -1.001924 | 5    | NaN  |
| 2013-01-02 | -0.165408 | 0.388338  | 0.185263  | 10   | 1    |
| 2013-01-03 | -0.100153 | -1.219736 | -1.097067 | 15   | 3    |
| 2013-01-04 | 1.189152  | -0.722621 | -1.322419 | 20   | 6    |
| 2013-01-05 | 1.227383  | 0.152436  | -1.414945 | 25   | 10   |
| 2013-01-06 | -0.936069 | 0.142157  | 0.284941  | 30   | 15   |

求每列最大最小值之差：

```py
df.apply(lambda x: x.max() - x.min())
```

```py
A    3.452758
B    2.483131
C    2.982217
D    0.000000
F    4.000000
dtype: float64
```

### 直方图

```py
s = pd.Series(np.random.randint(0, 7, size=10))
print s
```

```py
0    2
1    5
2    6
3    6
4    6
5    3
6    5
7    0
8    4
9    4
dtype: int64

```

直方图信息：

```py
print s.value_counts()

```

```py
6    3
5    2
4    2
3    1
2    1
0    1
dtype: int64
```

绘制直方图信息：

In [56]:

```py
h = s.hist()
```

![](data:image/png;base64,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)

### 字符串方法

当 `Series` 或者 `DataFrame` 的某一列是字符串时，我们可以用 `.str` 对这个字符串数组进行字符串的基本操作：

In [57]:

```py
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])

print s.str.lower()

```

```py
0       a
1       b
2       c
3    aaba
4    baca
5     NaN
6    caba
7     dog
8     cat
dtype: object

```

## 七、合并

### 连接

```py
df = pd.DataFrame(np.random.randn(10, 4))

df

```

|      | 0         | 1         | 2         | 3         |
| ---- | --------- | --------- | --------- | --------- |
| 0    | -2.346373 | 0.105651  | -0.048027 | 0.010637  |
| 1    | -0.682198 | 0.943043  | 0.147312  | -0.657871 |
| 2    | 0.515766  | -0.768286 | 0.361570  | 1.146278  |
| 3    | -0.607277 | -0.003086 | -1.499001 | 1.165728  |
| 4    | -1.226279 | -0.177246 | -1.379631 | -0.639261 |
| 5    | 0.807364  | -1.855060 | 0.325968  | 1.898831  |
| 6    | 0.438539  | -0.728131 | -0.009924 | 0.398360  |
| 7    | 1.497457  | -1.506314 | -1.557624 | 0.869043  |
| 8    | 0.945985  | -0.519435 | -0.510359 | -1.077751 |
| 9    | 1.597679  | -0.285955 | -1.060736 | 0.608629  |

可以使用 `pd.concat` 函数将多个 `pandas` 对象进行连接：

```py
pieces = [df[:2], df[4:5], df[7:]]

pd.concat(pieces)

```

|      | 0         | 1         | 2         | 3         |
| ---- | --------- | --------- | --------- | --------- |
| 0    | -2.346373 | 0.105651  | -0.048027 | 0.010637  |
| 1    | -0.682198 | 0.943043  | 0.147312  | -0.657871 |
| 4    | -1.226279 | -0.177246 | -1.379631 | -0.639261 |
| 7    | 1.497457  | -1.506314 | -1.557624 | 0.869043  |
| 8    | 0.945985  | -0.519435 | -0.510359 | -1.077751 |
| 9    | 1.597679  | -0.285955 | -1.060736 | 0.608629  |

### 数据库中的 Join

`merge` 可以实现数据库中的 `join` 操作：

```py
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})

print left
print right

```

```py
   key  lval
0  foo     1
1  foo     2
   key  rval
0  foo     4
1  foo     5

```

```py
pd.merge(left, right, on='key')

```

Out[61]:

|      | key  | lval | rval |
| ---- | ---- | ---- | ---- |
| 0    | foo  | 1    | 4    |
| 1    | foo  | 1    | 5    |
| 2    | foo  | 2    | 4    |
| 3    | foo  | 2    | 5    |

### append

向 `DataFrame` 中添加行：

```py
df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])

df

```

|      | A         | B         | C         | D         |
| ---- | --------- | --------- | --------- | --------- |
| 0    | 1.587778  | -0.110297 | 0.602245  | 1.212597  |
| 1    | -0.551109 | 0.337387  | -0.220919 | 0.363332  |
| 2    | 1.207373  | -0.128394 | 0.619937  | -0.612694 |
| 3    | -0.978282 | -1.038170 | 0.048995  | -0.788973 |
| 4    | 0.843893  | -1.079021 | 0.092212  | 0.485422  |
| 5    | -0.056594 | 1.831206  | 1.910864  | -1.331739 |
| 6    | -0.487106 | -1.495367 | 0.853440  | 0.410854  |
| 7    | 1.830852  | -0.014893 | 0.254025  | 0.197422  |

将第三行的值添加到最后：

```py
s = df.iloc[3]

df.append(s, ignore_index=True)

```

|      | A         | B         | C         | D         |
| ---- | --------- | --------- | --------- | --------- |
| 0    | 1.587778  | -0.110297 | 0.602245  | 1.212597  |
| 1    | -0.551109 | 0.337387  | -0.220919 | 0.363332  |
| 2    | 1.207373  | -0.128394 | 0.619937  | -0.612694 |
| 3    | -0.978282 | -1.038170 | 0.048995  | -0.788973 |
| 4    | 0.843893  | -1.079021 | 0.092212  | 0.485422  |
| 5    | -0.056594 | 1.831206  | 1.910864  | -1.331739 |
| 6    | -0.487106 | -1.495367 | 0.853440  | 0.410854  |
| 7    | 1.830852  | -0.014893 | 0.254025  | 0.197422  |
| 8    | -0.978282 | -1.038170 | 0.048995  | -0.788973 |

### Grouping

```py
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                          'foo', 'bar', 'foo', 'foo'],
                   'B' : ['one', 'one', 'two', 'three',
                          'two', 'two', 'one', 'three'],
                   'C' : np.random.randn(8),
                   'D' : np.random.randn(8)})

df

```

|      | A    | B     | C         | D         |
| ---- | ---- | ----- | --------- | --------- |
| 0    | foo  | one   | 0.773062  | 0.206503  |
| 1    | bar  | one   | 1.414609  | -0.346719 |
| 2    | foo  | two   | 0.964174  | 0.706623  |
| 3    | bar  | three | 0.182239  | -1.516509 |
| 4    | foo  | two   | -0.096255 | 0.494177  |
| 5    | bar  | two   | -0.759471 | -0.389213 |
| 6    | foo  | one   | -0.257519 | -1.411693 |
| 7    | foo  | three | -0.109368 | 0.241862  |

按照 `A` 的值进行分类：

```py
df.groupby('A').sum()

```

|      | C        | D         |
| ---- | -------- | --------- |
| A    |          |           |
| ---  | ---      | ---       |
| bar  | 0.837377 | -2.252441 |
| foo  | 1.274094 | 0.237472  |

按照 `A, B` 的值进行分类：

```py
df.groupby(['A', 'B']).sum()

```

|       |           | C         | D         |
| ----- | --------- | --------- | --------- |
| A     | B         |           |           |
| ---   | ---       | ---       | ---       |
| bar   | one       | 1.414609  | -0.346719 |
| three | 0.182239  | -1.516509 |           |
| two   | -0.759471 | -0.389213 |           |
| foo   | one       | 0.515543  | -1.205191 |
| three | -0.109368 | 0.241862  |           |
| two   | 0.867919  | 1.200800  |           |

## 八、改变形状

### Stack

产生一个多 `index` 的 `DataFrame`：

```py
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                     'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two',
                     'one', 'two', 'one', 'two']]))

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])

df

```

|       |           | A         | B         |
| ----- | --------- | --------- | --------- |
| first | second    |           |           |
| ---   | ---       | ---       | ---       |
| bar   | one       | -0.109174 | 0.958551  |
| two   | -0.254743 | -0.975924 |           |
| baz   | one       | -0.132039 | -0.119009 |
| two   | 0.587063  | -0.819037 |           |
| foo   | one       | -0.754123 | 0.430747  |
| two   | -0.426544 | 0.389822  |           |
| qux   | one       | -0.382501 | -0.562910 |
| two   | -0.529287 | 0.826337  |           |

`stack` 方法将 `columns` 变成一个新的 `index` 部分：

In [68]:

```py
df2 = df[:4]

stacked = df2.stack()

stacked

```

```py
first  second   
bar    one     A   -0.109174
               B    0.958551
       two     A   -0.254743
               B   -0.975924
baz    one     A   -0.132039
               B   -0.119009
       two     A    0.587063
               B   -0.819037
dtype: float64
```

可以使用 `unstack()` 将最后一级 `index` 放回 `column`：

```py
stacked.unstack()

```

|       |           | A         | B         |
| ----- | --------- | --------- | --------- |
| first | second    |           |           |
| ---   | ---       | ---       | ---       |
| bar   | one       | -0.109174 | 0.958551  |
| two   | -0.254743 | -0.975924 |           |
| baz   | one       | -0.132039 | -0.119009 |
| two   | 0.587063  | -0.819037 |           |

```py
stacked.unstack(1)

```

|       | second    | one       | two       |
| ----- | --------- | --------- | --------- |
| first |           |           |           |
| ---   | ---       | ---       | ---       |
| bar   | A         | -0.109174 | -0.254743 |
| B     | 0.958551  | -0.975924 |           |
| baz   | A         | -0.132039 | 0.587063  |
| B     | -0.119009 | -0.819037 |           |

## 九、时间序列

金融分析中常用到时间序列数据：

In [71]:

```py
rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
ts = pd.Series(np.random.randn(len(rng)), rng)

ts

```

```py
2012-03-06    1.096788
2012-03-07    0.029678
2012-03-08    0.511461
2012-03-09   -0.332369
2012-03-10    1.720321
Freq: D, dtype: float64
```

标准时间表示：

```py
ts_utc = ts.tz_localize('UTC')

ts_utc

```

```py
2012-03-06 00:00:00+00:00    1.096788
2012-03-07 00:00:00+00:00    0.029678
2012-03-08 00:00:00+00:00    0.511461
2012-03-09 00:00:00+00:00   -0.332369
2012-03-10 00:00:00+00:00    1.720321
Freq: D, dtype: float64
```

改变时区表示：

```py
ts_utc.tz_convert('US/Eastern')

```

```py
2012-03-05 19:00:00-05:00    1.096788
2012-03-06 19:00:00-05:00    0.029678
2012-03-07 19:00:00-05:00    0.511461
2012-03-08 19:00:00-05:00   -0.332369
2012-03-09 19:00:00-05:00    1.720321
Freq: D, dtype: float64
```

## 十、Categoricals

In [74]:

```py
df = pd.DataFrame({"id":[1,2,3,4,5,6], "raw_grade":['a', 'b', 'b', 'a', 'a', 'e']})

df

```

Out[74]:

|      | id   | raw_grade |
| ---- | ---- | --------- |
| 0    | 1    | a         |
| 1    | 2    | b         |
| 2    | 3    | b         |
| 3    | 4    | a         |
| 4    | 5    | a         |
| 5    | 6    | e         |

可以将 `grade` 变成类别：

In [75]:

```py
df["grade"] = df["raw_grade"].astype("category")

df["grade"]

```

Out[75]:

```py
0    a
1    b
2    b
3    a
4    a
5    e
Name: grade, dtype: category
Categories (3, object): [a, b, e]
```

将类别的表示转化为有意义的字符：

In [76]:

```py
df["grade"].cat.categories = ["very good", "good", "very bad"]

df["grade"]

```

Out[76]:

```py
0    very good
1         good
2         good
3    very good
4    very good
5     very bad
Name: grade, dtype: category
Categories (3, object): [very good, good, very bad]
```

添加缺失的类别：

In [77]:

```py
df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
df["grade"]

```

Out[77]:

```py
0    very good
1         good
2         good
3    very good
4    very good
5     very bad
Name: grade, dtype: category
Categories (5, object): [very bad, bad, medium, good, very good]
```

使用 `grade` 分组：

In [78]:

```py
df.groupby("grade").size()

```

Out[78]:

```py
grade
very bad     1
bad          0
medium       0
good         2
very good    3
dtype: int64
```

## 十一、绘图

使用 `ggplot` 风格：

In [79]:

```py
plt.style.use('ggplot')

```

`Series` 绘图：

In [80]:

```py
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))

p = ts.cumsum().plot()

```

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXgAAAEQCAYAAAC6Om+RAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAIABJREFUeJzt3Xl8VNX5+PHPudmXyUwSEpawLyoEQRRcigqi9WvVSvzWxha1gm21VStS1+oPxKJ1KyJaldZau9jWYtV8tbVqWwEVN0BUCIsgi+wh22Qme+ae3x93MpN9YZJZn/fr5cuZe8+de2ZueObMuec8R2mtNUIIIaKOEeoKCCGE6B8S4IUQIkpJgBdCiCglAV4IIaKUBHghhIhSEuCFECJKxQdy8MGDB3nsscd8z48cOcLll1/O2WefzbJlyygtLSUnJ4cFCxaQlpYWcGWFEEL0nOqrcfCmafKjH/2IX/ziF7zxxhvYbDZmz55NUVER1dXVXHHFFV0eX1xcTH5+fl9URYQ5udaxQa5zcHT1OfdZF82mTZsYNGgQAwYMYP369cyYMQOAmTNnsm7duh5VUsQGudaxQa5zcHT1OfdZgF+7di3Tp08HwOl04nA4ALDb7Tidzr46DdDzP5xoKRdt5+6NnrxmNH02kXDucL/OvSkb7uV6W7atPgnwTU1NbNiwgTPOOKPdPqVUX5yilXC/KNH0j7m/XrMvzx1Nn00knDvcr3NvyoZ7ud6WbatP+uDXrVvHW2+9xd133w3AzTffzOLFi3E4HFRUVHDvvfe2uhkLVqVbVrywsDDQagghRExauXKl73F+fr6vT75PAvxjjz3GSSedxMyZMwF4/vnnSU9Pp6CgoMc3WcEalSOin81mw+Vyhboaop/JdQ6OIUOGdLov4C6auro6Nm3axGmnnebbVlBQwKZNm5g/fz6bN2+moKAg0NMIIYTopT4bJtkXpAUfG6RlFxvkOgdHv7bghRBChCcJ8EIIEaUkwAshRJSSAC+EEFFKArwQQkQpCfBCCBGlJMALIUSUkgAvhBBRSgK8EEJEKQnwQggRpSTACyFElJIAL4QQUUoCvBBCRCkJ8CKk9IGv0HU1oa6GEFFJArwICW2amK/8CXPxjeh//C3U1REiKkmAF6HhrkK//qL12OMJbV2EiFLxoa6AiD1N2zdBTa1/g7sqdJURIopJgBdB577nJhg+2vdcu2XVHyH6g3TRiNCoKPM/rq0OXT2EiGIBt+Crq6tZsWIF+/fvB+D6669n8ODBLFu2jNLSUnJycliwYAFpaWkBV1ZEPv3JB9YDl9O/sdodmsoIEeUCDvDPPfccU6ZM4ZZbbsHj8VBfX8/LL7/MpEmTmD17NkVFRRQVFXHFFVf0RX1FhNOH9kFKKtTWoK69HTVyLOaDt4e6WkJEpYC6aGpqati2bRuzZs0CIC4ujtTUVNavX8+MGTMAmDlzJuvWrQu8piI6uJwkX3ol6qzzUVNOA0cW1LjRWoe6ZkJEnYBa8CUlJWRkZPDUU0+xd+9eRo0axdy5c3E6nTgcDgDsdjtOp7ObVxIxw1mBkX8SxjkX+7clJEJ5KWTnhK5eQkShgFrwHo+H3bt3c/755/PQQw+RnJxMUVFRqzJKqYAqKKKLdpZjOLJab6ytwbzz+6GpkBBRLKAWfHZ2NllZWYwdOxaA008/nVdeeQWHw0FlZSUOh4OKigrsdnu7Y4uLiykuLvY9LywsxGazBVIdEQGqXFUk5gwkvsW1rvT+Pz0lBRUvI3ejRWJiovybDpKVK1f6Hufn55Ofnw8EGOAdDgcDBgzg4MGDDBkyhM8//5xhw4YxbNgwVq9eTUFBAWvWrGHatGntjm1ZiWYul4yHjnZmRRmeNBvuFtfaePBZzIU/xlVagkqTgBAtbDab/JsOApvNRmFhYYf7Am4uzZs3jyeeeIKmpiYGDhzI9ddfj2maLFu2jFWrVvmGSQqha6pBm5CSBm7/0EiVnQM2O9TWgAR4IfpMwAF+5MiRPPDAA+22L1y4MNCXFtFm/x4YOrLj+zIpqSBZJYXoUzKTVQSNPrgXlTei453JKVBb2/E+IcQxkQAvgqe8FLI6GQopLXgh+pwE+Biha9zoDWtDW4mKUsga0OEulZ6Bdsl8CSH6kgT4GKHf+w/miofab692B7SikjY96OKNPSt7+AAqZ3DHO7NyoPzoMddDCNGeBPgYof/1YofbzeWLMW8/9klG5nWXYj52T/flXnwO9uyAkWM7LpCVY3XhiH6jXU7MN18JdTVEEEmAjwG62g3enOu6tk1rvbYaaqs7zQWjd21Hd7LiUstjdGNj13V4ywosKiGxw/0qKwddJi34/qQ/fgf99+dCXQ0RRBLgY8GBPf7H2z9vva85Va+zosNDzQduQ3/wdof79Op/+R8/9xi6puO0v+bq1wEwblrUeR2zc+DgXrRpdl5GBKZORinFGgnwscDtguNPRM26GH1ov2+zdldBUyMcNxEO7m13mC/YHjnYfl9VBfovK1Dfnmc9X/cuetXrHZ5er3sP40d3oE6c2nkds3Kgshz9wapevDHRK/US4GONBPgYoGvcqAG51mzRujoAzD8/jd74IQwfg8obgT7wVfsDq6wsMfrTD/2vVe1CV1VgPnK3tSHNhnHrL1AzLkDvKEab/u4c3dSE+cqfYN9uOO7ELuuoklPgpNPQRc8HlDpYa211SYl29JfbelTOs+JBPMu6v68iwp9kdooF1W4rBUBSMrir8Nz0HSstQHYu6rxvWhOMqtvnDNGb1sNx+bBruxW4y0sxf/ZD34IdAMqehTp+Igwdgb75CszrLiXumVfR9fWYi663RsbY7ChbRrfVVPZMdGUZOMvBkX1Mb1V/8Db6ueXEPfPqMR0fjrTHA4YReGbWvbsAMN//L8bXzu283CcfgOTnjwrSgo8F1S5ITbcCfH2dLzhTVoLKzIHEJGiob3eYfuNljPP/F9IyoLLCv45q8/FTTkdNPBmgVZIwXVMNB7/yDXs0fnBLz+o5ZLj1/4Md/JroKe9Yet1Bt1KkMhdcgX7p9wG9ht6/B7T160r/eUU3hSW4RwsJ8LGgxg1pVoBvvhGqLvy2tc+R5QvwuqkJ/cVmwNv/Xn4Uxk+CEWPQ2z6z+uubpaZhfO/Gjs9Xehh92N/Xryac1KNqGrMuRp0+E73l0153s+iyo3iuLfB9CZm/f7xXx4e12hr07h0BvYR5703Q0GA9iYvr/oD4hIDOJ8KDBPhY4O2iUckpVgBMz0ANH23ty86FpCT0mjcwly3CfOQua3vpEUhJRSUmocZPgq92QU21/zXraq38MS0Ydy2FkeOsiU/HOmkpJRX95ivoN1/qcLf5wSr03p3ttustG0Gb6P++Zm1ITDq284erLzajm7oeitqZ5i914/YHrQ25Q3py1DGdS4QXCfBRSrucmN4RKbrahWruoik/avXHjzoOdfo5KEcWqjkYelvvAObd1/m6O0i3g8tpBYrho610v0Ycqk0rT40ah3H599EfrbGGXY6bgPrmd3pX8ZR0q87v/afDgKZ/twzzb79tf9z+PdDcXTTzGx3eU4h4Wz87tuMO7oOho1DjJmDMX2z9muuArnZb8yQSkyAuQW5WRwEJ8FFKf7Qa/btl1oiUmmrrH3WGwwq8GXZUVg7G9715+tu0dn2jLWzWSlzKZrdufpaXokaMtSZHtWm9+wwbAwf2olf9EzXjGxiXzOldxeO8f5ID86D4047L7NjSfmKVy4kafYL1OGdQh/cUIp35zC+7LdPRPALzoTusawbWl7u7quPXv3kO+u1/WJ/fwCFw5EBA9RWhJwE+WsVZrWv98TtWazbNBoPyAFDDRrcu2ybAm4/fi7r4coy7vAHFlgFfFKP/8QLqlOnWtk4CvEryv5Yac0Lv6+391aCGjUKXHm5dr//+w//kyP5W+3S1G+W9SasGDIqaMd++PEED82DwsG7Lm9cVoMtKrGP37kR/4V0Ws3k28sDBcORQpxPK9Pr3rC/xrAFQWRZw/UVoSYCPVs5ysGei/7kSqirAkY0y4jDueRx10bdbl01KBsD46RLUmV+HmmrUhd9GDRho7c8e6C/bfMPU6PpGnZp5of/43hg5DnIHgz0TKstb7dI7/F1I7cbt17gh0zu0MmsAlJeGPntmX9jyGYyfjPHjO/2jlzrhmz/gbaGbL/wW85GfeXdaAV2lpkNaGpQc6vhF9u+BvOEoRza6QgJ8pJMAH4U8v7oP/c+VqOlfh9Q01GXzUAlWi14NHYnKyGx9QKY3hW9yCmrmhZCU0ipnjPL22Rrz7/GPxe5uTLb3S6O3jOnnEXf/r8GRhX7jJV9LU9fXwbZNGA8/h5o9Bw60mXnrHQpqPPwc5I0EvAnOIpyurUY5sq1fTHW1XU8Ca7RGyeh9u70H+1vpxvd/6i9XXoq58MedvozKGWyNrmrzBSsijwT4aPTZxwCoMccTd+fDGOdc1GVx5chCnXo25A5GjRhD3K/+1q6Msex5yD+5xUFdvN6V16PO/eYxVd33Gs1pDbytVr1+LYwdj8rMRg0ZgW47Vr6m2hoplJkN8d75e8c46iSs1FZDahokp0JFKbro+Q6L6b1fWq1vQP/hCWtj832IEyahxk/2F54wpf3xLb84Bg8Dm936gt25pS/ehQiRgGey3nDDDaSkpGAYBnFxcTzwwAO43W6WLVtGaWmpb9HttLS0vqiv6IbZMgA4snp8nPHDW7vcr9LbzkTtPMIbMy7o8Xk7PV+Gw+qqcVdZN4i/2Iya5A36eSNateC1afoDIfh/ZXTTpRHudGUZ+uN3UflTfPc89A6rT1031MPRw74lEM37FsCo4/zH1tdDqdUX3/amqvGjOzBvm9f6ZJ4mUArjrl+iBuXBwa/QgD5yCDV2Qv+8QdHv+iRVweLFi0lP9w+9KioqYtKkScyePZuioiKKioq44oor+uJUogv68AGrz71ZZ8vj9QV3EFZfSs+wWq3xCWh3FYbd+4WVMxCcFej6euumbl0tJCahWk7gGX28b9KTr1yE0St/B7u/gKnT/e9NGejtmzF/ac1XMH7zf/75CYb/B7n+5wtWgrm4OBg8tPULJyVDfS2eZYuIW/Bza1tDvdVFN3Kc9Twl1Xu+ANMjiJDqky6atv2C69evZ8aMGQDMnDmTdevW9cVpRDf0Nn8qYOPXRR20uvvIcfn9++XRLM2G+ZtHMO/8vjW8M8XbQjfirODf/CVT482104IxfzHUuDFXvY55Y5ubyhFCe5O9kWS13o2b7wWl0J9/7C9UVQlbvcNJ9+yAU75mzVj+10sY3/kBxo/uwJjdunGlmr8ItviHoerXXmj9i6f5HkxNFM4niCEBt+CVUixZsgTDMDjvvPM477zzcDqdOBwOAOx2O06nrLUZFLu2oaadhd6zw/+PuB8YC34elHwlavTxVsIzgL07fV0wgHc8t8uaiVvtbr0PvC1QhX7vrX6vZ3/Q9XXw1ZcYP1lo/RoBK59QXW3rPDsH9mL++mHr86h2obJz0cmpUF+Hys7t/jyuKthRjP5Pm+RsY05AnXEOuDoeMy8iQ8ABfsmSJWRmZlJVVcWSJUvIy8trtT/gDHiix/SX2zF+fAfG0FH9ep62M1j77Twnn4H+vz/7N6S0COKpqej9e1AjxkB1ldWib3msUtZtgq929ehceu+XoE18XRShVvyJNdt40jT/tmRvsriSQzBpGny+zkrlnDcC4+bF6A3vW+WrnFbqhh4wf3ql77E623/vRCmFHn0C7OvZ5yfCU8ABPjPTGnKXkZHBqaeeys6dO7Hb7VRWVuJwOKioqMBut7c7rri4mOLiYt/zwsJCbDZbu3KiZ0yXkypXJbbj860ujDCWmJjYo2uth4/CCSSe900a/vMattyBKG9LvfKLYvQXxdguKKDeWY5nyDBS27xm/dyfULviYYBuz1f1xycwv9qF44XwWHCkzu3EHD661Xsy6wfgqq9DV7uwP/BralY8hLl3J/GTp5EybCQMGwmA/snd0Nhg5R7qRGXbDQkJ2K+/o9WmhtyBNH6xmbRj/HfZ0+ssArdypf/eW35+Pvn5+UCAAb6+vh7TNElJSaGuro7PP/+cyy67jKlTp7J69WoKCgpYs2YN06ZNa3dsy0o0c7mkv+9Y6S2fw7BRuKvDf+SIzWbr8bVW1yyg6dSzMU6Zjttjgvc4Nfcm9O8fx+Vy4fn3q6jTz2n3mnqi/++uqqqqy1+TpjctQ7j8DZqHDkBmdqv66CYPuqIUMhy4G5sw0zLQu9ZgnnEuTR3Vu7GL95KSZqWuaE5H0NjY/vOLT8SsLDvmz6Q311kcO5vNRmFhYYf7AgrwTqeTRx55BADTNDnzzDOZPHkyY8aMYdmyZaxatco3TFL0L+1ytp/AFAWMM86xHrQZqqfOmIX+62/Q5Udh327U7Q+0O7bVyJmG+q4nX3l/9eiSg6geZVvsP7r0CPrQPn9unWbN7ydnkPV/u3W91ekzen0OY8lT1g3bF55Br3u340LpGdIHH+ECCvC5ubm+AN9Seno6CxcuDOSlRW9VuyA9dn4OK8NAnXo2+t1/W8P7klM7LGc8+FvM+2+xRoh0FeC9KXXNFQ8Rt2h5f1S5x8yf/RAA9c3vttruu/fhnd+gTjwFDu3v9L13RTV/OVx7G57OArzN3mliMhEZZMm+aOF2tRsqGPWGj7HyzXTxvlV2rjUOfP+erid+OSusFarsPZ8c1u86G4rqXbhDDR2FuubmgE+jpp7Z8Xj3tHSorUabnrC/ryM6JqkKokUHY8GjnRoyDHZs6fZ9q1HHd7hISDPd2ACV5VZ6hLrQZqHU9S3SHNsd7fariy/HmNV16oneMq67HePa29qfy4izhptWV3dwlIgEEuCjhav9UMGoN3i4NcW+u/edOxiOdpI9EeDQfsgZhErPQNeGNpiZzy61HgzM67DVbMy+AjXxlOBVyDuhzHPPjf4kZiJiSICPEtpVaeVviSHK5g3s3UzqUjmD0EePdLpfr34dNW6CL2NjSDU2YvxkIXH3PR3aejSze7NKHvwK8+fz/YvBiIggAT7CmW++jN68wVoowxZjLfhm3S3ukZ7R6RJ+5jO/RL/7Fuq8S6zZsCFuwXe01m0oqexcdMvJTtG4FGIUkwAf4fTff4/59997A3xsteABa13ZM2Z1XaiTlrnW2lrxCmDQUBgwCL7ahfn2P9qVDZr6Wl/umbCQMxD94WrfU/PPK2QhkAgiAT6C6eZFsWurreFsMdiCN76/AOOs87sulOSd4g94HrkLXXbU2u4dAqjOOh+llLWwyZgTYO+X/VnldvTWz6w1b8GqZzi14KeeCS373suPwq7toauQ6BUJ8BFMv/xH64HbBUnJQcsRE3GaV0MyPfDFZsw7v48+ehhKj8DwMRjfu9FXVH3tXIgL3pBArTXmowsx//iktaGu9phXw+oXDu8yiC3qpKNhIZUYIQE+gmjT0yo1s652WS2shnr/6j2ivYREMD2YC2/wbzv4Fbr0CAxok3Ex2DdaS703f5vHodfXWUnFwkVzYD9uojUaCWTyUwSRAB9BzFvnol/+I7r5H1i1y1okG6CpKXQVC3NKKTBNKLHS7KrzLsH8++/Rv3mk3cLgKiUVHcSVoPSXW60Zo7XV1spUDQ2QGD4B3pe/xzCsVb9GH2/9YhQRQQJ8BNCmieeHl4DLif7sY8wFV6Kr3dbYd0cW6vRzMO54MNTVjAjGwmUwMA8O77c2DGqz2lFyKtQFJ8Br00T/4VeoiSdDbS001EFiYr/m8g+EGjkOddoM9K7taI8n1NURPRCef0mitbIS/+ND+wAwb/me9TjNhvH9BbJuZjfUlddbD4YMR2UO8G8fO751weSU4K3lWuOGpkbUzAutG+V14XWDtSVf6uE0G2zZ2HppSBG2JBdNJDh8oP02j7dLJtZmrx4rb6tYxSegTzwZ495foYYMb18uawCUlaC17jS9sPnv/4PSIxjfvTawOrmc1q+J3MHWOT9+J7xusDYbfTxq1sWANblMA/q1v6KnnYVqu96rCCvSgo8A2ttqb6bmXOd/HC/f0T2hTp+JcdsvrMdGXMfBHVBpNqsVXV7a6Wvpt/+B7oux8i6n1f/uXalKb/00LFvwcT97BNVy2UAvvXlDiGokekoCfCRo7i8GjKdftpJiiV5RCYmo4yb2rHDmAKjsYjJP84LUgXJZcxdUXBzq7P+BzZ9Y48zDWfPC53N+5OsuFOFLAnwEaDlzUMXH+8YmGzfcHaoqRbc0my8/fIe8AV43NgR0Gu1yorwrSZHoXcwjzEeoqIFDMB5/AZXhsBbsFmFNft9HApfTWr3HWQFYQd5YtBw1rH8X145VKi3dmmPQWQHvwirm9Zdh3LgQNbn9kpQ94nJCuhXg1cXfgewcqHIe22sFkUpJRdvs4Gq3sqsIM9KCjwTuqnaLP0hw70dpNqjuogXvrEBdNg8A81dLjv08LidkeAN8WjrGebMx/vd7x/56wWSzy3J+EUACfJjTpgmuSozCa1DfujrU1YkNaemddpXo2ho4etjqM/fy3PBt9PZNXb6kL/8NYK79L56fXO5twUfoKKj0DJnRGgH6JMCbpsntt9/Ogw9ak23cbjdLlixh/vz53HfffVTLijDHbvsmyM1DjZ2AccG3Ql2b2JA5oNObnfqDt1EnTkWlpPqn7jfUY/6y8/shuqzEyn+zfRP68H7075dbuXG2ftZuJm3ESLEmhLVMnSHCT58E+Ndff52hQ4f6xg0XFRUxadIkli9fzsSJEykqKuqL08Qkve5d1BkzQ12NmKIGDLTy1HSkogyau8fazObsLNjpnVsBMP/0FOZC74SrseOt3OqDh/VJnYNNxcdDfIIvS2cw6PJSzPf+DYD5wjPoRkl61p2AA3xZWRkbN25k1qxZvj/w9evXM2PGDABmzpzJunXrAj1NzNIlh1DDRoe6GrElO7f17OGWql2+tMzGj+5AXXu7f19NJ79USw6hpp0FRw7A5FMxblrk65pRqWl9WfPgSknr/D33A/3OG+g/PIH2eND/fa3zayR8Ag7wf/jDH7jyyisxWuTPcDqdOBzW4hN2ux2nM/xHBoStijJ/ylYRHBkOcFV22CLX7ipUmjc4jxyHMe1MjEefh/h4qOpkVElZCZwwyTpm4BDUiVMxTj8HdeqM/noHwZGaFtwVnryTrPRrf7Wey+pS3QoowG/YsIGMjAxGjRrV6c/TzqZ7i+5pra0JN5lZoa5KTFHJKdDQgPnzm9EtsnSab74CWz/zDZP0lbdlwJjxUFZiLU697fNW+3VFKSprAGrmN6z0zoA65WsYP7yl/99Mf6qtsdZpraoIzvkSvfMPvHlwzDdfDs55I1hA4+C3b9/Ohg0b2LhxI42NjdTW1vLEE09gt9uprKzE4XBQUVGB3W5vd2xxcTHFxcW+54WFhdhstnblYpmuceOMiyMjJ0JvxHUiMTEx7K91JcD+3aTs30X8hJNAa5x/fw4jdzC2/JOsm6wt1E6YDHt3UH/wK+KLP6Hpxd+R8fCzAFS5q0gdPJT4KLuX0vTTe3EvupGU0sMk5LVP/dDX17nyzysAMHIGYR49DBs/DPu/o2BZudKf/C0/P5/8/HwgwAA/Z84c5syZA8CWLVt49dVX+clPfsLzzz/P6tWrKSgoYM2aNUyb1n4iSMtKNHO55CdXS/rgV2DPirrPxWazhf17Mhb8HPNff6dmz070a3+zulkSEmHJ07ibPNCm/npgHuba/wLQ8IbVsqw6dACVnoFZWU5NXAIqzN9zrw0eDid/jZqyMowO3ltfXufmX1Jq6pmo627HOLQf8/F7w/7vKBhsNhuFhYUd7uvTcfDN3TEFBQVs2rSJ+fPns3nzZgoKCvryNLGjsgwc0j0TCmrCSajRx6P/vAI+XwcH9sKIMZ3nas8ZDF9ua73t4D5rmcBqlzUxKAqplFQr1XF/q7ECuW5ebSvDHtQbvJGqz1IVTJgwgQkTrJzk6enpLFy4sK9eOmZptwsVqRNhooAaNoqWd5ZU/smdFx6Y1zp/zXET0c4KlNsFKamoIK7zGlQpaeg/PYnOHIA68ZT+O4+3pe7rGktJhRo3+tB+1OChmH94AjXtLNSEk/qvDhFIZrKGs8aGvstcKHpvyhkYdzyI8fgL1nN7ZqdFVVKS7yYggBoyzMrV4nKCzdHfNQ0db8DVO4q7KRig6irIGYT6nrWurjKsL0xz0fVoZwX6vX9jLlvUv3WIQBLgw1lDQ6ugIYJLxcWhxk7wtxq7W0ovyZvLffxkyMi0gntVpTXsMlo1fzb9vYSfuwryRqKSU9vtMp991PdY18vi8y1JgA9njfWQkBTqWgiAvBGokeO6LuNN+Rv30yXWZKgqJ7qqEhXFAd63VKSr87kuevMGtHfMujZNPHddi1n0fOezhTt6DXeVNRy1BeOupdaDrZ/5y61+vcevGQskwIczacGHjbjFT6DyRnRZRk04yeqLB39O+aOHrJmxUUqNGodxw93oTnL3mH96EnP5veiNH1ob6mrh6GH0P1di/uyHPT+Rq6rd/ANarMpl3Pj/rARwksK4FckHH84a6v0LQYiwp666AeWd8KdS0jAry2D9e6hrFoS4Zv1syHDopDWuN20Apfzpl2trrHVvu1gSsdXxjQ0QF2dl92w74c/b+GnOya/dVVZyPuEjLfhw1igt+EiilPIPo0xLh51bIT4eNfnU0Fasv2UNAGc5uqN++NQ01GkzobLMmpldVwPJqRjzF8Nx+e3Lt2HePg/9wm+tIcMZrW9yK6VgzAkwzuomUsmp6A9WBW9mbQSQAB9kuqIMfWBvzwo3NEgffKTyrl1q/OCWyE4o1gMqPsEaKdTROra11TBkGFSUYd59Hebff2/dmE1Lt/6+u6B3bQe3C731M/TuLzrsIou782H/5zt2vPX/o+1/TWit0ZXlvX1rEU8CfJCZv1+Oufgn6Abrbn+X+bQb66UFH6nSrMRYdDV2PprkDkZvWu97qivLaNq9A2prUIOHoctK4Ohh2LzBSjOcmAT1dR3+/XuW/j/Md95Ae1MDc3i/lZZ40NAuq6DsmTDldPT7b6PbpjH+fB3mbXMDfZcRRwJ8sHnXVTV/dR+6qRHz2tnoFqMAmum9X6I/WGUlvhJI3vudAAAgAElEQVQRR9nsGEuejpnrp6ZOh13bfc/Nv/wa98+utfrcBw2FvTuthVTsWVBZbgX42mrMW6/GXNVm5Mu2z9H/egn98Tuoq7zj3k88BZWQ0H09BgxEv/MG5o2Frb48dG1N37zRCCMBPtjcVajvXAtbP0O/9EcAdFUlnpuvaBXofcO9uhuaJ8KWGpQX6ioEjcpw+NMIQOsZ2FkDQGuwZWA88AzGnQ9BUpIV6KsqW7X8fUqPQH0d6qzzvS/Ys1BlFH7f99i8dja6shy9Z4dvDkPb+wT6y214HrydaCUBPoi01uB2oc48z3q+9VNrR0UpVLvQRw/5C3ua4JSvoaJ4iJ2IIskp1hDIZt7c7QCqeSSYMlAJCVbwb942bgJsWo/n/japk0eMxbjjQV9+K13TxSLobbXoqzdvm4t5/y3+laeqW68jq9evhS+3RW0LXwJ8P9N1NZi/9U7I2LwB0tJRScmoS6+yEljFxfvX/2yxSr0+uA/j65KkTUSI5NTWAb6uhuTv/hDjwd8CYNy9FOPHd/r3ewO8Ot5aCIU9OwCsCVEpqRh3L/VPogJUL5LuGQsfa7/Rm5hMb9/cut/fYy37Z94+r8evH0kkwPe3PTvRH7+D9ngw3/s36n+/B1irAQGoaWehy5oDvDUbUNfXwaF9rSZyCBHWUlKt/nZANzaiy0sxsnN8v0DVyHGtfo0qIw7jyRetyUlensfuwVx8k3VjtsVCQcbjL6Au/0GPq6Li4mDiya0nRnlb7vo3j2A+eT/mK3+yttfWoM44x7rxG4UkwPeCPrAXzw8v6d0xe3da/Y8uJ5QdRXmDtppwEsZTL1lB/HPvmrXeFrx+4RmYMKXdohJChK0kfxeNXv06bFqPatFN0xGVmNQ6CBdvhMoy36pXvnIpqdZQzF6Im78YVXCV77ne2mKVrc8+Rr/+orW9tsYa6dQQvMXDg0kCfC/oY5klt9v66Wn+bpk1kiDN/wetEhKgxcgA7apE19ag3/s3xqyLAq6vEEFjs0N9LdpVBU2NMOEk4nuQPlglJGLccHfrbd+9tk+qpJqHVeaN8HUBtaT3fglbP7OGVzY1tVqeMVpIgO+Nr3b1+hC9d6f1oHmETNt8GqZ1V9+465feVn4JDB6GGj85kJoKEVQqIcEa8bV7u9XtcdxEVA9TXauTTsO47QGMG+7GuGtpnyVnU8dPJO6ZV33PjUXLUWd+3ffc/M0jVjqQdJs1MS0Kb7RKLppuaI8H/cn78EUx+uN3rG37d6M/XG39EU9qvxyh79jaGitoH3+iP0dGm3Sn6rxLUDMutBJT7d+D+dpfITun396PEP1FZQ5AOyusQNnLlchUD9IWHCvj6p+AUqhho+DK6/0TqDxNqGlnQd5I7z2EaisLaBSRFnw39Eer0a/+xepXbGyApGTMe+ej33wF87+vdX1wTTWkpmP86A7fprZLvikjzlosovkP65MPUJkD+vptCNH/7JngLLcCZUr4pGdQo47DN6ghLg71w1th6CgoK0Gd/T/WDV17pvXrOcpIgO/Ozq2ocy/BWP4XqxvF06KfrrsFIBrqICnJN+lDXfCtTouq+ASMB5/tixoLERr2LHBa95HCeYCAcerZGIseg5PPsFrvgBozHt12Td0oEFAXTUNDA4sXL6axsZGmpiamTZvGnDlzcLvdLFu2jNLSUnJycliwYAFpaeHzjd4TeucWzGeXgSMb47QZ1oiAUcdByxsxmz9Blx5BDRjoP678KNTWovKGt073m2ZDjTmhy3Oq5q6ZaF7iTUQt5cjC3P65NXHPHt6LxSuliPvxz/wbsnLgyP7QVaifBBTgExMTueeee0hKSsLj8bBo0SK2bdvG+vXrmTRpErNnz6aoqIiioiKuuOKKvqpzv9O1NZgPeSdlmJ7WCzbExbdqxZsrnyXu+rv8z1c8BLu/sG7u1NdBYrJ12GN/7tG5jaV/hCjPPiiilD3TSj9w5CBEWpqGtHT0wX1orVuNwY90AXfRJCVZLdSmpiZM0yQtLY3169czY8YMAGbOnMm6desCPU1Q6Q/e9j9ps6Zm3IqXUXPno2bPsfJk7NyKbs513fI1qiqtu/S9pDIcvR7zK0RYsGfC7i+sxbHDuIumIyrNZg2E+OT9UFelTwU8isY0Te644w6OHDnC+eefz7Bhw3A6nTgcVlC02+04nZ2v1xiWSo+gvj0P/frfrTvtbVZVMqafC4A2Peh338K8bR7Gzx6B0cf7bi7p116wMke6XUGvvhAhkZWDuvhy1NSzQl2T3vP+G9f796JOmR7iyvSdgAO8YRg88sgj1NTUcP/997N58+ZW+yPy505drZU8yWb3jVPviDLi/E+aFx2urQZHNnrLRuu5J/omTwjRERUXh5odOV2xrTTfR4uyNV37bBx8amoqU6ZMYdeuXdjtdiorK3E4HFRUVGC329uVLy4upri42Pe8sLAQm83WrlwoVDc1kuDIoj4zC0yzy3o1/zkkexpJtNlwOiuIP34ijR+tsXYoI2zeV7hITEyUzyQGRNR1ttlouPkeGt9fRVqk1LmFlStX+h7n5+eTn2/NKwgowFdVVREXF0daWhoNDQ1s2rSJyy67jKlTp7J69WoKCgpYs2YN06a1nwzUshLNXK7w6M7wuF14tMJMTQete1Sv2vJS6pxOtLOCpmGj4aM1qO/diJo0LWzeV7iw2WzymcSASLvOOj4Rs7IsouoM1udcWFjY4b6AAnxlZSVPPvkkpmmitebss8/mxBNPZNSoUSxbtoxVq1b5hklGlLoaSE6xpkx3taQeoP73e+iX/4h+42VU3khr2nOWNVFJ5Q628lwIIcJfhgOOHEQ31Le77xapAgrww4cP56GHHmq3PT09nYULFwby0qHV3Ac/YhzQdYA3vnEZeuQ4zEcXotf+BzXrYlR6hnWUIzsYtRVC9IVBQ2HYaMwbvo26bB7G/1wa6hoFTGaytqGbGqG8FOyZGNPPxZh+XrfHqPGT4ZSvoT9agzr+RH/agUwJ8EJECqUUasppAOhPPwxxbfqGJBtra99uyBzQqxVkAIwrrkcPG20NlfQurB0tP/OEiBXKnm39+g6jXDqBkBZ8G7r0CAwc3OvjlC0D46JCqxXgyGqVplQIESEyvCP+Nq1Hf/VlaOvSByTAt1Vagsoe2H05IUTUUaOOw1jwcwBM76pPkUwCfFtVlWCXZF9CxKwTTkR962o4ejjUNQmYBPi2ql2tltUTQsQWZcShpp8HZUdDXZWASYBvQ9e4UWldLxYshIhyaTaoq7VG1UUwCfBtVbuhm9XghRDRTRkGpGdAVYQlSmxDAnwLuqLM6ndLi651GYUQxyDDHvHJxyTAt6D/XYSaMBmGDAt1VYQQoZbhQB8+gN7yaahrcsxkolNLleUwaVpkpjgWQvQtlxP926VowHjqJVRC5C3EIy34FrSzQpKDCSEstTX+x/t3h64eAZAA31JZieSPEUIAoL4+23qQOxh9cF9oK3OMJMB7mWv/C/W1kDsk1FURQoQB45yLiHvmVWtM/L5doa7OMYn5AK+1Rle74cutqPMvtYZHCSGEl5o0Df3pR53u16YZxNr0TkxHM11fBxs/wLx5DrqqEjV4aKirJIQINwMGthouqVukMNA1bszrCtA7t4SiZt2K6QBv3nMj5tMPWk8qyyFDbrAKIdpISgaPB93YiD7wFeZd1/r3HdoPgD56JESV61pMB3jKSvyPv9oFvcwBL4SIfkopa3Z7jRuqqwCraxdAHzloFaoKzwlRsR3gW9KmLLEnhOhYtQvz1qvB7V2Qu77Otx2AqorQ1KsbAU10Ki0t5cknn8TpdKKU4txzz+XCCy/E7XazbNkySktLfYtup6WF8Qop9ixwlssNViFEx7w3Un3977U11rrNdbUwdgL683Xob12NMuJCWMn2Aopo8fHxXH311Tz66KPcf//9vPnmm+zfv5+ioiImTZrE8uXLmThxIkVFRX1V3z7T/BMLQF1UiPHYX0JYGyFEODP+36MA6L8/Z21wV6ErytC7tqMmTYOERNi5NYQ17FhAAd7hcDBy5EgAkpOTycvLo7y8nPXr1zNjxgwAZs6cybp16wKuaJ+rrYGkFOKeeRXjnAslRbAQolNqxFiw2X3Pzd8vx/zVEti8AZJTUAPz0M7w66bpsz6JkpIS9uzZw7hx43A6nTgc1qpIdrsdpzMMU246K0DSEggheirO6tFW51zoHTpp3XAlKRnS0v3982GkTwJ8XV0dS5cuZe7cuaSkpLTaF7aJuyrLZNSMEKLH1JTTYdwE1OTTrB6Axnpre3KytUBIyUF0UyOep34R4pr6BZxNsqmpiaVLl3L22Wdz6qmnAlarvbKyEofDQUVFBXa7vd1xxcXFFBcX+54XFhZiswVvqbyGhloaB+SSFsRzCktiYmJQr7UIjai7ztfdCkDTru24t37m25ziyKLhs49pfP9t0i/5Lq6NH5L06YcknvX1oFVt5cqVvsf5+fnk5+cDAQZ4rTUrVqwgLy+Piy66yLd96tSprF69moKCAtasWcO0adPaHduyEs1cruD9xDEPH4JUW1DPKSw2m3zusSBar7M2/GFTXfAtaoeOglnfhPffpnrr5wDUPPkL6k86PSj1sdlsFBYWdrgvoC6a7du38+6771JcXMztt9/O7bffzqeffkpBQQGbNm1i/vz5bN68mYKCgkBO0z8qSiFTumiEEL2UlYO64kcAGN+6GpWYhBoxBuLjMZ9+wCozfnIIK+gXUAv+hBNO4G9/+1uH+xYuXBjIS/cL7a5Cf74e42uz0Pt2Y0w4KdRVEkJEGKUUauaF6Klntt7R1GT9f+x4cFcFv2IdiKmZPXrTBvRzj6E3fwJfbIahI0NdJSFEhFLpHazdrAyM7//UP8M1xGIqwNPYAIC55l+oiy9HZeWEuEJCiKgSFwfpNqh2h7omQKwF+Mpy6/87t8rCHkKIvhcXD0kpUF+H3r451LWJsQDv9AZ4dxXK7ghtXYQQ0Uf55/6Yv7yrVUqUUIipAK8rylDnX2o9Seug/0wIIY6Rmnom5I1ovbGuNjSV8Qp4olMk0If2Q0qKlTFy9hyIj4dBsnqTEKLvqGtvQ7VtsVdVQkpqaCpEjLTgzUXXYz6xBEpLIHMAxqVXoZKSQl0tIUQUUUr5Uo6refOtXFeu0C4EEhMBHrBWbMpwoDKk710I0b+Mr50LY8ajy46Gth4hPXuQKZnYJIQIEjVoKBw5ENI6xFSAl4lNQoigGToC/dWukFYh6gO8Nj2+xypD8r8LIYJDHT8RvigO6VDJqA/wHPjK/1j634UQQaIyMqGuFvPOH6CbGkNSh+gP8GUlMPFk67FNxr4LIYJIm1B+FL4o7r5sP4j6cfDa5UTZM1EPPovKltwzQojg05XlhGJtu+hvwburIN0uwV0IEXTqsnkwbgLUVofk/FHfgsflBLss7CGECD7jfy7FrKsJWXbJ6G/Bu6qk710IETqp6VAjAb5faFclytZ+0W8hhAgKCfD9yGX1wQshRCiotDR0Td/0wWvTRLucPS4fcB/8U089xcaNG8nIyGDp0qUAuN1uli1bRmlpKTk5OSxYsIC0tLRAT3Vs3E7pohFChE5qep/1wet33kT/+Wninnm1R+UDbsGfc8453HXXXa22FRUVMWnSJJYvX87EiRMpKioK9DTHRGvt7YOXFrwQIkRS03o8ikbXVKP37uy8QFVFr04dcIAfP358u9b5+vXrmTFjBgAzZ85k3bp1gZ7m2NTXWSusJCWH5vxCCNGLFrw5/7uY9/20w24YffArcPduMe9+6YN3Op04HFZaALvdjtPZ8z6jPuVySv+7ECK0eniTVTc1+R6bv3641T7z2Ucx77kRveqfVtnynqUh7vdx8M3rE7ZVXFxMcbF/+m5hYSE2m63Pzqs9HhpLD1HvyOzT1xWBS0xMlGsSA+Q6W3R6Ok6Ph/SUZFR8QqflPAf34Wufb99Ewpp/kTjzG+BpourD1a3KJn76Icmz5/ier1y50vc4Pz+f/Px8oJ8CvN1up7KyEofDQUVFBXZ7+1Z0y0o0c7l69/OjK3r9e9a34Mln9OnrisDZbDa5JjFArnMLqWm4jhzqMKOtLitBZeei97Tue697/mnqtnwKn3zQ+oAJU6jfu4tG72drs9koLCzs8LT90kUzdepUVq9eDcCaNWuYNm1af5ymS80ZOtXwMUE/txBCtJKaDtXtb7TqhnrMO3+A+dIf0JXlEJ8AmQP8BbzBXV16FeqqG6zHEyaje7iQSMAB/rHHHmPhwoUcPHiQH//4x6xatYqCggI2bdrE/Pnz2bx5MwUFBYGepvdq3agzv4668NvBP7cQQrSUmtZhP7x5gxWf9Bsvode/hzr3YuIe/h3Gr19BnXGOr5xx4bdRZ50PgDpuIhzuWYAPuIvm5ptv7nD7woULA33pwNRUQ2p6p/cAhBAiaFLTrJjUgt63u3WZLZ+Cd1lRZcTBVTegP1iFsWi5tU0pjCVPw8AhYBjorZ+hxk/u8rRRN5NVmx50VQUc3AcpqaGujhBCoFLT0W1a8OZzj/n3/+/3rAct5uyohETinnkVNWyUf9ugPJRSqFkXoTdv6Pa80Rfg1/4X85ar0R+8DXFxoa6OEEJAWuuhknrHFvC24I2HnkXNvBAANeq4Hr2cGjbaGhffjehLF9xi/UP19RD0/QshRFstJjtprTEfvhMA46dLUFnWWhXGDXfDoKE9ez1HNlR2P6s16lrw1NfBiVMxfvUiKj76vr+EEBEoMQn9f3+20qe07KoZMtz3UJ10Ws/vGabboLr7IajRF+AP7UONPg6VlBTqmgghhKWy3Pp/6RHrce4Q63n6MSZCTIvRAK/ffQsM6XsXQoQPdVEhpKZh/uYR9H9ehewc6wbqsd4nTEoGjwf95bYui0VVgNcN9QCo8y8NcU2EEMJPObIw5s6HPTvQ7/0bklICez2lIHcw+tOPuiwXVQGeajfYM6XvXQgRdtSU0+Gk06zHg/MCf73Jp6I/7zpTb3RFwuoqq29KCCHCkHHGLMyGBtQlVwT+YpnZ0M1QyagK8Pq9/0BdbairIYQQHVInn0HcyWf0zWs5stHdlAn7Lhpz7X/x/PAS9Cfvd1tWlx5plb9BCCGi1qDuu3nCOsDrTRvQf/qV9bj0SPcHeJpQY07o51oJIUQYGDys29n6YdtFo78oxnz8XgDUNy4Dtwttmiiji++k2hrJPyOEiAlKKeJWvNJlmbBtweutn/qf5AyCilLM6wpaLWvVTk01pKR1vl8IIWJI2AZ4vGPaAVRGJnr3DutJfRc3UWtrIFla8EIIAWEa4D1PP4B+qwjyRoBSYHdA8womtTUdHqM9HqhxWVnbhBBChGkfvHeZKuPuR60AX1Xp39fJMEhz+WKwZ6GSA5shJoQQ0SLsWvC6oR7iEzCeegmVkGDNSs3wJ8E3H74TbZqtj2lshK2fQaIkGBNCiGb9FuA//fRTbr75Zm666SaKiop6fqCzwko3kJDg26TiEzAeetZ6UltjpQRuqbLMKjd1eqDVFkKIqNEvAd40TZ599lnuuusuHn30UdauXcv+/ft7drCzHOyZ7TarrByI8/Yotb3RWlEGY07AuPg7AdZcCCGiR78E+J07dzJo0CByc3OJj49n+vTprF+/vmcHOysho32ABzCW/9UaMtm2H97lBJsjwFoLIUR06ZcAX15eTnZ2tu95VlYW5eXlPTpW17hRnYyEUUlJ1kSmNl00utqFSpckY0II0VJY3WTVu7Zb3S9djYRJSoa6Nn3w1W4ZHimEEG30yzDJrKwsysrKfM/LysrIyspqVaa4uJji4mLf88LCQhK2bKTps3XETzmNFFvHLXJ3uo0kBQkt9tc21qOyckju5BgRXhITE7HJtYp6cp2DZ+XKlb7H+fn55OfnA/0U4MeMGcPhw4cpKSkhKyuL999/n/nz57cq07ISzer/7y8AmCefQZOr4/UGzbgEairKMLz79VdfYr72Aup7N9LYyTEivNhsNlxyraKeXOfgsNlsFBYWdrivXwJ8XFwc11xzDffffz+maTJr1iyGDh3a8xdISu58n82O/nA1nDYDwLeiiTp+YgA1FkKI6NNvM1mnTJnClClTju3grtYrTEyCzRvQtTWolFRwVaEumYNqXqVcCCEEEGY3WZt1mW6gwXuDtbYaAH14P2rk2P6vlBBCRJiwCvDGT5dYD3IGdVpGXXS59aDGCvAcPgCDetH9I4QQMSKsAjzNqzENHtZpEWXPhLHjoaYaXV5qjYnPzglSBYUQInKEVYBXiUkYT7zQKg9Nh1LSoLYaXfwJasJJKKPrZauEECIWhV26YNWDBTtUhgN95ADs/RLGTw5CrYQQIvKEVQu+p9SJp6BffA798TuoIcNDXR0hhAhLERngW92EHSjDI4UQoiORGeAzBwBg3Ho/Kj0jxJURQojwFJkBvjmojzwutPUQQogwFnY3WXtCKUXcM6+GuhpCCBHWIrMFL4QQolsS4IUQIkpJgBdCiCglAV4IIaKUBHghhIhSEuCFECJKSYAXQogoJQFeCCGilAR4IYSIUsc8k/WDDz7gxRdf5MCBAzzwwAOMHj3at++VV15h1apVGIbBvHnzmDxZUvoKIUSwHXMLfvjw4dx6661MmDCh1fb9+/fz/vvv8+ijj3LXXXfx29/+FtM0A66oEEKI3jnmAJ+Xl8eQIe1T9a5bt47p06cTHx9Pbm4ugwYNYufOnQFVUgghRO/1eR98RUUF2dnZvufZ2dmUl5f39WmEEEJ0o8s++CVLllBZWdlu+3e/+12mTp3a45MopXpfMyGEEAHpMsAvXLiw1y+YlZVFWVmZ73lZWRlZWVntyhUXF1NcXOx7XlhY2GGXj4hONpst1FUQQSDXOThWrlzpe5yfn09+fj7QD100U6dOZe3atTQ1NVFSUsLhw4cZO3Zsu3L5+fkUFhb6/mtZwe70tGy0lJNzB/e80fTZREK5npaVz6bz/S1jaXNwB4hbvHjx4h6fqYWPP/6Y++67j4MHD/LRRx+xefNmzjrrLDIyMnC73axYsYK1a9dyzTXXMHjw4G5fr7i4uFXFupObmxtT5aLp3P1xraPls4mUc4f7de5N2XAv113Zrj5npbXWPT5LP2r+FhLRT651bJDrHBxdfc5hM5O1N9/0IrLJtY4Ncp2Do6vPOWxa8EIIIfpW2LTgY8VVV13V5f7Fixeza9euINVG9Be5zrEh3K+zBPgg625OgMwZiA5ynWNDuF/nkAT47r71ot2WLVt48MEHfc+fffZZVq9eHboK9aNYvtZynWNDOF/nkAT4UH+rhRulVNR+JtH6vo6FXOfYEE7X+ZjTBQeqrq6ORx55BLfbjcfj4Tvf+Q5Tp06lpKSEBx54gBNOOIEvvviCrKwsbrvtNhITE0NVVREgudaxQa5z+AlZH3xiYiK33norDz30EIsWLeKPf/yjb9/hw4e54IILWLp0KampqXz00Uehqma/MAyDloOXGhoaQlib/her11qus1znUAtZC15rzV/+8he2bduGUoqKigqcTidgzdoaMWIEAKNHj+bo0aOhqma/yMnJYf/+/TQ1NVFfX8/mzZsZP358qKvVb2L1Wst1luscaiEL8O+++y4ul4uHHnoIwzC44YYbaGxstCoV76+WYRhh9Y0YCI/HQ0JCAtnZ2Zxxxhnccsst5ObmMmrUqFBXrV/F2rWW6yzXOVyELMDX1NSQkZGBYRhs3ryZ0tLSUFUlaPbt28egQYMAuPLKK7nyyivblbnnnnuCXa1+F2vXWq6zXOdmob7OQe+Db/7WO+uss9i1axe33nor77zzDnl5eb4ybe9Ah8sd6UC89dZbPP7441x++eWhrkrQxOK1luss1zmcBD1VwZ49e3jmmWe4//77g3laEQJyrWODXOfwFdQumrfeeos33niDuXPnBvO0IgTkWscGuc7hTZKNCSFElJJcNEIIEaX6rYumtLSUJ598EqfTiVKKc889lwsvvBC3282yZcsoLS0lJyeHBQsWkJaWBsArr7zCqlWrMAyDefPmMXnyZAB27drFk08+SWNjI1OmTGHevHn9VW1xDPryWv/1r3/lnXfeobq6utVEGREe+upaNzQ0sHTpUkpKSjAMg1NOOYU5c+aE+N1FId1PKioq9O7du7XWWtfW1uqbbrpJ79u3T//pT3/SRUVFWmutX3nlFf38889rrbXet2+fvvXWW3VjY6M+cuSIvvHGG7Vpmlprre+88069Y8cOrbXWv/jFL/TGjRv7q9riGPTltd6xY4euqKjQV111VUjei+haX13r+vp6XVxcrLXWurGxUS9atEj+XfeDfuuicTgcjBw5EoDk5GTy8vIoLy9n/fr1zJgxA4CZM2eybt06ANatW8f06dOJj48nNzeXQYMGsWPHDioqKqirq/Mt3H322Wfz8ccf91e1xTHoq2sNMHbsWBwOR0jeh+heX13rxMREJkyYAFiToEaNGkV5eXlI3lM0C0offElJCXv27GHcuHE4nU7fP2C73e6bylxRUUF2drbvmOzsbMrLy6moqCArK8u3PSsrS/4Qwlgg11pElr661tXV1WzYsIGJEycGr/Ixot8DfF1dHUuXLmXu3LmkpKS02hfpkx1Ea4Fca/lbiCx9da09Hg/Lly/nG9/4Brm5uf1S11jWrwG+qamJpUuXcvbZZ3PqqacC1rd7ZWUlYH272+12wGqZl5WV+Y4tKysjOzu7XYu9rKysVYtehIdAr7Vc08jRl9f617/+NUOGDOHCCy8M4juIHf0W4LXWrFixgry8PC666CLf9qlTp/pWO1mzZg3Tpk3zbV+7di1NTU2UlJRw+PBhX39sSkoKO3bsQGvNu+++6/ujEuGhr661CH99ea1feOEFamtrufrqq4P+PmJFv0102rZtG/fccw/Dhw/3/SSbM2cOY8eO7XQ41csvv8yqVauIi4tj7ty5nHTSSYB/mGRDQ5ElXtEAAACHSURBVANTpkzhmmuu6Y8qi2PUl9f6+eefZ+3atVRUVJCZmcm5557LZZddFrL3Jlrrq2tdVlbG9ddfT15eni/T5AUXXMCsWbNC9t6ikcxkFUKIKCUzWYUQIkpJgBdCiCglAV4IIaKUBHghhIhSEuCFECJKSYAXQogoJQFeCCGilAR4IYSIUv8f8P777wHo2GwAAAAASUVORK5CYII=)

`DataFrame` 按照 `columns` 绘图：

In [81]:

```py
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
                  columns=['A', 'B', 'C', 'D'])

df.cumsum().plot()
p = plt.legend(loc="best")

```

![](data:image/png;base64,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)

## 十二、文件读写

### csv

写入文件：

```py
df.to_csv('foo.csv')

```

从文件中读取：

```py
pd.read_csv('foo.csv').head()

```

|      | Unnamed: 0 | A         | B        | C         | D         |
| ---- | ---------- | --------- | -------- | --------- | --------- |
| 0    | 2000-01-01 | -1.011554 | 1.200283 | -0.310949 | -1.060734 |
| 1    | 2000-01-02 | -1.030894 | 0.660518 | -0.214002 | -0.422014 |
| 2    | 2000-01-03 | -0.488692 | 1.709209 | -0.602208 | 1.115456  |
| 3    | 2000-01-04 | -0.440243 | 0.826692 | 0.321648  | -0.351698 |
| 4    | 2000-01-05 | -0.165684 | 1.297303 | 0.817233  | 0.174767  |

### hdf5

写入文件：

```py
df.to_hdf("foo.h5", "df")

```

读取文件：

```py
pd.read_hdf('foo.h5','df').head()

```

|            | A         | B        | C         | D         |
| ---------- | --------- | -------- | --------- | --------- |
| 2000-01-01 | -1.011554 | 1.200283 | -0.310949 | -1.060734 |
| 2000-01-02 | -1.030894 | 0.660518 | -0.214002 | -0.422014 |
| 2000-01-03 | -0.488692 | 1.709209 | -0.602208 | 1.115456  |
| 2000-01-04 | -0.440243 | 0.826692 | 0.321648  | -0.351698 |
| 2000-01-05 | -0.165684 | 1.297303 | 0.817233  | 0.174767  |

### excel

写入文件：

```py
df.to_excel('foo.xlsx', sheet_name='Sheet1')

```

读取文件：

```py
pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA']).head()

```

|            | A         | B        | C         | D         |
| ---------- | --------- | -------- | --------- | --------- |
| 2000-01-01 | -1.011554 | 1.200283 | -0.310949 | -1.060734 |
| 2000-01-02 | -1.030894 | 0.660518 | -0.214002 | -0.422014 |
| 2000-01-03 | -0.488692 | 1.709209 | -0.602208 | 1.115456  |
| 2000-01-04 | -0.440243 | 0.826692 | 0.321648  | -0.351698 |
| 2000-01-05 | -0.165684 | 1.297303 | 0.817233  | 0.174767  |

清理生成的临时文件：

```py
import glob
import os

for f in glob.glob("foo*"):
    os.remove(f)

```