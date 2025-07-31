import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

dataset = pd.read_csv('diabetes.csv')
dataset_X = dataset.iloc[:, [1, 2, 5, 7]].values

from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range=(0, 1))
dataset_scaled = sc.fit_transform(dataset_X)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        float_features = [float(x) for x in request.form.values()]
        final_features = [np.array(float_features)]

        if len(final_features[0]) != 4:
            return jsonify({'error': 'Please provide all 4 values.'}), 400

        prediction = model.predict(sc.transform(final_features))
        prediction_flag = int(prediction[0])
        
        # Get probability for diabetes (class 1)
        probability = model.predict_proba(sc.transform(final_features))[0][1]
        percentage = round(probability * 100, 2)

        if prediction_flag == 1:
            output = f"Positive. You may have Diabetes. Please consult a Doctor. (Confidence: {percentage}%)"
        else:
            output = f"Negative. You likely don't have Diabetes. (Confidence: {100-percentage}%)"

        return jsonify({
            'prediction_text': output,
        })
    except (ValueError, TypeError):
        return jsonify({'error': 'Please enter valid numerical values.'}), 400

if __name__ == "__main__":
    app.run(debug=True)