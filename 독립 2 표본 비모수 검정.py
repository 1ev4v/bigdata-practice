# 맨-휘트니-윌콕슨 검정(Mann-Whitney-Wilcoxon test)은 독립 2 표본 t-검정에 대응하는 비모수 검정이다.
# 모평균이 아닌 모중앙값에 대한 검정이다.

import pandas as pd
sample = [9.76, 11.1, 10.7, 10.72, 11.8, 6.15, 10.52, 14.83, 13.03, 16.46, 10.84, 12.45]
gender = ['female'] * 7 + ['male'] * 5
data_mww = pd.DataFrame({'id' : range(1,13), 'score' : sample, 'gender' : gender})
# print(data_mww)

from scipy.stats import rankdata
# 표본 크기 계산
n1 = len(data_mww[data_mww['gender'] == 'female'])
n2 = len(data_mww) - n1

# 순위합 계산하기
r_i = rankdata(data_mww['score'])
r_1p = sum(r_i[:7])
r_2p = sum(r_i[7:])
print(r_i)
print(r_1p, r_2p)

# 검정통계량 계산
u1 = n1 * n2 + sum(range(1, n1 + 1)) - r_1p
u2 = n1 * n2 + sum(range(1, n2 + 1)) - r_2p
U = min(u1, u2)

print(U)


# 맨-휘트니-윌콕슨 검정은 scipy.stats 모듈의 mannwhiteneyu() 함수를 사용해서 구현한다.
# 문제요약: 두 집단의 모중앙값이 같은지 유의수준 0.05하에서 검정한다.
from scipy.stats import mannwhitneyu

female = data_mww[data_mww['gender'] == 'female']['score']
male = data_mww[data_mww['gender'] == 'male']['score']

stat, pvalue = mannwhitneyu(female, male, method="exact")

print(f'stat: {stat.round(3)}')
print(f'p-value: {pvalue.round(3)}')


# 부루너 문젤(Brunner Munzel) 검정
# 맨-휘트니-윌콕슨(Mann-Whitney-Wilcoxon)의 등분산 가정을 표본이 만족하지 않는 경우 일반화 맨-휘트니-윌콕슨 검정이라 불리는 부루너 문젤(Brunner Munzel) 검정을 적용한다.
# scipy 패키지의 brunnermunzel()을 사용한다.

from scipy.stats.mstats import brunnermunzel

female2 = data_mww[data_mww['gender'] == 'female']['score']
male2 = data_mww[data_mww['gender'] == 'male']['score']

stat, pvalue = brunnermunzel(female2, male2, alternative='two-sided')

print(f'stat: {stat.round(3)}')
print(f'p-value: {pvalue.round(4)}')