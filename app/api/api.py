import json
from datetime import datetime
from flask import Flask, request, Response
from app.database.database import Database

def init_app(app: Flask):
    
    @app.route('/')
    def home_route():
        return "Welcome"

    @app.route('/user/<int:user_id>/', methods=['GET', 'POST'])
    def get_user(user_id):
        response = dict()
        try:
            db = Database()
            db_info = db.get_user_by_id(user_id)
            user = {
                "user_id": db_info[0],
                "name": db_info[1],
                "last_name": db_info[2],
                "phones_array": db_info[3],
                "creation_date": db_info[4].strftime('%m/%d/%Y'),
            }
            response = Response(json.dumps(user),  mimetype='application/json')
        except Exception as e:
            print(e)
        return response
    
    @app.route('/user/create/', methods=['POST'])
    def create_user():
        user_json = dict()
        response = dict()
        try:
            db = Database()
            if request.method == 'POST':
                data = request.get_json()
                user_json = dict()
                user_json['name'] = data.get('name')
                user_json['last_name'] = data.get('last_name')
                user_json['phones_array'] = data.get('phones_array')
                user_json['creation_date'] = str(datetime.now().date())
                user_json['id'] = db.create_user(user_json)
                response['user'] = user_json
                response['error'] = ""
                response = Response(json.dumps(response), mimetype='application/json')
                return response
        except Exception as e:
            response['user'] = None
            response['error'] = e
        
        return response
