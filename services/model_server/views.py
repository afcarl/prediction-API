from flask import Blueprint, jsonify, request, render_template
from sqlalchemy import exc

from services.model_server.models import Dataset
from services import db


data_blueprint = Blueprint('data', __name__, template_folder='./templates')


@data_blueprint.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })


@data_blueprint.route('/dataset', methods=['GET'])
def get_datasets():
    datasets = Dataset.query.all()
    dataset_list = [{'name': dataset.dataset_name,
                     'url': dataset.url,
                     'task': dataset.task_type,
                     'created_at': dataset.created_at} for dataset in datasets]
    response_object = {'status': 'success',
                       'data': {
                           'datasets': dataset_list
                       }}
    return jsonify(response_object), 200


@data_blueprint.route('/dataset', methods=['POST'])
def add_dataset():
    # SOMETHING WITH .form
    post_data = request.get_json()
    fail_response_object = {
        'status': 'fail',
        'message': 'Invalid payload'
    }
    if not post_data:
        fail_response_object['extra'] = 'No post data'
        return jsonify(fail_response_object), 400
    try:
        dataset_name = post_data['name']
        dataset_url = post_data['url']
        dataset_task = post_data['task']
    except:
        fail_response_object['extra'] = 'One of the keywords not correct'
        return jsonify(fail_response_object), 400
    try:
        dataset = db.session.query(Dataset).filter((Dataset.dataset_name == dataset_name) | (Dataset.url == dataset_url)).first()
        if not dataset:
            dataset = Dataset(dataset_name=dataset_name, url=dataset_url, task_type=dataset_task)
            db.session.add(dataset)
            db.session.commit()
            response_object = {
                'status':' success',
                'message': 'Dataset `{}` has been added'.format(dataset_name)
            }
            return jsonify(response_object), 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'Dataset already exists.'
            }
            return jsonify(response_object), 400
    except exc.IntegrityError as e:
        db.session.rollback()
        return jsonify(fail_response_object), 400


@data_blueprint.route('/', methods=['GET'])
def index():
    datasets = Dataset.query.all()
    return render_template('index.html', datasets=datasets)
