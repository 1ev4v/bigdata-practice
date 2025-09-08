import pandas as pd
import numpy as np
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



# 예측

from sklearn.metrics import mean_squared_error
import statsmodels.formula.api as smf
model = smf.ols('Petal_Length ~ Petal_Width + Sepal_Length + C(species)', data = iris).fit()

# 새로운 데이터 생성 (행 5개)
new_data = pd.DataFrame({
    'Petal_Width': [0.2, 1.5, 1.3, 2.1, 1.8],
    'Sepal_Length': [4.9, 5.5, 6.1, 6.7, 7.2],
    'species': ['setosa', 'versicolor', 'virginica', 'versicolor', 'virginica']
})

# 예측값 계산
y_pred = model.predict(new_data)

# 실제값과 비교할 y_true 생성 (예제 값 사용)
y_true = np.array([1.4, 4.7, 5.1, 5.8, 6.3])

# MSE 계산
mse_score = mean_squared_error(y_true, y_pred)

# 결과 출력
print('예측값:\n', y_pred)
print(f'MSE: {mse_score:.4f}')