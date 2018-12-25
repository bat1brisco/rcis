from flask import jsonify, Blueprint
from controller.usercontroller import *
user = Blueprint('user', __name__)

@user.route('/test/<bran>', methods=['GET'])
def home(bran):
    d = 
    return jsonify({'dong': bran})