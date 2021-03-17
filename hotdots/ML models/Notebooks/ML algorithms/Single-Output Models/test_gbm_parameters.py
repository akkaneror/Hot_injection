"""Nosetests for gbm_parameter functions"""

import pandas as pd
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
    """not sure yet"""
    best_estimator=highest_r2_calculator(x_train, y_train, x_test, y_test)
    low=1
    high=10
    assert low<best_estimator<high, "estimator outside of range"
