import pandas as pd
import matplotlib.pyplot as plt

hs = pd.read_csv('housing.csv')
print(hs)
print("----------------------------------------")
print(hs.info())  # 打印出csv文件的全部属性
# print(a.to_string())  # 打印出全部的csv数据
print("----------------------------------------")
print(hs["ocean_proximity"].value_counts())  # 查看csv文件中object的分类与数量关系
print(hs.describe())  # 查看csv文件中的所有数据的摘要和大致分布
print("----------------------------------------")
hs.hist(bins=50, figsize=(20, 15))
plt.show()  # 进一步更准确的查看数据信息的分布
