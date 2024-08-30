import numpy as np 
import pandas as pd 
# Missing values 
def missing_values(dff):
    # 1 - make the list of features which has missing values
    features_with_na=[features for features in dff.columns if dff[features].isnull().sum()>1]
    print(features_with_na)

    # 2- print the feature name and the percentage of missing values
    for feature in features_with_na:
        print(feature, np.round(dff[feature].isnull().mean()*100, 4),  ' % of missing values')


# Incorrect_entries 
def negative_values(dff):
    # Columns with negative value
    columns_with_negatives = []

    # Loop over each column
    for column in dff.columns:
        if dff[column].dtype != object:
            if (dff[column] < 0).any():  # Check if any value in the column is negative
                columns_with_negatives.append(column)

    # Print the list of columns with negative values
    print(columns_with_negatives)




    
   