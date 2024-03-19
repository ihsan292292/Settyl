from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import string
import re

# Initialize FastAPI app
app = FastAPI()

# Load tokenizer and encoder
with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

with open('encoder.pkl', 'rb') as f:
    encoder = pickle.load(f)


# Load model
model = load_model("model.h5")

# Maximum sequence length
maxlen = model.input_shape[1]

# Clean text function
def clean_text(input_string):
    pattern = r'[{}]'.format(re.escape(string.punctuation))
    output_string = re.sub(pattern, ' ', input_string)
    return output_string.lower()

# Prediction function
def predict_outcome(text):
    input_sequence = tokenizer.texts_to_sequences([clean_text(text)])
    padded_input_sequence = pad_sequences(input_sequence, truncating="post", padding="post", maxlen=maxlen) if len(input_sequence[0]) <= maxlen else pad_sequences([list(filter(lambda x: x != 1, input_sequence[0]))], truncating="post", padding="post", maxlen=maxlen)
    pred_index = model.predict(padded_input_sequence, verbose=0)[0].argmax()
    return pred_index

# API request body model
class PredictionRequest(BaseModel):
    text: str

# API response model
class PredictionResponse(BaseModel):
    predicted_label: str

# Define prediction endpoint
@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    prediction_index = predict_outcome(request.text)
    predicted_label = encoder.categories_[0][prediction_index]
    return {"predicted_label": predicted_label}