import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from efficient_apriori import apriori
import pyfpgrowth


def main():
    # header=None，不将第一行作为head
    dataset = pd.read_csv('./Market_Basket_Optimisation.csv', header=None)
    # print(dataset.shape)
    apri(dataset)
    fpgrowth(dataset)


# 使用apriori方法
def apri(dataset):
    # 将数据存放到transactions中
    transactions = []
    for i in range(0, dataset.shape[0]):
        temp = []
        for j in range(0, 20):
            if str(dataset.values[i, j]) != 'nan':
                temp.append(str(dataset.values[i, j]))
        transactions.append(temp)
    # print(transactions)
    # 挖掘频繁项集和频繁规则，频率为0.02以上
    itemsets, rules = apriori(transactions, min_support=0.02, min_confidence=0.4)
    print("频繁项集：", itemsets)
    print("关联规则：", rules)


# 使用fpgrowth方法
def fpgrowth(dataset):
    # 将数据存放到transactions中
    transactions = []
    for i in range(0, dataset.shape[0]):
        temp = []
        for j in range(0, 20):
            if str(dataset.values[i, j]) != 'nan':
                temp.append(str(dataset.values[i, j]))
        transactions.append(temp)
        # print(transactions)
    # 挖掘频繁项集和频繁规则，频数为100以上
    itemsets = pyfpgrowth.find_frequent_patterns(transactions, 100)
    rules = pyfpgrowth.generate_association_rules(itemsets, 0.4)
    print("频繁项集：", itemsets)
    print("关联规则：", rules)


if __name__ == '__main__':
    main()