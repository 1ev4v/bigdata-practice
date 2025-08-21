# F검정은 F분포를 이용해서 “두 집단의 분산이 같은지” 또는 “여러 그룹 평균이 차이가 있는지”를 판단하는 통계적 방법

import numpy as np
import scipy.stats as stats

oj_lenghts = np.array([17.6, 9.7, 16.5, 12.0, 21.5, 23.3, 23.6, 26.4, 20.0, 25.2,
                       25.8, 21.2, 14.5, 27.3, 23.8])

vc_lenghts = np.array([7.6, 4.2, 10.0, 11.5, 7.3, 5.8, 14.5, 10.6, 8.2, 9.4,
                       16.5, 9.7, 8.3, 13.6, 8.2])

s1 = oj_lenghts.std(ddof=1)
s2 = vc_lenghts.std(ddof=1)

ratio_of_variances = s1**2 / s2**2

print('ratio_of_variances: ', round(ratio_of_variances, 4))

def f_test(x, y, alternative='two-sided'):
    x = np.array(x)
    y = np.array(y)
    df1 = len(x) - 1
    df2 = len(y) - 1
    f = np.var(x, ddof=1) / np.var(y, ddof=1)
    if alternative == 'greater':
        p = 1.0 - stats.f.cdf(f, df1, df2)
    elif alternative == 'less':
        p = stats.f.cdf(f, df1, df2)
    else:
        p = 2.0 * (1.0 - stats.f.cdf(f, df1, df2))
    return f, p

# F검정 수행하기
f_value, p_value = f_test(oj_lenghts, vc_lenghts)

print(f"Test statistic: {f_value}")
print(f"P-value: {p_value}")