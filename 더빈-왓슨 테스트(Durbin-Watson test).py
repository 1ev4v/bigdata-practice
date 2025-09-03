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

# 더빈-왓슨 테스트(Durbin-Watson Test)는 독립성 가정을 체크하기 위한 대표적인 검정이다. 
# 더빈-왓슨 테스트(Durbin-Watson Test)는 회귀분석의 잔차(residual)들이 서로 독립적인가를 확인하는 방법이다.
# 특히 자기상관(autocorrelation) 문제, 즉 오차가 연속적으로 이어질 때 상관성이 있는지를 본다.

model = smf.ols('Petal_Length ~ Petal_Width + Sepal_Length', data = iris).fit()

dw_stat = model.summary().tables[2].data[0][3]
print(f'Durbin-Watson statistic: {dw_stat}')

'''
# 또는 이렇게도 가능
from statsmodels.stats.stattools import durbin_watson

dw_stat = durbin_watson(model.resid)
print(dw_stat)
'''