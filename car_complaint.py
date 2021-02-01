# 对汽车投诉信息进行分析
# 1、求品牌投诉总数 ------------------df2
# 2、求车型投诉总数 ------------------df3
# 3、求各品牌平均投诉最多排名 --------df4

import pandas as pd
import numpy as np
result = pd.read_csv('car_complain.csv')
# 以','逗号为依据，拆分problem，分解为多个字段
result = result.drop('problem', axis=1).join(result.problem.str.get_dummies(','))

#tags为之前拆分出来的problem的多字段，作为标签
tags = result.columns[7:]
#print(tags)
#数据清洗，别名合并，将原来brand为 '一汽-大众' 的全部更替为 '一汽大众'
def subs(x):
    x=x.replace('一汽-大众','一汽大众')
    return x
result['brand']=result['brand'].apply(subs)
# 通过brand进行聚类，求总数
df= result.groupby(['brand'])['id'].agg(['count'])
# 通过brand的故障标签求总数
df2= result.groupby(['brand'])[tags].agg(['sum'])
# df和df2进行表合并
df2 = df.merge(df2, left_index=True, right_index=True, how='left')
# 通过reset_index将DataFrameGroupBy => DataFrame
df2.reset_index(inplace=True)
# 由count进行从大到小排序
df2.sort_values('count', ascending=False,inplace=True)
# 输出前十行
print('------------------------')
print('品牌投诉总数排名前十:')
print(df2.head(10))

df3= result.groupby(['car_model'])['id'].agg(['count'])
# 通过reset_index将DataFrameGroupBy => DataFrame
df3.reset_index(inplace=True)
# 由count进行从大到小排序
df3.sort_values('count',ascending=False,inplace=True)
# 修改列名称
df3.columns=['车型','数量']
# 输出前十行
print('车型投诉总数排名前十:')
print(df3.head(10))

# 通过brand，car_model进行聚类，求总数
df4 = result.groupby(['brand','car_model'])['id'].agg(['count'])
# 聚类后根据求和结果，按brand分类求平均数
df4 = df4.groupby(['brand'])['count'].agg(['mean'])
#通过reset_index将DataFrameGroupBy => DataFrame
df4.reset_index(inplace=True)
df4.columns=['品牌','品牌平均故障数']
df4.sort_values('品牌平均故障数',ascending=False,inplace=True)
# 输出前十行
print('------------------------')
print('品牌平均投诉总数排名前十:')
print(df4.head(10))
