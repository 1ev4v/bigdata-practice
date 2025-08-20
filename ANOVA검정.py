import pandas as pd
import numpy as np

scents = ['Lavender', 'Rosemary', 'Peppermint']
minutes_lavender = [10, 12, 11, 9, 8, 12, 11, 10, 10, 11]
minutes_rosemary = [14, 15, 13, 16, 14, 15, 14, 13, 14, 16]
minutes_peppermint = [18, 17, 18, 16, 17, 19, 18, 17, 18, 19]

anova_data = pd.DataFrame({
    'Scent' : np.repeat(scents, 10),
    'Minutes' : minutes_lavender + minutes_rosemary + minutes_peppermint
})
# print(anova_data.head())
# print(anova_data.groupby(['Scent']).describe())


# ANOVA(Analysis of Variance)
# scipy.stats 라이브러리의 f_oneway()함수를 사용하면 검정통계량 값과 유의확률을 계산할때 유용하다.

#문제요약: 유의수준 5% 하에서 일원 분산분석을 수행한다.
from scipy.stats import f_oneway

lavender = anova_data[anova_data['Scent'] == 'Lavender']['Minutes']
rosemary = anova_data[anova_data['Scent'] == 'Rosemary']['Minutes']
peppermint = anova_data[anova_data['Scent'] == 'Peppermint']['Minutes']

# 일원 분산분석(One-way ANOVA) 수행
f_statistic, p_value = f_oneway(lavender, rosemary, peppermint)
print(f'F-statistic: {f_statistic} p-value: {p_value}')


# 가정 체크 
# 가정 체크와 여타 분석까지 해야하는 경우에는, f_oneway() 함수를 사용하기 보다는 statsmodels 패키지를 사용하는 것이 좋다.
import statsmodels.api as sm
from statsmodels.formula.api import ols

# 모델 적합
model = ols('Minutes ~ C(Scent)', data=anova_data).fit()

# ANOVA 수행하기
anova_results = sm.stats.anova_lm(model, typ=2)
print(anova_results)


# 잔차의 정규성
import matplotlib.pyplot as plt

plt.scatter(model.fittedvalues, model.resid)
plt.show()


# QQplot과 잔차 벡터를 사용하여 유의수준 5% 하에서 Shapiro-Wilk검정 수행
import scipy.stats as sp
sp.probplot(model.resid, dist='norm', plot=plt)

W, p = sp.shapiro(model.resid)
print(f'검정통계량: {W: .3f}, 유의확률: {p: .3f}')