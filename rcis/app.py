from flask import *
from rcis.api.routes.routes import user

app = Flask(__name__)

app.register_blueprint(user)

if (__name__ == "__main__"):
    app.debug = True