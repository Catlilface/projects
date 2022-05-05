from sklearn.datasets import fetch_california_housing
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import plot_tree
from sklearn.metrics import mean_squared_error

data = fetch_california_housing()

features = data.feature_names
X = data.data
Y = data.target

df = pd.DataFrame(X, columns=features)
df['target'] = Y

X_train, X_test, Y_train, Y_test = train_test_split(
	df[features],
	df['target'],
	test_size = .2,
	shuffle = True,
	random_state = 3
)

tree = DecisionTreeRegressor(random_state = 1, min_samples_leaf = 24, max_depth = 14, max_leaf_nodes = 400)
tree.fit(X_train, Y_train)

pred_train = tree.predict(X_train)
pred_test = tree.predict(X_test)

mse_train = mean_squared_error(Y_train, pred_train)
mse_test = mean_squared_error(Y_test, pred_test)

print(f'MSE на обучении {mse_train:.4f}')
print(f'MSE на тесте {mse_test:.4f}')