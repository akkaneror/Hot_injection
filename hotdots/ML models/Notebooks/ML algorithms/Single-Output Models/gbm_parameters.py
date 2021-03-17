"""This module identifies gradient boosting machine parameters that give highest r2 value"""

import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score
from tqdm import tqdm

def highest_r2_calculator(x_train, y_train, x_test, y_test):
    """iterates over estimator values to find the one that gives highest r2"""
    r2_dict = {}
    low = 1
    high = 10
    for estimator in tqdm(np.arange (low, high, 1)):
        gbm = GradientBoostingRegressor(n_estimators=estimator)
        gbm.fit(x_train,y_train)
        y_predict = gbm.predict(x_test)
        r2_value = r2_score(y_test, y_predict)
        r2_dict[estimator] = r2_value

    return max(r2_dict, key=r2_dict.get)
