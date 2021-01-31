import numpy as np
import pandas as pd
#原表数据
ind=['张飞','关羽','刘备','典韦','许褚']
col=['语文','数学','英语']
df=pd.DataFrame([[68,65,30],[95,76,98],[98,86,88],[90,88,77],[80,90,90]],index=ind, columns=col)

#按格式输出所要求的一系列数据
def show(subject, score):
    print('{}|{}|{}|{}|{}|{}'.format(subject, '%-8.2f'%np.mean(score), '%-8.2f'%np.amin(score), '%-8.2f'%np.amax(score), 
                                     '%-6.2f'%np.var(score), '%-8.2f'%np.std(score)))
print("科目|平均成绩|最小成绩|最大成绩| 方差 |标准差")
show('语文', df['语文'])
show('数学', df['数学'])
show('英语', df['英语'])

#复制表计算排名
df2=df.copy()
#计算总分加入表中
df2['总分'] = df.apply(lambda x: x.sum(),axis=1)
#计算排名加入表中
df2["排名"] = df2['总分'].rank(ascending=False,method='min')
#排序
df2=df2.sort_values(by='排名')
print('--------------------')
print('-----总成绩排名-----')
print(df2)
