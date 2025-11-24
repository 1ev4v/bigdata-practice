# p244 모범 답안 작성 예시 (Regression)


import pandas as pd
import numpy as np
train = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/st_train.csv')
test = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/st_test.csv')
# print(train.info())
# print(test.info())

train_X = train.drop(['grade'], axis=1)
train_y = train['grade']

test_X = test.drop(['grade'], axis=1)
test_y = test['grade']

from sklearn.model_selection import train_test_split
train_X, valid_X, train_y, valid_y = train_test_split(train_X, train_y, test_size=0.3, random_state=1)
# print(train_X.shape, train_Y.shape, valid_X.shape, valid_Y.shape)

cat_columns = train_X.select_dtypes('object').columns.tolist()
num_columns = train_X.select_dtypes('number').columns.tolist()
# print(cat_columns, num_columns)

from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer

# help(OneHotEncoder)
onehotencoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
# help(SimpleImputer)
imputer = SimpleImputer(strategy='mean')

train_X_numeric_imputed = imputer.fit_transform(train_X[num_columns])
valid_X_numeric_imputed = imputer.transform(valid_X[num_columns])
test_X_numeric_imputed = imputer.transform(test_X[num_columns])

train_X_categorical_encoded = onehotencoder.fit_transform(train_X[cat_columns])
valid_X_categorical_encoded = onehotencoder.transform(valid_X[cat_columns])
test_X_categorical_encoded = onehotencoder.transform(test_X[cat_columns])

train_X_preprocessed = np.concatenate([train_X_numeric_imputed, train_X_categorical_encoded], axis=1)
valid_X_preprocessed = np.concatenate([valid_X_numeric_imputed, valid_X_categorical_encoded], axis=1)
test_X_preprocessed = np.concatenate([test_X_numeric_imputed, test_X_categorical_encoded], axis=1)
#print(train_X_preprocessed.shape, valid_X_preprocessed.shape, test_X_preprocessed.shape)

from sklearn.ensemble import RandomForestRegressor
#help(RandomForestRegressor)
rf = RandomForestRegressor(random_state=1)
rf.fit(train_X_preprocessed, train_y)
# RandomForestRegressor(random_state=1)

from sklearn.metrics import mean_squared_error, root_mean_squared_error
pred_val = rf.predict(valid_X_preprocessed)
val_mse = mean_squared_error(valid_y, pred_val)
val_rmse = np.sqrt(val_mse)
alpha = root_mean_squared_error(valid_y, pred_val)
print('valid RMSE', val_rmse)
print('확인용 RMSE', alpha)


# test_pred = rf.predict(test_X_preprocessed)
# test_pred = pd.DataFrame(test_pred, columns=['grade'])
# test_pred.to_csv('result.csv', index=False)



# GridSearch & K-fold cross validation
train_X_full = np.concatenate([train_X_preprocessed, valid_X_preprocessed], axis=0)
train_y_full = np.concatenate([train_y, valid_y], axis=0)


from sklearn.model_selection import GridSearchCV

# import sklearn
# help(sklearn.ensemble.RandomForestRegressor)

param_grid = {
    'max_depth': [10, 20, 30],
    'min_samples_split': [2, 5, 10]
}

# from sklearn.metrics import get_scorer_names
# print(get_scorer_names())

rf = RandomForestRegressor(random_state=1)
rf_search = GridSearchCV(
    estimator = rf,
    param_grid = param_grid,
    cv = 3,
    scoring = 'neg_root_mean_squared_error'
)

rf_search.fit(train_X_full, train_y_full)

# best_params_도 있음.
print('교차검증 RMSE-score', -rf_search.best_score_)

# test_pred2 = rf_search.predict(test_X_preprocessed)
# test_pred2 = pd.DataFrame(test_pred2, columns=['grade'])
# test_pred2.to_csv('result.csv', index=False)