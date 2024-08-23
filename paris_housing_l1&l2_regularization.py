# -*- coding: utf-8 -*-
"""Paris Housing-L1&L2-Regularization.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oF-u_d3MDEk3nvXND-xXYKLJbuLlNrUG

##Introduction to the Paris Housing Price Prediction Dataset
###The Paris Housing Price Prediction dataset is a comprehensive dataset designed to provide insights into property pricing dynamics in Paris. This dataset is ideal for regression tasks, where the goal is to predict the price of a property based on various features. The dataset includes several key factors that influence housing prices, making it suitable for exploring different regression techniques and regularization methods like Lasso (L1) and Ridge (L2).

##Dataset Overview
###The dataset contains information about various properties in Paris, including features that are typically relevant in determining real estate prices. These features range from property-specific characteristics like the number of bedrooms to more contextual attributes like the property’s location within the city.

##Key Features:
1. Square Meters: The size of the property in square meters, a crucial determinant of price.
2. Number of Rooms: The total number of rooms in the property, including living rooms and bedrooms.
3. Number of Bedrooms: Specifies the number of bedrooms, which directly influences the valuation of the property.
4. Floors: Indicates the floor level on which the property is situated, which can impact desirability and hence, price.
5. Property Age: The age of the building in years, as older properties may either be valued less or more depending on historical significance.
6. Location: Encoded location data that captures different districts or neighborhoods within Paris. Location is one of the most influential factors in housing prices.
7. Transport Accessibility: Information related to proximity to metro stations or other public transport facilities.

##Objective:

###The main objective of this project is to predict housing prices using linear regression models, incorporating L1 (Lasso) and L2 (Ridge) regularization techniques. By applying these regularization methods, we aim to improve the generalization capability of the model while preventing overfitting, which is common in complex real-world datasets.

##Why Regularization?
###In linear regression, overfitting can occur when the model becomes too complex by fitting noise in the dataset. Regularization methods such as Lasso and Ridge introduce a penalty on the coefficients, encouraging simpler models that generalize better to unseen data. This is especially important in housing price prediction, where capturing underlying trends without being misled by outliers or noise is key to making reliable predictions.

##Exploratory Data Analysis (EDA) and Feature Engineering:
###The dataset will first undergo thorough exploratory data analysis (EDA) to uncover relationships between features and housing prices. We will then preprocess the data by handling missing values, standardizing features, and encoding categorical variables. Feature engineering may be applied to derive additional meaningful insights from the existing features.

##Modeling Approach:
###We will apply both Lasso and Ridge regression models to understand the impact of L1 and L2 regularization techniques on the predictive performance. We will evaluate the models based on metrics like Mean Squared Error (MSE) and R-squared (R²) values, and further fine-tune the models by adjusting the regularization strength (alpha) to optimize performance.

##Conclusion:
###This dataset and project provide an excellent platform to explore the use of regularization in regression analysis. By comparing Lasso and Ridge, we aim to strike a balance between model accuracy and simplicity, ensuring the model not only fits well on the training data but also performs effectively on new, unseen data.
"""

import pandas as pd # Pandas is a powerful library for data manipulation and analysis.
import numpy as np # NumPy is a powerful tool for numerical computations in Python

"""##Loading the Dataset"""

df= pd.read_csv("ParisHousing (1).csv") #The df = pd.read_csv line reads a CSV file into a DataFrame named df using the pandas library.

df.head()

df.shape # Displays the total count of the Rows and Columns respectively.

df.info() #Displays the total count of values present in the particular column along with the null count and data type.

print(df.isnull().sum()) #Is used to display the dimensions of the DataFrame df. Giving you a quick overview of the size of your dataset.

df.info() #Displays the total count of values present in the particular column along with the null count and data type.

"""###There is no null value in the dataset."""

X= df.iloc[:,:-1].values #Extracts all the columns of the DataFrame df except the last one

y = df.iloc[:,-1].values #Extracts the last column of the DataFrame df and stores its underlying NumPy array representation in the variable y.

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""####This code splits your data (X - features, and y - target variable) into training and testing sets. 80% of the data is used for training (X_train, y_train) and 20% for testing (X_test, y_test). The random_state ensures that the split is reproducible."""

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

"""Imagine you're preparing ingredients for a recipe. Some ingredients might be measured in cups, others in teaspoons. To make sure everything blends well, you need to standardize the measurements.

That's exactly what this code does! It standardizes the data to ensure all features are on a similar scale. It calculates the average (mean) and spread (standard deviation) of each feature in the training data (X_train) and adjusts the values accordingly. The same transformation is then applied to the testing data (X_test) to maintain consistency. This helps the machine learning models perform better.
"""

from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error, r2_score

lasso = Lasso(alpha=1)  # Adjust alpha for regularization strength
lasso.fit(X_train_scaled, y_train)

#lasso = Lasso(alpha=1): Creates a Lasso regression model with a regularization strength (alpha) of 1.
#This parameter controls how much the model penalizes large coefficients, helping to prevent overfitting.
#lasso.fit(X_train_scaled, y_train): Trains the Lasso model using the standardized training data (X_train_scaled) and
#corresponding target values (y_train). The model learns the relationship between the features and the target to make predictions.

# Predict on test set
y_pred_lasso = lasso.predict(X_test_scaled)

# Calculate accuracy metrics
mse_lasso = mean_squared_error(y_test, y_pred_lasso)
r2_lasso = r2_score(y_test, y_pred_lasso)

print(f"Lasso Regression - MSE: {mse_lasso}, R2: {r2_lasso}")

from sklearn.linear_model import Ridge

ridge = Ridge(alpha=0.01)  # Adjust alpha for regularization strength
ridge.fit(X_train_scaled, y_train)

# Predict on test set
y_pred_ridge = ridge.predict(X_test_scaled)

# Calculate accuracy metrics
mse_ridge = mean_squared_error(y_test, y_pred_ridge)
r2_ridge = r2_score(y_test, y_pred_ridge)

print(f"Ridge Regression - MSE: {mse_ridge}, R2: {r2_ridge}")

from sklearn.model_selection import GridSearchCV

# For Lasso
lasso_cv = GridSearchCV(Lasso(), {'alpha': [0.01, 0.1, 1, 10]}, cv=5)
lasso_cv.fit(X_train_scaled, y_train)
print(f"Best alpha for Lasso: {lasso_cv.best_params_['alpha']}")

# For Ridge
ridge_cv = GridSearchCV(Ridge(), {'alpha': [0.01, 0.1, 1, 10]}, cv=5)
ridge_cv.fit(X_train_scaled, y_train)
print(f"Best alpha for Ridge: {ridge_cv.best_params_['alpha']}")

"""This code uses GridSearchCV to automatically try different values for the alpha parameter in your Lasso model. It tests the values [0.01, 0.1, 1, 10], evaluates their performance using 5-fold cross-validation (cv=5), and determines which alpha results in the best model performance. This helps you optimize your Lasso model for better predictions. And same is done with Ridge."""

