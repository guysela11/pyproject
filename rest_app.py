import requests as requests
from flask import Flask, request
import db_connector

app = Flask(__name__)

@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user (user_id):
    if request.method == 'POST':
        request_data = request.json
        user_name = request_data.get('user_name')
        db_connector.add_user(user_id, user_name)
        return {'status': 'ok', 'user_added': user_name}, 200 # status code

    elif request.method == 'GET':
        return {'status': 'ok', 'user_name': db_connector.get_user(user_id)}, 200 # status code

    elif request.method == 'PUT':
        request_data = request.json
        user_name = request_data.get('user_name')
        db_connector.update_user(user_id, user_name)
        return {'status': 'ok', 'user_updated': user_name}, 200  # status code

    elif request.method == 'DELETE':
        db_connector.del_user(user_id)
        return {'status': 'ok', 'user_deleted': user_id}

app.run(host='127.0.0.1', debug=True, port=5000)