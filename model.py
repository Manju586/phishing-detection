import sys
import os
print(os.getcwd())
print(sys.path)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import myutils

# Load dataset
data = pd.read_csv("dataset.csv")

# Extract features
X_raw = data["url"].apply(lambda x: myutils.extract_features(x))
X = pd.DataFrame(X_raw.tolist(), columns=[f'f{i}' for i in range(6)])

y = data["label"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

print(f"Accuracy: {model.score(X_test, y_test):.2f}")

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved!")
print("Script completed.")
