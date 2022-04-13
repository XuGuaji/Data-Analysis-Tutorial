[toc]

## 1、导入数据源

湖北宜化2022年(至20220412为止)，其中

![image-20220413155535110](C:\Users\XuDonghui\AppData\Roaming\Typora\typora-user-images\image-20220413155535110.png)

**输出参数**

| 名称       | 类型  | 描述              |
| :--------- | :---- | :---------------- |
| ts_code    | str   | 股票代码          |
| trade_date | str   | 交易日期          |
| open       | float | 开盘价            |
| high       | float | 最高价            |
| low        | float | 最低价            |
| close      | float | 收盘价            |
| pre_close  | float | 昨收价            |
| change     | float | 涨跌额            |
| pct_chg    | float | 涨跌幅 （未复权） |
| vol        | float | 成交量 （手）     |
| amount     | float | 成交额 （千元）   |

## 2、拖拽`Trade Date`、`Low`字段

![image-20220413160153666](C:\Users\XuDonghui\AppData\Roaming\Typora\typora-user-images\image-20220413160153666.png)

## 3、创建字段`High-Low`拖到`标记`下的`大小`

![image-20220413193835320](C:\Users\XuDonghui\AppData\Roaming\Typora\typora-user-images\image-20220413193835320.png)

## 4、拖拽`Trade Date`、`Open`字段

![image-20220413194148343](C:\Users\XuDonghui\AppData\Roaming\Typora\typora-user-images\image-20220413194148343.png)

## 5、将Change `拖到`标记`下的`大小`

![image-20220413194347254](C:\Users\XuDonghui\AppData\Roaming\Typora\typora-user-images\image-20220413194347254.png)

## 6、双轴、同步轴、缩小形状

![image-20220413194454099](C:\Users\XuDonghui\AppData\Roaming\Typora\typora-user-images\image-20220413194454099.png)

## 7、创建字段`rise/fall`看涨跌情况

![image-20220413194602415](C:\Users\XuDonghui\AppData\Roaming\Typora\typora-user-images\image-20220413194602415.png)

设置颜色

![image-20220413194627383](C:\Users\XuDonghui\AppData\Roaming\Typora\typora-user-images\image-20220413194627383.png)

## 8、加入成交量、成交额

![image-20220413194746511](C:\Users\XuDonghui\AppData\Roaming\Typora\typora-user-images\image-20220413194746511.png)