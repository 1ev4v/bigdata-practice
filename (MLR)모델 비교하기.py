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


import statsmodels.api as sm
from statsmodels.formula.api import ols

model1 = ols('Petal_Length ~ Petal_Width', data=iris).fit()  # mod1
model2 = ols('Petal_Length ~ Petal_Width + Sepal_Length + Sepal_Width', data=iris).fit()  # mod2

# model이 들어갈때 Reduced모델이 첫번째, Full모델이 두번째로 들어간다.
table = sm.stats.anova_lm(model1, model2)  # anova
print(table)