from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

with open("model.pkl", "rb") as model_file:
    churn_model = pickle.load(model_file)

with open("scaler.pkl", "rb") as scaler_file:
    feature_scaler = pickle.load(scaler_file)

@app.route("/")
def home():
    return "Customer Churn Prediction API is running successfully"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_data = request.get_json()

        if not input_data:
            return jsonify({"error": "No input data provided"}), 400

        input_df = pd.DataFrame([input_data])
        scaled_input = feature_scaler.transform(input_df)

        churn_prediction = churn_model.predict(scaled_input)[0]
        churn_probability = churn_model.predict_proba(scaled_input)[0][1]

        response = {
            "prediction": "Churn" if churn_prediction == 1 else "No Churn",
            "probability": round(float(churn_probability), 3)
        }

        return jsonify(response)

    except Exception as error:
        return jsonify({
            "error": "Prediction failed",
            "details": str(error)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)

