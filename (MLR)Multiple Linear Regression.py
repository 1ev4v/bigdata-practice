# 잡음 ei들의 분포는 평균이 0이고 분산이 sigma^2인 정규분포를 따른다고 가정한다.
# 회귀분석은 주로 statsmodels 라이브러리를 활용한다.

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

# 1. Iris 데이터 로드
df_iris = load_iris()

# 2. pandas DataFrame으로 변환
iris = pd.DataFrame(data = df_iris.data, columns = df_iris.feature_names)
iris.columns = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width'] # 칼럼명 변경시

# 3. 타켓(클래스) 추가
iris['species'] = df_iris.target

# 4. 클래스 라벨을 실제 이름으로 변환 (0: setosa, 1: versicolor, 2: virginica)
iris['species'] = iris['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# -----------------------------------------------------------------------------
# Formula API 활용
import statsmodels.api as sm
import statsmodels.formula.api as smf

model = smf.ols('Petal_Length ~ Petal_Width + Sepal_Length', data = iris).fit()
#print(model.summary())

# family = sm.families.Gaussian()은 다중 선형회귀 모형을 의미한다.
# model = smf.glm('Petal_Length ~ Petal_Width + Sepal_Length', family = sm.families.Gaussian(), data = iris).fit()

# smf.ols는 smf.glm에 비해 선형회귀에 특화된 가설 검정 결과를 제공한다.

# model = smf.ols('Petal_Length ~ Petal_Width + Sepal_Length + C(species)', data = iris).fit()

# ----------------------------------------------------------------------------------------------
# 행렬 활용
'''
import statsmodels.api as sm

X = iris[['Petal_Width', 'Sepal_Length']]
y = iris['Petal_Length']

X = sm.add_constant(X)

# 다중회귀 분석 모델 적합 (train 데이터 사용)
model = sm.OLS(y, X).fit()

# 회귀계수 출력
print(model.summary())

model = smf.glm('Petal_Length ~ Petal_Width + Sepal_Length', family = sm.families.Gaussian(), data = iris).fit()

# 독립 변수 (Petal_Width, Sepal_Length) + 범주형 변수 species 추가
X = iris[['Petal_Width', 'Sepal_Length', 'species']]

# 범주형 변수 species를 더미 변수로 변환 (setosa를 기준으로 drop)
X = pd.get_dummies(X, columns = ['species'], drop_first=True)
X = X.astype(float)
y = iris['Petal_Length']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
'''

# -------------------------------------------------
# 회귀계수에 따른 모델식
coefficients = model.params[1:]
#print(f'회귀계수가 가장 큰 변수: {coefficients.idxmax()}')
#print(iris)

# 회귀계수에 대한 통계적 유의성 
t_values = model.tvalues
#print('t-values:\n', t_values)

p_values = model.pvalues
#print('p-values:\n', p_values)

#print(f'|tvalue|가 가장 큰 변수: {np.abs(t_values).idxmax()}')

# 신뢰구간
conf_intervals = model.conf_int()
#print('Confidence intervals: \n', conf_intervals)

conf_intervals_90 = model.conf_int(alpha=0.10) # 90% 신뢰구간
#print('90% Confidence intervals: \n', conf_intervals_90)

# ---------------------------------------------------------------
# 더미 변수 함정(Dummy Variable Trap)
'''
import pandas as pd
import statsmodels.api as sm

data= {
    'color' : ['red', 'blue', 'green', 'red', 'green', 'red', 'green', 'blue', 'green', 'red'],
    'size' : [1, 2, 3, 1, 3, 5, 9, 2, 9, 10],
    'price' : [10, 20, 30, 10, 30, 55, 29, 10, 25, 12]
}
df = pd.DataFrame(data)

# 범주형 변수 더미 코딩 (drop_first = True로 기준 범주 제거)
df_dummies = pd.get_dummies(df, columns=['color'], drop_first=True)
#print(df_dummies)

# 종속 변수와 독립 변수 설정
X = df_dummies[['size', 'color_green', 'color_red']]
y = df_dummies['price']

X = X.astype(float)
y = y.astype(float)

# 상수항 추가
X = sm.add_constant(X)

# 다중회귀모델 적합
model = sm.OLS(y, X).fit()
#print(model.summary())

import statsmodels.formula.api as smf

# 회귀 분석 공식 설정
formula = 'price ~ size + C(color)'

# 회귀 모델 적합
model = smf.ols(formula, data=df).fit()

# 모델 요약 출력
#print(model.summary())
'''

# -----------------------------------------------
# 모델 평가

# 결정계수(R-squared)
print(f'R-squared: {np.round(model.rsquared, 2)}')

# 수정 결정계수(Adj. R-squared)
print(f'Adj. R-squared: {np.round(model.rsquared_adj, 2)}')

# F-statistic
print(f'F-statistic: {np.round(model.fvalue, 4)}')
print(f'Prob (F-statistic): {np.round(model.f_pvalue, 4)}')

# AIC, BIC
print(f'AIC {np.round(model.aic, 2)}')
print(f'BIC {np.round(model.bic, 2)}')