# Problem Statement

## Business problem

A financial institution wants to improve how it targets customers during marketing campaigns. Contacting every customer is expensive and inefficient. The business wants to identify customers who are more likely to subscribe to a financial product so that marketing resources can be focused more effectively.

## Machine learning problem

This is a supervised binary classification problem.

The model predicts whether a customer will subscribe to a financial product.

Target variable:

- `yes`: customer subscribed
- `no`: customer did not subscribe

## Why ML is appropriate

Machine learning is appropriate because the decision depends on patterns across multiple customer and campaign features. A rule-based system would be too rigid and may miss non-obvious interactions between variables.

## Expected users

Potential users include:

- Marketing analysts
- Data scientists
- Fintech product teams
- CRM teams
- ML engineers responsible for model deployment

## Success criteria

The model should:

- Perform better than a simple baseline
- Handle categorical and numerical features correctly
- Avoid data leakage
- Produce reproducible results
- Be deployable through an API
- Be trackable using experiment tracking
- Be testable through automated tests

## Initial ML metrics

Because this is likely to be an imbalanced classification problem, accuracy alone is not sufficient.

Primary metrics:

- F1-score
- Precision
- Recall
- ROC-AUC

## Initial deployment pattern

The first version will use batch training and API-based inference.

Training will be run offline. The trained model will then be loaded by a FastAPI service to return predictions.