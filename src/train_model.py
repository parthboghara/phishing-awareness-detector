import os
import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from features import extract_features

# Load dataset
df = pd.read_csv("../dataset/sample_urls.csv")

X = df["url"].apply(extract_features).tolist()
y = df["label"].map({"legitimate": 0, "phishing": 1})

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

accuracy = accuracy_score(y_test, model.predict(X_test))
print(f"[+] Model Accuracy: {accuracy * 100:.2f}%")

os.makedirs("../model", exist_ok=True)
joblib.dump(model, "../model/phishing_model.pkl")

print("[+] Model saved successfully")
