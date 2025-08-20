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

import statsmodels.api as sm
from statsmodels.formula.api import ols

model = ols('Minutes ~ C(Scent)', data=anova_data).fit()

# Bartlett 검정통계량은 여러 그룹 간의 분산이 같은 지 검정하는데 사용된다. 
# Bartlett 검정은 scipy.stats에서 제공하는 bartlett() 함수를 사용한다.
from scipy.stats import bartlett

groups = ['Lavender', 'Rosemary', 'Peppermint']
grouped_residuals = [model.resid[anova_data['Scent'] == group] for group in groups]

# 여기서 bartlett() 함수의 매개변수에서 *는 리스트 언패킹을 의미한다. 리스트 안에 들어있는 요소들 하나하나를 언패킹하는것임.
test_statistic, p_value = bartlett(*grouped_residuals)
print(f'검정통계량: {test_statistic}, p-value: {p_value}')