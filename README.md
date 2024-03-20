# Settyl FastAPI Model Deployment

This repository contains code to deploy a text classification model using FastAPI and ngrok.

## Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- ngrok authentication token (sign up for ngrok and obtain the token)

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/ihsan292292/Settyl.git

## Files

- `settyl.ipynb`: jupyternotebook to model creation, training and deploy the FastAPI app with ngrok.
- `model.py`: Python script containing the FastAPI app, model loading, and prediction logic.
- `requirements.txt`: List of required Python packages.
- `tokenizer.pkl`: Serialized tokenizer object for text preprocessing.
- `encoder.pkl`: Serialized encoder object for label encoding.
- `save/`: Directory containing the saved model artifacts.