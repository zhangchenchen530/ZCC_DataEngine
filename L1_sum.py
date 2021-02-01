import numpy as np
import pandas as pd
# 创建一个空的数组，用来存放偶数元素
even=[]
for i in range(2,101,2):
    even+=[i]
a=np.sum(even)
# 检查一下求和的元素是否正确
print('符合条件的数组为:'+ str(even))
print('求和数为:'+ str(a))
