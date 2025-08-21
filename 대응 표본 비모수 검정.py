# 대응 표본은 2개 그룹이 있는 데이터처럼 보이지만, 특정 변수 값에 대응하는 표본끼리의 연산을 통하여 1개 표본으로 변환 가능하다.
# 따라서 짝이 존재하는 대응 표본은 윌콕슨 순위합 검정을 사용하여 처리할 수 있다.

# 문제요약: 교육 프로그램 이수 후 성적이 향상되었는지 유의수준 5% 하에서 검정한다.

import pandas as pd
import numpy as np

sample = np.array([9.76, 11.1, 10.7, 10.72, 11.8, 6.15, 10.52, 14.83, 13.03, 16.46, 10.84, 12.45])

id = [1, 2, 3, 4, 5, 6]
before_after = ['before'] * 6 + ['after'] * 6
tab3 = pd.DataFrame({'id': id * 2, 'score': sample, 'group': before_after})

# 자료 변환
test3_data = tab3.pivot(index = 'id', columns = 'group', values = 'score')
test3_data['score_diff'] = test3_data['after'] - test3_data['before']

print(test3_data['score_diff'])


from scipy.stats import rankdata

sample_sign = np.sign(test3_data['score_diff'])
print(sum(rankdata(abs(test3_data['score_diff']))[sample_sign > 0]))


# ---------------------------------------
from scipy.stats import wilcoxon
statistics, pvalue = wilcoxon(test3_data['score_diff'], alternative='greater')

print(f'statistics: {statistics}')
print(f'p-value: {pvalue}')