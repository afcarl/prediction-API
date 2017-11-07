from flask import Flask, request, jsonify
from model_dir.model import Model

import sys

app = Flask(__name__)

model = Model()
model.load()


@app.route('/predict', methods=['POST'])
def predict():
    return_dict = model.predict(request.get_json())
    return_dict['status'] = 'success'
    return_dict['message'] = 'pong!'
    return jsonify(return_dict), 201


@app.route('/ping2', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong2!'
    })
