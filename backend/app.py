# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import os

app = Flask(__name__)
CORS(app)

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

model = None
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
    print("Model loaded from", MODEL_PATH)
else:
    print("Warning: model.pkl not found at", MODEL_PATH)

@app.route("/")
def hello():
    return "Heart Disease Prediction API is running."

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded. Put model.pkl in backend/ folder."}), 500

    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON payload received"}), 400

    # Expecting features in specific order; match frontend
    try:
        features = [
            float(data.get("age", 0)),
            float(data.get("sex", 0)),
            float(data.get("cp", 0)),
            float(data.get("trestbps", 0)),
            float(data.get("chol", 0)),
            float(data.get("fbs", 0)),
            float(data.get("restecg", 0)),
            float(data.get("thalach", 0)),
            float(data.get("exang", 0)),
        ]
    except Exception as e:
        return jsonify({"error": "Invalid input values", "details": str(e)}), 400

    X = np.array(features).reshape(1, -1)
    try:
        pred = model.predict(X)[0]
        # if classifier supports predict_proba:
        proba = None
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(X).max().item()
        result = {
            "prediction": int(pred),
            "probability": proba
        }
        # Interpret prediction (depends on how model was trained)
        result["label"] = "No Heart Disease" if int(pred) == 0 else "Heart Disease"
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": "Prediction failed", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
