# 직접 n사분위수를 구해보는 코드
'''
import numpy as np

data = np.array([155, 126, 27, 82, 115, 140, 73, 92, 110, 134])
sorted_data = np.sort(data)
n = len(sorted_data)

# 75th percentile (3rd quartile)
q3_percentile = (n-1) * 0.75 + 1
j3, h3 = divmod(q3_percentile, 1)
q3 = (1 - h3) * sorted_data[int(j3) -1] + h3 * sorted_data[int(j3)]
print(q3)
'''


# 함수 사용해서 n사분위수 구하기
'''
import numpy as np
x = np.array([155, 126, 27, 82, 115, 140, 73, 92, 110, 134])

q1 = np.percentile(x, 25)
q2 = np.percentile(x, 50)
q3 = np.percentile(x, 75)
print('1사분위수: ', q1)
print('2사분위수: ', q2)
print('3사분위수: ', q3)
'''


#데이터에 대응하는 백분위 구하기
'''
import numpy as np
import scipy.stats as sp

x = np.array([155, 126, 27, 82, 115, 140, 73, 92, 110, 134])
percentiles = np.array([sp.percentileofscore(x, value, kind='rank')for value in x])
print(percentiles)
'''


#QQ-Plot
import numpy as np
import scipy.stats as sp
data_x = np.array([4.62, 4.09, 6.2, 8.24, 0.77, 5.55, 3.11, 11.97, 2.16, 3.24, 10.91, 11.36, 0.87])
percentile_rank = np.array([sp.percentileofscore(data_x, value, kind='rank')for value in data_x])
print(percentile_rank[:6])

theory_x = sp.norm.ppf(percentile_rank/100, np.mean(data_x), np.std(data_x))
print(theory_x[:6])

import matplotlib.pyplot as plt

'''
plt.scatter(theory_x, data_x, color='k')
plt.plot([0,12], [0,12], 'k')
plt.title('QQplot')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Sample Quantiles')
plt.show()
'''

#scipy에는 QQplot을 쉽게 그려주는 함수가 있음.
sp.probplot(data_x, dist="norm", plot=plt)