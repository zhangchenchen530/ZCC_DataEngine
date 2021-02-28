from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, ward
from sklearn.cluster import KMeans, AgglomerativeClustering
from pylab import *
# 图表中文正常显示
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']

data = pd.read_csv('car_data.csv',encoding='gbk')
train_x=data[['人均GDP','城镇人口比重','交通工具消费价格指数','百户拥有汽车量']]
# 规范化到 [0,1] 空间
min_max_scaler=preprocessing.MinMaxScaler()
train_x=min_max_scaler.fit_transform(train_x)
pd.DataFrame(train_x).to_csv('temp.csv', index=False)

# K-Means 手肘法：统计不同K取值的误差平方和
sse = []
for k in range(1, 11):
# kmeans算法
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(train_x)
# 计算inertia簇内误差平方和
    sse.append(kmeans.inertia_)
x = range(1, 11)
plt.xlabel('K')
plt.ylabel('SSE')
plt.plot(x, sse, 'o-')
plt.show()

### 使用KMeans聚类
def kmeans(train_x,data):
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(train_x)
    predict_y = kmeans.predict(train_x)
# 合并聚类结果，插入到原数据中
    result = pd.concat((data,pd.DataFrame(predict_y)),axis=1)
    result.rename({0:u'聚类结果'},axis=1,inplace=True)
# 合并聚类结果排序
    result.sort_values('聚类结果',inplace=True)
    print('-'*20+'KMeans聚类结果'+'-'*20)
    print(result)


### 使用层次聚类
def hierarchy(train_x,data):
    model = AgglomerativeClustering(linkage='ward',n_clusters=3)
    y = model.fit_predict(train_x)
    result_2=pd.concat((data,pd.DataFrame(y)),axis=1)#将聚类结果加入原始表
    result_2.rename({0:u'层次聚类结果'},axis=1,inplace=True)
    linkage_matrix = ward(train_x)
    dendrogram(linkage_matrix,labels=list(result_2["地区"]))
# 合并聚类结果排序
    result_2.sort_values('层次聚类结果',inplace=True)
    print('-'*20,'层级聚类结果','-'*20)
    print(result_2)

# 调用KMeans聚类方法
kmeans(train_x,data)
# 调用层次聚类方法
hierarchy(train_x,data)