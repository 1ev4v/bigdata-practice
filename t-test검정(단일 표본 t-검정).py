'''
**단일 표본 t-검정(one-sample t-test)**은 ‘모집단의 평균이 어떤 특정한 값(기준값)과 유의하게 다른가?’를 검정하는 통계적 가설검정 방법입니다.
즉, 표본 평균이 주어진 기준값과 차이가 통계적으로 유의미한지를 확인하는 절차입니다.

예시:
“우리 반 학생들의 평균 키가 전국 평균 170cm와 차이가 있는가?”
'''

sample = [9.76, 11.1, 10.7, 10.72, 11.8, 6.15, 10.52, 14.83, 13.03, 16.46, 10.84, 12.45]

from scipy.stats import ttest_1samp


# popmean은 비교할 평균값을 의미한다.
# 학생들의 성적 평균이 10점인지 아닌지를 알기 위해서 비교하는 값(10)이 된다.
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