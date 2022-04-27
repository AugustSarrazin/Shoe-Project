from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
from flask_app.models import comment
from flask_app.models import shoe

class Like:
    db_name = 'fassion_shoes'
    def __init__(self,db_data):
        self.id = db_data['id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.shoe_id = db_data['shoe_id']
        self.user_id = db_data['user_id']
        self.nick_name = db_data['nick_name']
        self.likes = []
        
        
        
    @classmethod
    def save(cls,data):
        query = 'INSERT INTO likes (shoe_id,user_id) VALUES (%(shoe_id)s, %(user_id)s);'
        return connectToMySQL(cls.db_name).query_db(query,data)
