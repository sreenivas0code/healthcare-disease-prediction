from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Load dataset
data = pd.read_csv("dataset.csv")

X = data.drop("disease", axis=1)
y = data["disease"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    age = float(request.form["age"])
    glucose = float(request.form["glucose"])
    bp = float(request.form["bp"])
    bmi = float(request.form["bmi"])
    insulin = float(request.form["insulin"])

    input_data = pd.DataFrame(
        [[age, glucose, bp, bmi, insulin]],
        columns=X.columns
    )

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        result = "Disease Likely"
    else:
        result = "No Disease"

    return render_template("index.html", prediction_text=result)


if __name__ == "__main__":
    app.run(debug=True)