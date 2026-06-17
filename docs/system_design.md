# Initial System Design

## Chapter 1 architecture sketch

```text
Customer / campaign data
        |
        v
Data cleaning and validation
        |
        v
Feature engineering pipeline
        |
        v
Model training and evaluation
        |
        v
MLflow experiment tracking
        |
        v
Saved model artifact
        |
        v
FastAPI prediction service
        |
        v
Prediction: subscribe / not subscribe

## System type

This project will use a classification pipeline with offline training and online inference.

## High-level architecture

```text
Raw data
   ↓
Data validation and cleaning
   ↓
Feature engineering and preprocessing
   ↓
Model training
   ↓
Model evaluation
   ↓
Experiment tracking with MLflow
   ↓
Model persistence
   ↓
FastAPI inference service
   ↓
Prediction response
```

## Storage layer

The storage layer contains:

- Raw dataset
- Processed dataset
- Trained model artifacts
- MLflow experiment metadata
- Evaluation reports

## Compute layer

The compute layer contains:

- Data loading code
- Preprocessing pipeline
- Model training code
- Model evaluation code
- Hyperparameter tuning code
- Prediction logic

## Application layer

The application layer contains:

- FastAPI service
- Request schema
- Response schema
- Model loading logic
- Health check endpoint
- Prediction endpoint

## Future AWS deployment

Planned AWS components:

- S3 for data and model artifacts
- ECR for Docker image storage
- ECS, App Runner, or SageMaker endpoint for serving
- CloudWatch for logs and monitoring
- GitHub Actions for CI/CD

## Future Azure deployment

Planned Azure components:

- Azure Blob Storage for data and model artifacts
- Azure Container Registry for Docker image storage
- Azure Container Apps or Azure ML managed endpoint for serving
- Azure Application Insights for logs and monitoring
- GitHub Actions for CI/CD