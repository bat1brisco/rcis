from flask import Flask

app = Flask(__name__)

from rcis.api.routes.routes import user

app.register_blueprint(api.routes.routes.user)