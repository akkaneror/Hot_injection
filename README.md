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
            |- Use Cases and Comp Spec Illustration.pdf
        |- hotdots
            |- ML models
                |- Datasets
                    |- CdSe - Raw.csv
                    |- CdSe for Abs (S&E).csv
                    |- CdSe for Diameter (S&E).csv
                    |- CdSe for PL (S&E).csv
                    |- CdSe scaled.csv
                    |- Models_Metrics.csv
                    |- augmented_data.csv
                    |- documentation.txt
                |- Notebooks
                    |- Comparison Santos et al
                        |- Analysis_Summary.ipynb
                        |- Models_Metrics.csv
                        |- Recreate figures test 2.ipynb
                        |- Recreate figures test.ipynb
                    |- Dataset Cleaning
                       |- Data Augmentation
                           |- Augmenting Data.ipynb
                           |- Optimization ML Models for Data Augmentation.ipynb
                           |- abs_filler.csv
                           |- augmented absorbance.csv
                           |- augmented_data.csv
                           |- pl_filler.csv
                           |- random_forest_ab.joblib
                           |- random_forest_pl.joblib
                       |- Standardization and One-Hot Encoding.ipynb
                    |- ML algorithms
                       |- Single-Output Models
                           |- Decision Tree.ipynb
                           |- Extra Trees.ipynb
                           |- Gradient Boosting Machine.ipynb
                           |- KNN.ipynb
                           |- Multilinear Regression.ipynb
                           |- Random Forest.ipynb
                           |- Ridge Regression.ipynb
                           |- SVR (kernel='linear','rbf).ipynb
                       |- Multi-Output Models.ipynb
        |- .gitignore
        |- .travis.yml
        |- LICENSE.txt
        |- README.md
        |- environment.yml
                    
                    
            
## Getting started with the hotdots package 

There are 2 primary submodules inside this hotdots package: Usecase 1 and Usecase 2. 

Usecase 1 contains the components for the predictive package, which allows a user to enter certain experimental parameters for the hot injection synthesis of CdSe quantum dots after which package will use the extra trees algorithm to predict the synthesized CdSe dots' diameter, absorbance and emission. 

Usecase 2 contains the analysis that our team conducted on the various ML models' predictive capabilities in predicting the diameter, absorbance and emission. It also includes our comparative analysis with the **[paper](https://pubs.acs.org/doi/10.1021/acs.jpcc.0c05993)**, from which we obtained our initial dataset. 


### Usecase 1: Streamlit - User Interface

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
4. Enter the command `streamlit run main.py`
5. Copy the URL into your browser and make some quantum dots!


#### User Interface Module Code

The user interface code is in a file called `main.py` inside the `Streamlit-User Interface`. The test file for this file is called `test_main.py`. 


### Usecase 2: ML Model Analysis

The `Datasets` submodule contain the datasets that were used to train the various ML models explored. The original **[dataset](https://pubs.acs.org/doi/suppl/10.1021/acs.jpcc.0c05993/suppl_file/jp0c05993_si_004.txt)**  was part of the supplementary information of **[Machine Learning Tools to Predict Hot Injection Syntheses Outcomes for II-VI and IV-VI Quantum Dots] (https://pubs.acs.org/doi/10.1021/acs.jpcc.0c05993)**. All of the input data were standardized (numerical inputs) and one-hot encoded (categorical inputs). Data augmentation was used to impute the "None" values of some of the absorbance and emission entries. The resultant dataset after these transformations is labelled as `augmented_data.csv` in the `Datasets` submodule. 

The `Notebooks` submodule contains all of the analytic components. A summary of predictive accuracies of each of the ML models explored could be found in the `Analysis` submodule. The dataset standardization, one-hot encoding and augmentation is documented in the `Dataset cleaning` submodule. The `Machine Learning Models` submodules include all of the different ML models that were explored in this project, which includes both single-output and multi-output ML models.



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
