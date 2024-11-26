from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle

app = FastAPI()

# Załaduj model ocSVM
with open('oc_svm_model.pkl', 'rb') as f:
    model = pickle.load(f)

class Data(BaseModel):
    features: list

@app.post("/predict/")
async def predict(data: Data):
    features = np.array(data.features).reshape(1, -1)
    score = model.decision_function(features)
    return {"score": score[0]}