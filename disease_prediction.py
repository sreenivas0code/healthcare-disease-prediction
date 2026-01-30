print("Program started")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

print("Libraries imported")

data = pd.read_csv("dataset.csv")
print("Dataset loaded")

X = data.drop("disease", axis=1)
y = data["disease"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

new_patient = [[40, 120, 80, 26.5, 110]]
result = model.predict(new_patient)

if result[0] == 1:
    print("Disease Prediction: POSITIVE")
else:
    print("Disease Prediction: NEGATIVE")
