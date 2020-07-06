import numpy as np
import flask
from flask import Flask, request, jsonify, render_template
import pickle
import math

app = Flask(__name__)
model = pickle.load(open('RandomForestRegressor.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    int_features = [['Year', 'Engine_CC', 'Power_bhp']]
    prediction = model.predict(int_features)
    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text="Car Price should be {}".format(output))


if __name__ == '__main__':
    app.run()
