from flask import Flask
from App.home.views import home as home_blueprint
from App.admin.views import admin as admin_blueprint
from App.views import blue


def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint=home_blueprint,url_prefix='/home/')
    app.register_blueprint(blueprint=admin_blueprint,url_prefix='/admin/')
    app.register_blueprint(blueprint=blue,url_prefix='/test/')
    return app
