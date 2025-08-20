import pandas as pd
import numpy as np

scents = ['Lavender', 'Rosemary', 'Peppermint']
minutes_lavender = [10, 12, 11, 9, 8, 12, 11, 10, 10, 11]
minutes_rosemary = [14, 15, 13, 16, 14, 15, 14, 13, 14, 16]
minutes_peppermint = [18, 17, 18, 16, 17, 19, 18, 17, 18, 19]

anova_data = pd.DataFrame({
    'Scent' : np.repeat(scents, 10),
    'Minutes' : minutes_lavender + minutes_rosemary + minutes_peppermint
})


# 분산분석은 3개 이상의 집단 간 평균 차이가 통계적으로 유의미한 지를 검정하는데 사용된다.
# 분산분석 자체는 어느 그룹 간에 차이가 있는지는 알려주지 않는다.
# 사후 검정은 세부적으로 어느 그룹 간 평균 차이가 통계적으로 유의미한 지 추가 검정을 할 때 사용된다.

# statsmodels 패키지의 pairwise_tukeyhsd() 함수로 Tukey's HSD 사후 검정을 수행할 수 있다.
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Tukey HSD 사후 검정
# endog: 종속변수로, 분석하고자 하는 측정값이나 점수를 의미한다.
# groups: 각 샘플에 대한 그룹 라벨을 지정한다.
# alpha: 검정의 유의수준을 설정하며, 일반적으로 0.05로 설정된다.
tukey = pairwise_tukeyhsd(endog=anova_data['Minutes'],
                          groups=anova_data['Scent'],
                          alpha=0.05)
#print(help(pairwise_tukeyhsd))
print(tukey)

# 결과해석
'''
meandiff는 평균차이를 의미함. 예시를 하나 들면 Lavender는 peppermint의 평균차이는 7.3이다.
p-adj는 p_value를 의미함.
reject는 귀무가설을 기각할지의 여부를 나타냄. true일경우 귀무가설이 기각된다는 의미이다.
'''
# p-adj: 여러 번 비교를 한다는 사실을 고려해, **Familywise Error Rate (FWER)**가 α(예: 0.05)를 넘지 않도록 보정한 값

# p-adj가 의미하는 것은 조정된 유의수준의 스케일을 원해 설정한 FWER에 맞춰서 판단할 수 있도록 다시 조정한 값을 말한다. 따라서 p-adj 값이 0.04가 나왔더라도 이 값이 FWER보다 작으면 귀무가설을 기각한다.