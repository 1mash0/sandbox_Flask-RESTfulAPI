from datetime import datetime
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from sqlalchemy_utils.types import UUIDType
from ..database import db

import uuid

ma = Marshmallow()

class UserModel(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(255), nullable=False)
    
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    
    def __init__(self, name, state):
        self.name = name
        self.state = state
        
    def __repr__(self):
        return "UserModel {}:{}".format(self.id, self.name)
    
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        
    created_at = fields.DateTime("%Y-%m-%dT%H:%M:%S")
    updated_at = fields.DateTime('%Y-%m-%dT%H:%M:%S')