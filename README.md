# FinTech Customer Conversion MLOps System

## Project overview

This project builds an end-to-end machine learning engineering system for predicting whether a banking customer is likely to subscribe to a financial product after a marketing campaign.

The goal is not only to train a machine learning model, but to build a production-style ML system with reproducible training, preprocessing pipelines, model evaluation, experiment tracking, testing, API inference, containerisation, and cloud deployment planning.

## Why this project?

Many finance and fintech teams use machine learning for customer targeting, risk scoring, fraud detection, churn prediction, and decision support. This project focuses on a supervised classification use case and develops it using machine learning engineering and MLOps practices.

## ML engineering scope

This project will include:

- Data cleaning
- Exploratory data analysis
- Feature engineering
- Preprocessing pipeline
- Baseline model
- Improved model
- Model evaluation
- Error analysis
- Hyperparameter tuning
- MLflow experiment tracking
- Model persistence
- Unit tests
- FastAPI inference service
- Docker containerisation
- AWS deployment plan
- Azure deployment plan

## Textbook alignment

This project follows the structure of *Machine Learning Engineering with Python, Second Edition*:

- Chapter 1: ML engineering roles, real-world ML systems, and high-level system design
- Chapter 2: Discover, Play, Develop, Deploy workflow
- Chapter 3: Model factory, pipelines, retraining, model persistence, and drift
- Chapter 4: Packaging, testing, logging, error handling
- Chapter 5: Deployment patterns, microservices, containers, and cloud deployment
- Chapter 8: ML microservice with FastAPI

## Initial system design

The system will begin as a batch training pipeline and will later expose predictions through a FastAPI microservice.

High-level layers:

1. Storage layer: dataset, model artifacts, MLflow runs
2. Compute layer: preprocessing, training, evaluation, prediction
3. Application layer: FastAPI inference endpoint

## Status

Current stage: Chapter 1 — problem framing and repository setup.