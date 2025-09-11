# p.432 연습문제 1,2,3번
# import pandas as pd
# import numpy as np

# 예제 데이터 생성
'''
np.random.seed(42)
n_samples = 100
X = np.random.randn(n_samples, 5)
y = 3 * X[:, 0] + 2 * X[:, 1] + X[:, 2] + np.random.randn(n_samples)
df = pd.DataFrame(X, columns=['var1', 'var2', 'var3', 'var4', 'var5'])
df['target'] = y
'''

# 데이터 확인
# print(df.head())


# p.432 연습문제 1번
'''
# print(df)
corr_df = df.corr()
# print(corr_df)
corr_target = corr_df['target'].drop('target')
# print(corr_target)
corr_df = corr_df.drop('target', axis=1)
# print(corr_df)
corr_best_X = corr_target.abs().idxmax()
corr_best_score = corr_target.abs().max()

print(f'가장 큰 상관관계를 갖는 변수: {corr_best_X}, 상관계수: {corr_best_score}')
'''

# 정답
'''
correlation_matrix = df.corr()
# print(correlation_matrix)
target_corr = correlation_matrix['target'].drop('target')
# print(target_corr)
max_corr_var = target_corr.abs().idxmax()
# print(max_corr_var)
max_corr_value = target_corr.abs().max()
print(f'가장 큰 상관게수를 갖는 변수: {max_corr_var}, 상관계수: {max_corr_value}')
'''


# p.432 연습문제 2번
'''
import statsmodels.api as sm
X = df.drop(columns='target')
y = df['target']
# print(X, y)
X = sm.add_constant(X)
# print(help(sm.OLS))
model = sm.OLS(y, X).fit()
r_squared = model.rsquared
print(f'모델의 결정계수: {r_squared}')
'''

# 정답
'''
import statsmodels.api as sm
X = df.drop(columns='target')
y = df['target']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

r_squared = model.rsquared
print(f'결정계수: {r_squared}')
'''


# p.433 연습문제 3번
'''
import statsmodels.api as sm
X = df.drop(columns='target')
y = df['target']
# print(X, y)
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

p_values = model.pvalues.drop('const')
max_p_values_X = p_values.idxmax()
max_p_values_score = p_values.max()

print(f'가장 큰 p-value를 갖는 변수: {max_p_values_X}, p-value: {max_p_values_score}')
'''

# 정답
'''
import statsmodels.api as sm
X = df.drop(columns='target')
y = df['target']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

p_values = model.pvalues.drop('const')
max_p_value_var = p_values.idxmax()
max_p_value = p_values.max()
print(f'가장 큰 p-value를 갖는 변수: {max_p_value_var}, p-value: {max_p_value}')
'''


# --------------------------------------------------
# p.433 연습문제 4,5,6번
# import pandas as pd
# import numpy as np
# from sklearn.datasets import make_regression
# import statsmodels.api as sm

# 예제 데이터 생성
'''
X, y = make_regression(n_samples = 100, n_features = 3, noise = 0.1, random_state = 42)
df = pd.DataFrame(X, columns = [f'var{i}' for i in range(3)])
df['target'] = y

# 데이터 확인
# print(df.head())
'''


# p.433 연습문제 4번
'''
# print(df)
X = df.drop(columns='target')
y = df['target']
# print(X, y)
# print(dir(sm))
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

smallest_pvalue_X = model.pvalues.drop('const').idxmin()
# print(model.summary())

smallest_pvalue_score = model.params[smallest_pvalue_X]

print(f'p-value가 가장 작은 변수의 회귀계수: {smallest_pvalue_score}')
'''

# 정답
'''
X = df.drop(columns='target')
y = df['target']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

print(model.summary())

p_values = model.pvalues
smallest_p_var = p_values.idxmin()
smallest_p_coef = model.params[smallest_p_var]
print(f'p값이 제일 작은 변수의 회귀계수: {smallest_p_coef}')
'''


# p.433 연습문제 5번
'''
X = df.drop(columns='target')
y = df['target']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

r_squared = model.rsquared
print(f'결정계수: {r_squared}')
'''

# 정답
'''
X = df.drop(columns='target')
y = df['target']
X.add_constant(X)
model = sm.OLS(y, X).fit()

r_squared = model.rsquared
print(f'결정계수: {r_squared}')
'''


# p.433 연습문제 6번
'''
X = df.drop(columns='target')
y = df['target']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

# print(X.info())

test_X = pd.DataFrame([[1.0, 0.5, 1.2, 0.3]], columns=['const', 'var0', 'var1', 'var2'])
# print(test_X)
pred_y = model.predict(test_X)
print(f'새로운 데이터에 대한 예측값: {pred_y[0]}')
'''

# 정답
'''
X = df.drop(columns='target')
y = df['target']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

new_data = pd.DataFrame({'const': [1.0], 'var0': [0.5], 'var1': [1.2], 'var2': [0.3]})
predicted_value = model.predict(new_data)
print(f'예측된 값: {predicted_value[0]}')
'''


# --------------------------------------------------
# p.452 연습문제 1,2,3번
import pandas as pd
import numpy as np

# 예제 데이터 생성
np.random.seed(42)
n_samples = 210
X = np.random.randn(n_samples, 4)
y = (X[:, 0] + X[:, 1] * 0.5 + np.random.randn(n_samples) * 0.5 > 0).astype(int)
df = pd.DataFrame(X, columns=['weight', 'height', 'age', 'income'])
df['gender'] = y

# 데이터 확인
print(df.head())


# p.452 연습문제 1번


# 정답
