import pandas as pd
import statsmodels.stats.weightstats as ssw
import numpy as np
import scipy.stats as ss

iris = pd.read_csv('iris.csv')

#z检验
z_pvalue = ssw.ztest(iris['sepal_length'],value=5.8)
#sepal_length平均值
sepal_length_mean = np.mean(iris['sepal_length'])
#单样本t检验
t_pvalue = ss.ttest_1samp(iris['sepal_length'],popmean=5.8)

#根据species分类，选择两个样本
iris_1 = iris[iris.species=='Iris-setosa']
iris_2 = iris[iris.species=='Iris-virginica']
#双样本t检验
t_pvalue_ind = ss.ttest_ind(iris_1['sepal_length'],iris_2['sepal_length'])


print(sepal_length_mean)
print(z_pvalue)
print(t_pvalue)
print(t_pvalue_ind)
