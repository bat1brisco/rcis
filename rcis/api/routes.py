from flask import *

user = Blueprint('user', __name__)

@user.route('/test')
def home():
    d = {}
    return jsonify({'dong': 'koyla'})

if __name__ == '__main__':
    app.run(debug=True)