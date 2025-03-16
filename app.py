import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template

# Load the trained model
with open("regmodel.pkl", "rb") as file:
    model = pickle.load(file)

# Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        try:
            # Get user inputs from the form
            features = [float(request.form[f'feature{i}']) for i in range(8)]
            features = np.array(features).reshape(1, -1)

            # Make prediction
            prediction = model.predict(features)[0]
        except ValueError:
            prediction = "Invalid input! Please enter numeric values."

    return render_template("home.html", prediction=prediction)

# API endpoint for making predictions
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON request data
        data = request.get_json()

        # Extract features
        features = np.array(data["features"]).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)[0]

        return jsonify({"prediction": prediction})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

