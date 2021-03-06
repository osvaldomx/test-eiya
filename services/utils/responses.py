"""
Test Eiya!
"""
from flask import jsonify

def response(data):
    return jsonify({
        'success': True,
        'data': data
    }), 200

def bad_request(data=" "):
    return jsonify({
        'success': False,
        'data': data,
        'message': 'Bad Request',
        'code': 400
    }), 400
