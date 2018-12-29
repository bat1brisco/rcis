from flask import *

from api.routes.routes import user


app = Flask(__name__)

app.register_blueprint(api.routes.routes.user)

if (__name__ == "__main__"):
    app.debug = True