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

# Formula API 활용
import statsmodels.api as sm
import statsmodels.formula.api as smf

model = smf.ols('Petal_Length ~ Petal_Width + Sepal_Length', data = iris).fit()

# 잔차 계산
residuals = model.resid

# 회귀 분석에서는 정규성 가정이 존재한다. 즉, 오차(잡음)의 분포는 정규분포로 가정한다.
# 정규성 가정은 Shapiro-Wilk 검정, 앤더슨-달링(Anderson-Darling) 검정을 통해 체크할 수 있다.
from scipy.stats import anderson

# 엔더슨-달링 테스트
ad_stat, ad_critical_values, ad_significance_level = anderson(residuals, dist='norm')

# 실제 표본으로부터 계산된 검정통계량
print(f'Anderson-Darling Test Statistic: {ad_stat}')
# 각 유의수준에서의 기각 기준치
print(f'Critical Values: {ad_critical_values}')   # (15%, 10%, 5%, 2.5%, 1%)에 대한 임곗값
# 각 유의수준
print(f'Significance Levels: {ad_significance_level}')


from scipy.stats import shapiro
# 샤피로-윌크 테스트
sw_stat, sw_p_value = shapiro(residuals)

print(f'Shapiro-Wilk Test Statistic: {sw_stat}')
print(f'p-value: {sw_p_value}')