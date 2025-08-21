# 1 표본 t-검정에 대응하는 비모수 검정은 윌콕슨 순위합 검정(Wilcoxon signed rank test)이다.
# 모평균이 아닌 모중앙값에 대한 검정이다.

# “내 표본 중앙값이 μ₀와 달라 보이는데, 이게 진짜 차이일까, 아니면 그냥 운일까?”
# 그걸 판단하는 도구가 바로 윌콕슨 순위합 검정(Wilcoxon signed rank test)이에요.

import numpy as np
from scipy.stats import rankdata
sample = np.array([9.76, 11.1, 10.7, 10.72, 11.8, 6.15, 10.52, 14.83, 13.03, 16.46, 10.84, 12.45])

sample_diff = abs(np.array(sample) - 10)
r_i = rankdata(sample_diff)
psi_i = np.where(sample - 10 >= 0, 1, 0)

print(sum(r_i[psi_i > 0]))


# 모중앙값이 10인지 아닌지 유의수준 0.05 하에서 윌콕슨 순위합 검정을 수행.
from scipy.stats import wilcoxon
eta_0 = 10
statistics, pvalue = wilcoxon(sample-eta_0, alternative="two-sided")

print(f'Test statistic: {statistics}')
print(f'p-value: {pvalue}')

# 위의 wilcoxon() 함수의 검정통계량 값과 앞에서 직접 구현한 검정통계량 값이 다른 것을 볼 수 있다.
# 그 이유는 wilcoxon() 함수는 양수 쪽 순위합과 음수 쪽 순위합 중 작은 것을 반환하기 때문이다.
a = np.arange(start=1, stop=13)
print(sum(a)-statistics)