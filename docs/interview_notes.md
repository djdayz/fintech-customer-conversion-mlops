# Interview notes
## Model vs ML system

A machine learning model is the algorithm trained on data to make predictions.

A machine learning system includes the model plus everything needed to make it useful in practice: data loading, preprocessing, training, evaluation, experiment tracking, model tracking, model saving, API serving, testing, monitoring and retraining.

For this fintech project, the model predicts whether a customer will subscribe to a financial product. The system makes that prediction reproducible, testable, deployable, and usable by another application.

## Features and target

In supervised learning, X contains the input features and y contains the target label.

For this project:
- X = customer and campaign features
- y = whether the customer subscribed

The target column must be removed from X because the model should not be given the answer as an input. 
