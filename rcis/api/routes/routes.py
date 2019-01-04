from flask import Flask, jsonify, Blueprint
from rcis.api.mold.controller.usercontroller import usr_controller

user = Blueprint('user', __name__)

@user.route('/test/<bran>', methods=['GET'])
def home(bran):
    res = usr_controller.main(bran)
    return jsonify(res)