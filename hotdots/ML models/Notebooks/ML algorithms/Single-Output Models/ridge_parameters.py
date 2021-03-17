"""This module identifies ridge regressor parameters that give highest r2 value"""

import numpy as np
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score

def ridge_estimator(x_train, x_test, y_train, y_test, alpha):
    """performs ridge regression and returns r2 value"""
    ridge = Ridge(alpha=alpha)
    ridge.fit(x_train,y_train)
    y_predict = ridge.predict(x_test)
    return r2_score(y_test, y_predict)

def highest_r2_calculator(x_train, x_test, y_train, y_test, low, high, step):
    """iterates over alpha values to find the one that give highest r2"""
    r2_dict = {}

    for alpha in np.arange (low, high, step):
        r2_value = ridge_estimator(x_train, x_test, y_train, y_test, alpha)
        r2_dict[alpha] = r2_value

    print("best alpha = ", max(r2_dict, key=r2_dict.get))
