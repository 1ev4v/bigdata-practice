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
import scipy.stats as stats

# result1 = z-value의 값을 의미함.
result1 = 0.002256 / 0.001094
# result2 = p-value의 값을 의미함. (양측검정)
result2 = 2 * (1 - stats.norm.cdf(result1))
print(result1)
print(result2)