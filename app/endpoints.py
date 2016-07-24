# -*- encoding: utf-8 -*-
from flask import Flask, jsonify, request
from app import app

feed = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/api/feed', methods=['GET'])
def get_feed():
    return jsonify({'feed': feed})


@app.route('/api/feed', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)

    q = {
        'id': feed[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    feed.append(q)
    return jsonify({'feed': feed}), 201