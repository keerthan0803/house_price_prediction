# Backend for House Price Predictor using scikit-learn model
import os
import pickle
from flask import Flask, request, jsonify, send_from_directory
import numpy as np

app = Flask(__name__)

MODEL_PATH = 'model.pkl'

def check_model_exists():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Model file '{MODEL_PATH}' not found.\n"
            "Please run 'linear.py' first to train and save the model."
        )

check_model_exists()

# Load the scikit-learn model
with open(MODEL_PATH, 'rb') as f:
    model_data = pickle.load(f)
    model = model_data['model']
    label_encoders = model_data.get('label_encoders', {})
    feature_names = model_data['feature_names']
    scaler = model_data.get('scaler', None)
    poly = model_data.get('poly', None)
    model_type = model_data.get('model_type', 'Unknown')
print(f"Model loaded successfully! ({model_type})")
print("Expected features:", feature_names)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        # Extract features in the correct order
        features = [float(data[k]) for k in feature_names]
        features_np = np.array([features])
        
        # Apply transformations if needed
        if poly is not None:
            features_np = poly.transform(features_np)
        if scaler is not None:
            features_np = scaler.transform(features_np)
        
        prediction = model.predict(features_np)
        pred_value = float(prediction[0])
        return jsonify({'prediction': round(pred_value, 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    # Use environment variable PORT for deployment platforms like Render
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
