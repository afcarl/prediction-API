from flask import Flask, request, jsonify

import sys, logging

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.DEBUG)


@app.route('/predict', methods=['POST'])
def predict():
    app.logger.debug(request.get_json())
    return_dict = dict()
    app.logger.debug(return_dict)
    return_dict['status'] = 'success'
    return_dict['message'] = 'logged prediction request'
    return jsonify(return_dict), 201


@app.route('/register_model', methods=['POST'])
def register_model():
    app.logger.debug(request.get_json())
    return_dict = dict()
    app.logger.debug(return_dict)
    return_dict['status'] = 'success'
    return_dict['message'] = 'logged model register'
    return jsonify(return_dict), 201
