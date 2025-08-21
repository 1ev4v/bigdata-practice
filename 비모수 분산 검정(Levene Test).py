# 비모수 검정에서 등분산 가정을 체크할 때, Levene 검정을 많이 사용함.
# Levene 검정은 F-검정과 비교하면 2개 이상의 그룹에도 적용 가능함(F-검정은 2개 그룹에만 적용 가능), 이상치에 대해서 좀 더 robust(건강한)한 검정임.

# 해당 검정통계량의 특징은 원 데이터를 이용하는 것이 아니라 변형된 데이터들을 사용하여 통계량을 구하는 것이 특징이다.
# 변형된 데이터를 구하는 방법은 3가지가 있다.
# 일반적으로 데이터가 대칭분포를 이룬다면 평균에서의 편차(mean)를 사용하고, 치우친 분포의 경우 중앙값(median)에서의 편차, 꼬리가 두꺼운 경우에는 절단 평균(trimmed mean)을 사용하도록 권장한다.

import pandas as pd
import numpy as np
mydata=pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/tooth_growth.csv')

print(mydata.head())

from scipy.stats import levene
a = mydata[mydata['supp'] == 'OJ']['len']
b = mydata[mydata['supp'] == 'VC']['len']

statistics, pvalue = levene(a, b, center = 'mean')
print(f'Test statistic: {statistics}')
print(f'p-value: {pvalue}')