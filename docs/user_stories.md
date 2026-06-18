# User Stories

## User story 1 - Marketing analyst

As a marketing analyst, I want to identify customers who are more likely to subscribe to a financial product so that I can prioritise outreach and reduce wasted campaign effort.

Acceptance criteria:
- The system outputs a predicted class.
- The system outputs a conversion probability.
- The model is evaluated using metrics suitable for imbalanced classification.

## User story 2 - ML engineer

As an ML engineer, I want the training pipeline to be reproducible so that model results can be tested, tracked, and improved safely.

Acceptance criteria:
- Training code can be run from the command line.
- Dependencies are listed in requirements.txt.
- Model metrics are logged.
- Tests can be run automatically.

## User story 3 - Product or API user

As an API user, I want to send customer and campaign features to an endpoint and receive a prediction so that the model can be integrated into another product.

Acceptance criteria:
- The API has a health endpoint.
- The API has a prediction endpoint.
- The request and response schemas are documented.
