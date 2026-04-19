import os

import pandas as pd
import joblib

from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("data/intents.csv")

# Inputs and outputs
X = df["text"]
y = df["intent"]

# Split data (stratified so each intent appears in train and test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Create pipeline (TF-IDF + ML model)
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression(max_iter=1000))
])

# Cross-validation on full data (stable metric for small balanced sets)
cv_scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")
print("5-fold CV accuracy (mean +/- std):", f"{cv_scores.mean():.3f} +/- {cv_scores.std():.3f}")
print("CV folds:", cv_scores.round(3))

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate holdout split
print("\nHoldout test accuracy:", accuracy_score(y_test, y_pred))
print("\nReport:\n", classification_report(y_test, y_pred, zero_division=0))

# Save model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/chatbot_model.pkl")

print("\nModel saved successfully!")