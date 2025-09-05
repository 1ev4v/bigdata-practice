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


# 회귀분석에서는 등분산 가정이 존재한다. 즉, 오차(잡음)의 분산은 일정하다고 가정한다.
# 등분산 가정은 Breusch-Pagan 검정을 통해 체크할 수 있다.

# Breusch-Pagan 검정
from statsmodels.stats.diagnostic import het_breuschpagan
bptest = het_breuschpagan(model.resid, model.model.exog)

print(f'BP-test statistics: {bptest[0]}')
print(f'p-value: {bptest[1]}')