from flask import Flask, jsonify
from flask_restful import Api
from .database import init_db
from .APIs.user import UserListAPI, UserAPI

def create_app():
    app = Flask(__name__)
    app.config.from_object("src.config.Config")
    
    init_db(app)
    
    api = Api(app)
    api.add_resource(UserListAPI, "/users")
    api.add_resource(UserAPI, "/users/<id>")
    
    return app

app = create_app()