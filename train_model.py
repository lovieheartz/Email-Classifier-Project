# train_model.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib
from app.utils import clean_text
from app.logger import get_logger

logger = get_logger()

df = pd.read_csv("data/raw/supports_emails.csv")
df["email"] = df["email"].apply(clean_text)

X = df["email"]
y = df["type"]

vectorizer = TfidfVectorizer()
X_vect = vectorizer.fit_transform(X)

model = RandomForestClassifier()
model.fit(X_vect, y)

joblib.dump(model, "models/classifier.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

logger.info("Model and vectorizer saved to /models/")
