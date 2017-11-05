from flask import Blueprint, jsonify, request, render_template
from sqlalchemy import exc

from services.model_server.models import Model
from services import db


users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
