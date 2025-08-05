sample = [9.76, 11.1, 10.7, 10.72, 11.8, 6.15, 10.52, 14.83, 13.03, 16.46, 10.84, 12.45]

from scipy.stats import ttest_1samp


t_statistic, p_value = ttest_1samp(sample, popmean = 10, alternative='two-sided')
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")


import numpy as np

n = len(sample)
mean = np.mean(sample)
std = np.std(sample, ddof=1)
mu0 = 10

t_statistic = (mean - mu0) / (std / np.sqrt(n))
print(f"T-statistic (직접계산): {t_statistic}")


from scipy.stats import t

# p_value_Alpha = 2 * t.cdf(t_statistic, n-1)
# cdf는 누적분포함수이기 때문에 t값이 -일때는 그냥 사용가능하지만 +이게 되면 해당 t값보다 더 큰 값들을 구해야하기때문에 1에서 뺀값을 사용한 것.
p_value_Alpha = 2 * (1 - t.cdf(t_statistic, n-1))

print(p_value_Alpha)