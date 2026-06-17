# Chapter 1 Checklist — Introduction to ML Engineering

## What I need to understand

- [ ] Difference between data scientist, ML engineer, MLOps engineer, and data engineer
- [ ] Why ML engineering is about productionisation, not just modelling
- [ ] What an ML solution looks like: storage layer, compute layer, application layer
- [ ] Difference between batch, API, and streaming ML systems
- [ ] Why ML is not always the right solution
- [ ] How this project creates business value
- [ ] How to explain this project in an interview

## Project decisions

### Problem type

Supervised binary classification.

### Project domain

Finance / fintech.

### Initial system pattern

Offline training with online API inference.

### Why not just a notebook?

A notebook can demonstrate exploration, but it does not show reproducibility, testing, deployment, or maintainability. This project aims to show those ML engineering skills.

## Interview answer draft

A machine learning model is only the algorithm trained on data. A machine learning system includes the model plus the surrounding engineering needed to make it useful: data pipelines, preprocessing, validation, experiment tracking, model storage, deployment, monitoring, and retraining.