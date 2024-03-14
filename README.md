# Profitability_prediction
### Problem Statement: 
Financial Analysts want to predict if a company will be profitable or not in next 5 years.

### Objective: 
Our end goal will be to enable shareholders optimizing growth parameters using prediction output along with keep investors aware of current business trend for making a profitable investment.
Solution Steps:

*	‘class’ is the target variable with two labels ‘0’ and ‘1’ which denotes ‘not profitable’ and ‘profitable’ respectively. 
   The final predictive model became a classification model.
*	Imputed missing values of columns contains more than 30% of it.
*	Removed highly skewed variables from data.
*	Standardized all numerical variables, removed values having z-score greater than 3 and less than -3 from all features as a part of outlier treatment.
*	For bivariate analysis, used grouped box and bar plots for checking the variation of target variable with respect to predictors.
*	Extracted a new feature named ‘Altman Score’ to check if any organization is going to become profitable or not in next 5 years. 
*	Performed Anova and Chi-square tests for selection of final predictors.
*	Among different classification models, tuned Random- forest and Decision tree had drawn highest accuracy and precision score as 0.89 and 0.90 respectively.
*	These models are also showing better performance for F1-score.

