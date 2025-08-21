# 부호 검정은 부로만을 이용한 검정이므로 적용할 수 있는 범위는 넓지만, 그만큼 검정력이 떨어진다.

# 부호 검정을 하기 위해서는 statsmodels 패키지에서 제공하는 sign_test()를 사용하면 된다.
import numpy as np
from statsmodels.stats.descriptivestats import sign_test

sample = np.array([9.76, 11.1, 10.7, 10.72, 11.8, 6.15, 10.52, 14.83, 13.03, 16.46, 10.84, 12.45])
statistics, pvalue = sign_test(sample, mu0=10)

print(f'Test statistic: {statistics}')
print(f'p-value: {pvalue}')

# -------------------------------
from scipy.stats import binom
print((1 - binom.cdf(9, 12, 0.5)) * 2)

# 해당 검정에서는 mu0의 값을 사용해서 각각의 데이터의 부호를 정한다.
# 그래서 mu0값과 같은 데이터가 있을 경우에는 값이 0이 되서 부호를 정할 수 없음.
# 그래서 mu0과 값이 같은 데이터는 제외하고 진행한다.