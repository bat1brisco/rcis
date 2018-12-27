from flask import jsonify, Blueprint
from module.controller.usercontroller import *
user = Blueprint('user', __name__)

@user.route('/test/<bran>', methods=['GET'])
def home(bran):
    
    return jsonify({'dong': bran})