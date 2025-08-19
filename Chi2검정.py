# 카이제곱 검정은 주어진 데이터가 기대되는 분포나 독립성, 동질성을 갖는지를 검증하는 데 사용하는 통계적 방법이다.
# 1 표본 분산 검정(One-sample chi-squared test for variance), 카이제곱 독립성 검정(Chi-squared test for independence), 카이제곱 동질성 검정(Chi-squared test for homogeneity), 카이제곱 적합도 검정(Chi-squared goodness-of-fit test) 이렇게 4개가 있음.



# 1표본 분산 검정(One-sample chi-squared test for variance): 데이터를 발생시키는 모분포의 분산이 특정값과 같은지 검정함.
'''
# 문제를 요약하면 분산이 1.3으르 넘는 경우 생산 부적격이라고 판단한다. 생산 부적격 검정을 유의수준 5%로 설정하여 검정을 수행하라.
import numpy as np
sample_data = [10.67, 9.92, 9.62, 9.53, 9.14, 9.74, 8.45, 12.65, 11.47, 8.62]
n = len(sample_data)
sample_variance = np.var(sample_data,ddof = 1)
t = (n-1) * sample_variance / 1.3
# 여기서의 t값은 카이제곱 검정통계량의 값을 의미한다.
print(t)

from scipy.stats import chi2
# 여기서는 문제에서 1.3이 넘는 경우 생산 부적격이라고 말했기 떄문에 1.3보다 작은 경우 1.3인 경우는 필요가 없다 그래서 단측검정을 실행함.
# 그래서 생존함수형태인 1 - chi2.cdf()가 된 것.
print('p-value:', 1 - chi2.cdf(t, df = n-1))
'''


# 카이제곱 독립성 검정(Chi-squared test for independence): 주어진 표에서 두 카테고리 변수 간의 상관성이 있는지 여부를 분석하는 방법.
'''
# 독립성 검정의 검정통계량이 측정하는 것은 주어진 데이터(관찰빈도)가 이론적으로 계산된 값(기대빈도)과 얼마나 차이가 나는가이다. 
# 귀무가설이 참이면 두 값의 차이가 작고, 귀무가설이 거짓이면 두 값의 차이가 커지도록 설계(제곱 사용)되어 있다.
# 검정통계량의 값이 카이제곱 분포의 오른쪽 끝부분에 위치할 수록 귀무가설을 기각시킬 수 있는 근거가 되는 것이다.
from scipy.stats import chi2

#기각역 계산
critical_value = chi2.ppf(0.95, df = 1)
# 이 방법의 경우는 0.95에 해당하는 값을 구한후 검정통계량이 그 값보다 큰지를 비교하여 크면 귀무가설을 기각하는 형태로 진행하는 방법이다.
print(critical_value)

pvalue = chi2.sf(15.55, df = 1)
# 이 방법의 경우에는 검정통계량(15.55)에 해당하는 생존함수(sf)를 구하여 문제에서 주어지는 유의수준과 비교한후 생존함수(sf)로 구해진 p-value의 값과 비교 후 값이 더 클경우에 귀무가설을 기각하는 형태로 진행하는 방법이다.
print(pvalue)


# chi2_contingency함수를 이용하면 더 편리하게 구할 수 있음.
from scipy.stats import chi2_contingency

table = np.array([[14, 4], [0, 10]])

# chi2_contingency() 함수는 array 형태를 입력값으로 받는다는 점을 주의해야함.
# chi2_contingency() 함수의 경우, "Yates' correction for continuity"를 기본적으로 적용하기 때문에 일반적인 카이제곱 검정통계량을 얻기 위해서는 correction=False로 설정해야함.
# Yates' correction for continuity(연속성 수정): 카이제곱 독립성 검정을 수행할 때 사용되는 보정 방법이다. 작은 샘플 크기로 인해 과도하게 큰 카이제곱통계량이 계산되는 것을 방지함.
# 시험에서는 연속성 수정을 적용하라는 지시가 있으면 옵션을 추가 적용하면 됨.
chi2, p, df, expected = chi2_contingency(table, correction = False)
print(f'X-squared: {chi2.round(3)} df: {df} p-value: {p.round(3)}')

# 기대빈도 또한 확인해서 조건을 충족하는지 체크해볼 수 있음. 5이상일때 통계적 판단을 신뢰할 수 있다고 판단함.
print(expected)
'''


# 카이제곱 동질성 검정(Chi-squared test for homogeneity): 두 개 이상의 모집단에서 추출된 표본들의 카테고리 분포 또는 비율이 동일한지 검정하는 방법.
'''
# 카이제곱 동질성 검정에서도 위에서 사용한 chi2_contingency() 함수를 사용하여 쉽게 계산할 수 있다.
import numpy as np
from scipy.stats import chi2_contingency

table = np.array([[50, 30, 20],
                  [45, 35, 20]])
chi2, p, df, expected = chi2_contingency(table, correction=False)

print(chi2.round(3), p.round(3))

print(expected)
'''


# 카이제곱 적합도 검정(Chi-squared goodness-of-fit test): 관찰된 데이터가 특정 이론적 분포를 따르는 지를 검정하는 방법이다.

# 카이제곱 적합도 검정의 검정통계량 값은 chisquare()함수를 사용해서 구할 수 있다.
# 앞선 독립성 검정과 동질성 검정에서 사용한 chi2_contingency() 함수와 적합성 검정에서 사용하는 chisquare() 함수의 차이는 f_exp() 옵션을 사용해서 기대빈도(해당 사건이 발생할 예상 횟수를 의미함.)를 직접 넣을 수 있다는 점이다.
from scipy.stats import chisquare
import numpy as np

observed = np.array([13, 23, 24, 20, 27, 18, 15])
expected = np.repeat(20, 7)

statistic, p_value = chisquare(observed, f_exp=expected)
print(f'Test statistic: {statistic.round(3)}')
print(f'p-value: {p_value.round(3)}')

# expected(기대빈도)의 값이 5보다 모두 크다면 해당 검정의 결과를 신뢰할 수 있다고 판단한다.
print(f'Expected: {expected}')