from flask import Flask
from .routes.zillowRoute import zillow_blueprint
app = Flask(__name__)
app.register_blueprint(zillow_blueprint)