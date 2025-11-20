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
# import pandas as pd
# import numpy as np

# 예제 데이터 생성
'''
np.random.seed(42)
n_samples = 210
X = np.random.randn(n_samples, 4)
y = (X[:, 0] + X[:, 1] * 0.5 + np.random.randn(n_samples) * 0.5 > 0).astype(int)
df = pd.DataFrame(X, columns=['weight', 'height', 'age', 'income'])
df['gender'] = y

# 데이터 확인
# print(df.head())
'''


# p.452 연습문제 1번
'''
import statsmodels.api as sm
print(df)
X = df[['weight']]
y = df['gender']
X = sm.add_constant(X)
model = sm.Logit(y, X).fit()
print(model.summary())

odds_ratios = np.exp(model.params['weight'])
print(f'weight의 오즈비: {odds_ratios}')
'''

# 정답
'''
import statsmodels.api as sm

X_weight = df[['weight']]
X_weight = sm.add_constant(X_weight)
y = df['gender']
logit_model_weight = sm.Logit(y, X_weight).fit()

print(logit_model_weight.summary()) 

odds_ratios_weight = np.exp(logit_model_weight.params['weight'])
print(f'weight의 오즈비: {odds_ratios_weight}')
'''


# p.452 연습문제 2번
'''
import statsmodels.formula.api as smf
import statsmodels.api as sm
model = smf.glm('gender ~ weight + height + age + income', data = df, family=sm.families.Binomial()).fit()
# print(dir(model))
# print(model.deviance.round(3))


X = df.drop(columns='gender')
y = df['gender']
# print(X, y)
X = sm.add_constant(X)
model = sm.Logit(y, X).fit()

residual_deviance = -2 * model.llf
print(f'Residual deviance: {residual_deviance.round(3)}')
'''

# 정답
'''
X_all = df[['weight', 'height', 'age', 'income']]
import statsmodels.api as sm
X_all = sm.add_constant(X_all)
logit_model_all = sm.Logit(y, X_all).fit()

residual_deviance = -2 * logit_model_all.llf
print(f'Residual deviance: {residual_deviance.round(3)}')
'''


# p.452 연습문제 3번
'''
from sklearn.model_selection import train_test_split
# import sklearn
# print(dir(sklearn.model_selection))

train_df, test_df = train_test_split(df, test_size=90, random_state=42)
# print(train_df.shape, test_df.shape)
train_X = train_df[['weight']]
train_y = train_df['gender']
import statsmodels.api as sm
train_X = sm.add_constant(train_X)
model = sm.Logit(train_y, train_X).fit()

test_X = test_df[['weight']]
test_y = test_df['gender']
test_X = sm.add_constant(test_X)

pred_y = model.predict(test_X) > 0.5
# print(pred_y)
# print(test_y)

from sklearn.metrics import accuracy_score
# print(dir(sklearn.metrics))

result = accuracy_score(test_y, pred_y)

error_rate = 1 - result
print(f'오분류율 {round(error_rate, 4)}')
'''

# 정답
'''
from sklearn.model_selection import train_test_split

df_train, df_test = train_test_split(df, test_size=90, random_state=42)
import statsmodels.api as sm
X_train = sm.add_constant(df_train[['weight']])
y_train = df_train['gender']
X_test = sm.add_constant(df_test[['weight']])
y_test = df_test['gender']

print(X_train.shape)
print(X_test.shape)

logit_model_train = sm.Logit(y_train, X_train).fit()

from sklearn.metrics import accuracy_score

y_pred = logit_model_train.predict(X_test) > 0.5

error_rate = 1 - accuracy_score(y_test, y_pred)
print(f'오분류율: {round(error_rate, 4)}')
'''


# --------------------------------------------------
# p.453 연습문제 4,5,6번
import pandas as pd
import numpy as np
from sklearn.datasets import load_diabetes

diabetes = load_diabetes(as_frame=True)
df = diabetes.frame
# print(df.head())


# p.453 연습문제 4번
'''
df['target'] = (df['target'] > df['target'].median()).astype(int)
# print(df['target'])
X = df.drop(columns=['target', 's1', 's2', 's3', 's4', 's5', 's6'])
y = df['target']
import statsmodels.api as sm
X = sm.add_constant(X)
# print(X, y)
model = sm.Logit(y, X).fit()
# print(model.summary())

model_pvalues = model.pvalues
rs = model_pvalues >= 0.05
# print(model_pvalues >= 0.05)
print(rs.sum())
'''

# 정답
'''
import statsmodels.api as sm
X = df.iloc[:, 0:4]
X = sm.add_constant(X)

y = (df['target'] > df['target'].median()).astype(int)

logit_model = sm.Logit(y, X).fit()
print(logit_model.summary())

p_values = logit_model.pvalues
non_significant_vars = p_values[p_values >= 0.05]
num_non_significant_vars = len(non_significant_vars)

print(f'유의하지 않은 변수의 수: {num_non_significant_vars}')
'''


# p.453 연습문제 5번
'''
# print(df)
X = df[['age', 'sex', 'bmi', 'bp']]
import statsmodels.api as sm
X = sm.add_constant(X)
y = df['target']
y = (y > y.median()).astype(int)
# print(y)
model = sm.Logit(y, X).fit()
alpha = model.pvalues[model.pvalues < 0.05]
alpha = alpha.index.drop('const', errors='ignore')
# print(X1)

X1 = df[alpha]
X1 = sm.add_constant(X1)
model1 = sm.Logit(y, X1).fit()
print(f'유의한 변수들만 사용 시 회귀계수들의 평균: {model1.params.mean()}')
'''

# 정답
'''
import statsmodels.api as sm
X = df.iloc[:, 0:4]
X = sm.add_constant(X)

y = (df['target'] > df['target'].median()).astype(int)

logit_model = sm.Logit(y, X).fit()
# print(logit_model.summary())

p_values = logit_model.pvalues
significant_vars = p_values[p_values < 0.05]
# print(significant_vars)
significant_var_names = significant_vars.index.drop('const', errors='ignore')

X_significant = X[significant_var_names]
X_significant = sm.add_constant(X_significant)

logit_model_significant = sm.Logit(y, X_significant).fit()

significant_coef_mean = logit_model_significant.params.mean()
print(f'유의한 변수들만 사용 시 회귀계수들의 평균: {significant_coef_mean}')
'''


# p.453 연습문제 6번
'''
# print(df)
X = df[['age', 'sex', 'bmi', 'bp']]
import statsmodels.api as sm
X = sm.add_constant(X)
y = df['target']
y = (y > y.median()).astype(int)
# print(X, y)
model = sm.Logit(y, X).fit()

rank = 1
age_coef = model.params['age']
odds_ratio = np.exp(age_coef * rank)
print(f'age 변수가 1단위 증가할 때 오즈비: {odds_ratio}')
'''

# 정답
'''
import statsmodels.api as sm
X = df.iloc[:, 0:4]
X = sm.add_constant(X)

y = (df['target'] > df['target'].median()).astype(int)

logit_model = sm.Logit(y, X).fit()

coef_bmi = logit_model.params['age']

delta_x = 1
odds_ratio = np.exp(coef_bmi * delta_x)
print(f'age 변수가 1단위 증가할 때 오즈비: {odds_ratio}')
'''