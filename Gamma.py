# p282 모범 답안 작성 예시 (classification)

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()

X = data.data
y = data.target

df = pd.DataFrame(X, columns=data.feature_names)
df['target'] = y

# print(df.head())

from sklearn.model_selection import train_test_split
train_X, test_X, train_y, test_y = train_test_split(df.drop(columns = 'target'),
                                                    df['target'],
                                                    test_size=0.3,
                                                    random_state=42)

