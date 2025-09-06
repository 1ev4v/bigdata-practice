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



# 다중공선성이 존재하면 계수에 대한 통계 검정 결과는 신뢰할 수 없게 된다.
# 이것은 특정 독립변수 Xj의 정보가 다른 독립 변수들의 정보로 모두 설명이 가능하다는 의미이다.

# 분산팽창계수(Variance Inflation Factors)가 활용된다.

from statsmodels.stats.outliers_influence import variance_inflation_factor
X = iris[['Petal_Width', 'Sepal_Length']]

# VIF 계산
vif_data = pd.DataFrame()
vif_data['Variable'] = X.columns
vif_data['VIF'] = [variance_inflation_factor(X.values, i)for i in range(X.shape[1])]
print(vif_data)