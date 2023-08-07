from flask_restful import Resource, reqparse, abort
from flask import jsonify
from ..Models.user import UserModel, UserSchema
from ..database import db

class UserListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(UserListAPI, self).__init__()
        
    def get(self):
        results = UserModel.query.all()
        jsonData = UserSchema(many=True).dump(results)
        # return jsonify({"results": jsonData})
        return jsonData
    
class UserAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("id")
        self.reqparse.add_argument("name")
        self.reqparse.add_argument("state")
        super(UserAPI, self).__init__()
        
    def get(self, id):
        user = db.session.query(UserModel).filter_by(id=id).first()
        
        if user is None:
            abort(404)
            
        res = UserSchema().dump(user)
        return res