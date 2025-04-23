# app/model.py

import joblib


model = joblib.load("models/classifier.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")


def classify_email(text: str) -> str:
    """
    Predict the category of the given email text.
    """
    features = vectorizer.transform([text])
    return model.predict(features)[0]
