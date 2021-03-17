"""Nosetests for gbm_parameter functions"""

import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from gbm_parameters import highest_r2_calculator

# load augmented df
df = pd.read_csv('../../../Datasets/augmented_data.csv')

#Separate x and y data
x = df.drop(columns =[
		'Unnamed: 0','Unnamed: 0.1','Diameter_nm','Absorbance max (nm)', 'PL max (nm)'],
                inplace = False, axis = 1) #keep synthesis parameters that matter
y = df['Diameter_nm'].values #will predict diameter

#split dataset into train and test set
x_train, x_test, y_train, y_test = train_test_split(
					x, y, test_size=0.25, random_state=8, shuffle=True)

def test_1():
    """make sure best estimator is actually in defined range"""
    best_estimator=highest_r2_calculator(x_train, y_train, x_test, y_test)
    low=1
    high=10
    assert low<best_estimator<high, "estimator outside of range"

def test_2():
    """make sure r2 is between -1 and 1"""
    best_estimator=highest_r2_calculator(x_train, y_train, x_test, y_test)
    gbm = GradientBoostingRegressor(n_estimators=best_estimator)
    gbm.fit(x_train, y_train)
    y_predict = gbm.predict(x_test)
    r2_value = r2_score(y_test, y_predict)
    assert -1 < r2_value < 1, "r2 outside expected range"

def test_3():
    """make sure we are actually pulling out highest r2"""
    best_estimator=highest_r2_calculator(x_train, y_train, x_test, y_test)
    r2_dict = {}
    low = 1
    high = 10
    for estimator in np.arange(low, high, 1):
        gbm = GradientBoostingRegressor(n_estimators=estimator)
        gbm.fit(x_train,y_train)
        y_predict = gbm.predict(x_test)
        r2_value = r2_score(y_test, y_predict)
        r2_dict[estimator] = r2_value
    return r2_dict
    gbm = GradientBoostingRegressor(n_estimators=best_estimator)
    gbm.fit(x_train, y_train)
    y_predict = gbm.predict(x_test)
    r2_value = r2_score(y_test, y_predict)
    assert r2_value==max(r2_dict), "max r2 and calculated r2 do not match"
