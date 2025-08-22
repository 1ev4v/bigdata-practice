# 피어슨 상관계수(Pearson Correlation Coefficient, PCC)란 두 연속형 변수 간의 선형적 관계를 측정하는 가장 일반적인 방법이다.
# 직관적이지만 이상치에 민감하며, 선형 관계만 측정가능하다.(비선형 관계는 측정 불가능)

import numpy as np
import scipy.stats as stats

x = np.array([10, 20, 30, 40, 50])
y = np.array([5, 15, 25, 35, 48])

corr_coeff, p_value = stats.pearsonr(x, y)

print(f'피어슨 상관계수 (r): {corr_coeff:.4f}')
print(f'p-value: {p_value:.4f}')