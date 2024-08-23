# Paris-Housing-L1-L2-Regularization

This project focuses on predicting housing prices in Paris using the Paris Housing Price Prediction dataset. The goal is to build robust regression models using Lasso (L1) and Ridge (L2) regularization techniques to enhance model performance and avoid overfitting.

Project Overview

Housing prices are influenced by a variety of factors such as property size, number of rooms, location, and accessibility. In this project, we explore the relationship between these factors and housing prices using regularized linear regression models. By applying Lasso and Ridge regression, we aim to develop models that strike a balance between accuracy and generalization, ensuring reliable predictions even on unseen data.

Dataset Features:

* Square Meters: Property size in square meters.
* Number of Rooms: Total number of rooms in the property.
* Number of Bedrooms: Number of bedrooms, an important indicator of property value.
* Floors: The floor level on which the property is situated.
* Property Age: Age of the building in years.
* Location: Encoded neighborhood information within Paris.
* Transport Accessibility: Proximity to public transportation like metro stations.

Project Workflow:

1* Data Preprocessing: Data cleaning, feature encoding, and scaling.
2. Exploratory Data Analysis (EDA): Visualizing relationships between features and prices.
3 Modeling:
* Lasso Regression (L1 Regularization)
* Ridge Regression (L2 Regularization)
4. Model Evaluation: Comparing model performance using metrics like Mean Squared Error (MSE) and R-squared (R²).
5. Hyperparameter Tuning: Fine-tuning the regularization strength (alpha) for optimal performance.

Key Takeaways:

* L1 regularization (Lasso) helps in feature selection by driving less important feature coefficients to zero.
* L2 regularization (Ridge) tends to shrink coefficients but keeps all features, balancing model complexity and performance.
* Both techniques help improve model generalization by penalizing overly complex models.

Conclusion:

This project demonstrates how regularization techniques can be applied to predict housing prices with improved accuracy and generalization. By leveraging the strengths of Lasso and Ridge regression, we achieve reliable predictions while avoiding overfitting.

