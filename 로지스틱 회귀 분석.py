import pandas as pd

admission_data = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/admission.csv')
import statsmodels.formula.api as smf
import statsmodels.api as sm

admission_data['rank'] = admission_data['rank'].astype('category')
admission_data['gender'] = admission_data['gender'].astype('category')

# Formula api 활용
# print(admission_data.head())
# model = smf.logit('admit ~ gre + gpa + rank + gender', data=admission_data).fit()
model = smf.glm('admit ~ gre + gpa + rank + gender', data=admission_data, family=sm.families.Binomial()).fit()
print(model.summary())


# --------------------------------------------------
# 행렬 활용

'''
# 범주형 변수를 더미 변수로 변환
admission_data = pd.get_dummies(admission_data, columns = ['rank', 'gender'], drop_first=True)

# bool 타입을 int로 변환
admission_data[['rank_2', 'rank_3', 'rank_4', 'gender_M']] = admission_data[['rank_2', 'rank_3', 'rank_4', 'gender_M']].astype(int)

# 독립변수와 종속변수 설정
X = admission_data[['gre', 'gpa', 'rank_2', 'rank_3', 'rank_4', 'gender_M']]
y = admission_data['admit']

# 상수항 추가
X = sm.add_constant(X)

# Logit 모델 적합 (로지스틱 회귀)
# model = sm.Logit(y, X).fit()
model = sm.GLM(y, X, family=sm.families.Binomial()).fit()
print(model.summary())
'''

# --------------------------------------------------
# gre계수 검정하기
import numpy as np
import scipy.stats as stats

# result1 = z-value의 값을 의미함.
result1 = 0.002256 / 0.001094
# result2 = p-value의 값을 의미함. (양측검정)
result2 = 2 * (1 - stats.norm.cdf(result1))
# print(result1)
# print(result2)

# 각 Odds ratio에 대한 신뢰구간 구하기
# print(model.params)
odds_ratios = pd.DataFrame({
    'OR': model.params,
    # CI = 신뢰구간
    'Lower CI': model.conf_int()[0],
    'Upper CI': model.conf_int()[1],
})
odds_ratios = np.exp(odds_ratios)

# print(odds_ratios)

# 신뢰구간 직접 계산

# 표준오차 확인
# model.bse

a = round(model.params[5] - stats.norm.ppf(0.975) * 0.001094, 3)
b = round(model.params[5] + stats.norm.ppf(0.975) * 0.001094, 3)

glue_str = f"({a}, {b})"
# print(glue_str)

# 오즈비에 대한 신뢰구간 직접 구하기
a = round(np.exp(a), 3)
b = round(np.exp(b), 3)
glue_str = f"({a}, {b})"
# print(glue_str)


# --------------------------------------------------
# 로지스틱 회귀모델의 유의성 체크
# model.summary()에서도 나옴 
# LL-Null이 귀무가설 하에서의 로그 우도함수 값
# Log-Likelihood가 대립가설 하에서의 로그 우도함수 값 

# Log-Likelihood와 같은값
# print(model.llf)

# LL-Null과 같은값
# print(model.llnull)

# 검정통계량
test_statistic = np.round(-2 * (model.llnull - model.llf), 3)
# print(f'Test Statistic: {test_statistic}')

from scipy.stats import chi2
# 자유도 계산 (두 모델의 자유도 차이)
df = model.df_model - 0

# p-value 계산
p_value = chi2.sf(test_statistic, df)
# print(f'p-value: {np.round(p_value, 10)}')

# --------------------------------------------------
# deviance 구하는법 (모델의 적합도 평가)
test_statistic2 = np.round(model.null_deviance - model.deviance, 3)
print(f'Test Statistic2(Deviance): {test_statistic2}')

# Null Deviance와 Residual Deviance는 로그 우도함수 값을 통해서 계산할 수도 있음.
# llf = 귀무가설 하에서의 로그 우도함수 값
llf = model.llf
# llnull = 대립가설 하에서의 로그 우도함수 값
llnull = model.llnull
# model.deviance = Residual Deviance
deviance = np.round(model.deviance, 3)
# model.null_deviance = Null Deviance
null_deviance = np.round(model.null_deviance, 3)

deviance_calculated = np.round(-2 * llf, 3)
null_deviance_calculated = np.round(-2 * llnull, 3)

result = {
    'deviance == -2 * llf': deviance == deviance_calculated,
    'null_deviance == -2 * llnull': null_deviance == null_deviance_calculated
}

print(result)


# ---------------------------------------------------
# 예측
from sklearn.metrics import roc_auc_score
new_data = pd.DataFrame({
    'gre': [400, 700, 750, 500],
    'gpa': [3.5, 3.8, 3.9, 3.2],
    'rank': [2, 1, 4, 3],
    'gender': ['M', 'F', 'F', 'M']
})
y_true = pd.Series([0, 1, 0, 0])

new_data['admit_prob'] = model.predict(new_data)
auc_score = roc_auc_score(y_true, new_data['admit_prob'])

print(new_data[['gre', 'gpa', 'rank', 'gender', 'admit_prob']])
print(f'AUC score: {auc_score}')