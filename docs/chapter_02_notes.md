# Chapter 2 Notes - The Machine Learning Development Process

## Main idea

A successful ML engineering project needs a structured workflow, not just modelling.

The textbook uses four stages:

1. Discover
2. Play
3. Develop
4. Deploy

## Discover

Goal: understand the business problem, users, data sources, success metrics, and why ML is appropriate.

For this project:
- Business problem: improve customer targeting in fintech marketing.
- ML task: binary classification.
- Success metrics: F1-score, precision, recall, ROC-AUC.
- Initial deployment: offline training with API inference.

## Play

Goal: explore the data and prove that the ML problem is feasible.

For this project:
- Use notebooks for EDA.
- Check class imbalance.
- Check missing values.
- Build a simple proof-of-concept model.

## Develop

Goal: turn exploratory work into reusable, tested, maintainable Python code.

For this project:
- Move preprocessing into src/fintech_mlops/features.py.
- Move training into src/fintech_mlops/train.py.
- Move evaluation into src/fintech_mlops/evaluate.py.
- Add unit tests.
- Add logging and config.

## Deploy

Goal: make the model usable outside the notebook.

For this project:
- Save the trained model.
- Load it in a FastAPI app.
- Add Docker support.
- Later map deployment to AWS and Azure.

## Key lesson

A machine learning project becomes an ML engineering project when it is reproducible, tested, packaged, tracked, and deployable.
