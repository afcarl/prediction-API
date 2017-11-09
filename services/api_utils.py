from flask import jsonify


def verify_api_request(request, required_keys=None):
    post_data = request.get_json()
    fail_response_object = {
        'status': 'fail',
        'message': 'Invalid payload'
    }
    if not post_data:
        return jsonify(fail_response_object), 400
    if required_keys is None:
        required_keys = []
    for key in required_keys:
        if key not in post_data:
            return jsonify(fail_response_object), 400
    return post_data, 201
