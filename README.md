# Hot_Injection

This is a class project for University of Washington CHEME 545/546 Winter 2021.

The purpose of this project is two-fold:
   
   1. Predict the size (nm), max absorbance (nm) and max photoluminescence emission (nm) outcomes of a hot injection synthesis of CdSe Quantum Dots based on a particular set of experimental conditions. 
   
   2. Compare and contrast the diameter prediction models explored in this project with those discussed in the paper **[Machine Learning Tools to Predict Hot Injection Syntheses Outcomes for II-VI and IV-VI Quantum Dots] (https://pubs.acs.org/doi/10.1021/acs.jpcc.0c05993)**. 
    
 
    

## Organization 

    Hot_injection
        |- doc
            |- component_specification.txt
            |- Initial Project Idea.pdf
            |- Technology Review.pdf
            |- User Cases and Comp Spec Illustration.pdf
        |- hotdots
            |- ML Model Analysis
                |-Datasets
                    |- CdSe - BetterthanRaw.csv
                    |- CdSe for Abs (S&E).csv
                    |- CdSe for Diameter (S&E).csv
                    |- CdSe for PL (S&E).csv
                    |- CdSe scaled.csv
                    |- augmented_data.csv
                    |- documentation.txt
                |-Notebooks
                    |- Analysis
                        |- Analysis Summary.csv
                        |- Analysis_summary.ipynb
                        |- Recreate figures test 2.ipynb
                        |- Recreate figures test.ipynb
                    |- Dataset cleaning
                        |- Data Augmentation
                            |- Augmenting Data.ipynb
                            |- CdSe scaled.csv
                            |- Optimization ML Models for Data Augmentation.ipynb
                            |- abs_filler.csv
                            |- augmented absorbance.csv
                            |- augmented_data.csv
                            |- pl_filler.csv
                            |- random_forest_ab.joblib
                            |- random_forest_pl.joblib
                        |- Column Transformer.ipynb
                    |- Machine Learning Models
                        |- Decision Tree.ipynb
                        |- Extra Trees.ipynb
                        |- Gradient Boosting Machine.ipynb
                        |- KNN.ipynb
                        |- Multi-Output Models.ipynb
                        |- Multilinear Regression.ipynb
                        |- Random Forest.ipynb
                        |- Ridge Regression.ipynb
                        |- SVR (kernel='linear','rbf).ipynb
            |-Streamlit-User Interface
                |- CdSe - BetterthanRaw.csv
                |- ET_reg.joblib
                |- main.py
                |- test_main.py
            |-documentation.txt
        |- LICENSE.txt
        |- README.md
        |- .gitignore
    
## Getting started with the hotdots package 

There are 2 primary submodules inside this hotdots package. Module 1, ML Model Analysis, outlines the various ML models that were investigated in this study. It also contains the ML model comparison with the **[paper](https://pubs.acs.org/doi/10.1021/acs.jpcc.0c05993)**. Module 2, Streamlit-User Interface, is the core module of this package that enables the prediction of 3 characteristics of CdSe quantum dots based on a particular set of experimental conditions. 


### Module 1:  ML Model Analysis

The `Datasets` submodule contain the datasets that were used to train the various ML models explored. The original **[dataset](https://pubs.acs.org/doi/suppl/10.1021/acs.jpcc.0c05993/suppl_file/jp0c05993_si_004.txt)**  was part of the supplementary information of **[Machine Learning Tools to Predict Hot Injection Syntheses Outcomes for II-VI and IV-VI Quantum Dots] (https://pubs.acs.org/doi/10.1021/acs.jpcc.0c05993)**. All of the input data were standardized (numerical inputs) and one-hot encoded (categorical inputs). Data augmentation was used to impute the "None" values of some of the absorbance and emission entries. The resultant dataset after these transformations is labelled as `augmented_data.csv` in the `Datasets` submodule. 

The `Notebooks` submodule contains all of the analytic components. A summary of predictive accuracies of each of the ML models explored could be found in the `Analysis` submodule. The dataset standardization, one-hot encoding and augmentation is documented in the `Dataset cleaning` submodule. The `Machine Learning Models` submodules include all of the different ML models that were explored in this project, which includes both single-output and multi-output ML models.


### Module 2: Streamlit - User Interface

This interface enables the user input certain experimental conditions after which the package will predict the resultant CdSe diameter (nm), absorbance (nm) and PL emission (nm) wavelength. The package utilizes extra trees model to create 

#### Prerequisites
Windows Users: Windows preview, **[Ubuntu](https://towardsdatascience.com/setting-up-a-data-science-environment-using-windows-subsystem-for-linux-wsl-c4b390803dd)**

Mac OS: Terminal

#### Package dependencies

* bokeh
* joblib
* numpy
* pandas
* sklearn
* streamlit

#### Installation of the package and accessing the user interface

1. Enter into your desired directory from your terminal
2. Enter the command `git clone https://github.com/UW-DIRECT-2021-NANO/Hot_injection.git`
3. Once inside the local, cloned repository, enter the command `cd hotdots/Streamlit-User\ Interface/`
4. Enter the command `Streamlit run main.py`


#### User Interface Module Code

The user interface code is in a file called `main.py` inside the `Streamlit-User Interface`. The test file for this file is called `test_modules.py`. 


## Running the Tests

Tests can be run using the **[nosetests](https://nose.readthedocs.io/en/latest/)** package. 

`nosetests Hot_injection/hotdots/Streamlit-user| Interface/ tests_modules.py`


### Style Tests

This project follows the PEP8 style using the **[pylint](https://www.pylint.org/)** code checker.  


## Built With



## Authors

* **Benedicte Diakubama** - MS, Chemical Engineering
* **Florence Dou** - PhD, Chemistry
* **Hao Anh Nguyen** - PhD, Chemistry
* **Harrison Sarsito** - MS, Chemical Engineering
