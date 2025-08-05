import numpy as np
before = np.array([9.76, 11.1, 10.7, 10.72, 11.8, 6.15])
after = np.array([10.52, 14.83, 13.03, 16.46, 10.84, 12.45])

# ttest_related
from scipy.stats import ttest_rel

# t_statistic, p_value = ttest_rel(after, before, alternative='greater')
# print(f"T-statistic: {t_statistic}")
# print(f"P-value: {p_value}")



#새로운 모수를 정의하고 단일 표본 t-검정으로 수행하는 방법.
from scipy.stats import ttest_1samp

sample_d = after - before
t_statistic, p_value = ttest_1samp(sample_d, 0, alternative='greater')
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")
