# 앤더슨-달링 검정은 이론적인 누적분포함수와 데이터에서 뽑혀진 누적분포함수가 얼마나 비슷한지 체크하여 검정하는 방법입니다.
# 앤더슨-달링 검정은 귀무가설이 참이라면 0에 가가운 값이 나오고, 값이 클 수록 귀무가설이 거짓이라는 통계적 근거가 되도록 설계되어져있음.

# 주어진 데이터가 정규분포를 따르는지 유의수준 5% 하에서 앤더슨-달링 검정 진행.
import numpy as np
import scipy.stats as sp

sample_data = np.array([4.62, 4.09, 6.2, 8.24, 0.77, 5.55, 3.11, 11.97, 2.16, 3.24, 10.91, 11.36, 0.87])

# Anderson-Darling 검정 수행
# anderson()함수의 인자중 dist는 검정에 사용할 기준 분포를 의미한다. 'norm'은 정규분포를 의미함.
result = sp.anderson(sample_data, dist='norm')
print(f'검정통계량: {result[0]}')
print(f'임계값: {result[1]}')
print(f'유의수준: {result[2]}')

# statsmodels에서 제공하는 ECDF()함수를 사용하면 데이터에 들어있는 분포의 정보를 사용하여 누적분포함수를 구할 수 있다.
import matplotlib.pyplot as plt
from scipy.stats import norm
import statsmodels.api as sm
# import statsmodels.formula.api as smf

ecdf = sm.distributions.ECDF(sample_data)
x = np.linspace(min(sample_data), max(sample_data))
y = ecdf(x)

plt.scatter(x, y)
plt.title('Estimated CDF vs. CDF')

# add Normal CDF
k = np.arange(min(sample_data), max(sample_data), 0.1)
plt.plot(k, norm.cdf(k, loc = np.mean(sample_data), scale = np.std(sample_data, ddof=1)), color='k')
plt.show()