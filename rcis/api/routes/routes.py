from flask import jsonify, Blueprint
from module.controller.usercontroller import *
user = Blueprint('user', __name__)

@user.route('/test/<bran>', methods=['GET'])
def home(bran):
    res = usr_controller.main()
    return jsonify({'dong': bran})