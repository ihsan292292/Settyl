# Settyl Data Science And Machine Learning Engineer Task

[yy_BIwbeTso.webm](https://github.com/ihsan292292/Settyl/assets/97184876/2b573266-7830-43ed-846e-1e28a0992cf1)


This repository contains code to deploy a text classification model using FastAPI and ngrok.


### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- ngrok authentication token (sign up for ngrok and obtain the token)


## Files

- `settyl.ipynb`: jupyternotebook to model creation, training and deploy the FastAPI app with ngrok.
- `model.py`: Python script containing the FastAPI app, model loading, and prediction logic.
- `requirements.txt`: List of required Python packages.
- `tokenizer.pkl`: Serialized tokenizer object for text preprocessing.
- `encoder.pkl`: Serialized encoder object for label encoding.
- `save/`: Directory containing the saved model artifacts.


## Techniques Used

1. **Text Preprocessing**:
   - Tokenization and cleaning of text data were performed to prepare it for model training.

2. **Data Exploration**:
   - Exploratory data analysis was conducted to understand the distribution of internal and external status labels in the dataset.

3. **Class Balancing**:
   - The imbalanced dataset was balanced using the Synthetic Minority Over-sampling Technique (SMOTE) to ensure equal representation of each class during model training.

4. **Model Architecture**:
   - A bidirectional Long Short-Term Memory (LSTM) neural network architecture was employed for sequence classification tasks.

5. **Hyperparameter Tuning**:
   - Hyperparameters such as embedding dimension, LSTM units, and learning rate were tuned to optimize model performance.

6. **Model Evaluation**:
   - Model performance was evaluated using metrics such as accuracy and loss on both training and validation datasets.

7. **Model Serialization**:
   - Trained model, tokenizer, and encoder objects were serialized using the `pickle` library for later use in deployment.

8. **API Development**:
   - FastAPI framework was used to develop an API endpoint for model prediction. The API accepts input text, preprocesses it, and returns the predicted label.

9. **Error Handling**:
   - Appropriate error handling mechanisms were implemented to handle exceptions during model prediction and API requests, providing meaningful error messages to the user.

10. **Deployment**:
    - The model and API were deployed using ngrok, enabling the model to be accessible via a public URL for real-world usage.

