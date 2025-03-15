import pickle
import numpy as np
from flask import Flask, request, render_template

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

if __name__ == "__main__":
    app.run(debug=True)

