from flask import jsonify 

def success_response(message,data=None):
    return jsonify({
        "status":200,
        "error":False,
        "message":message,
        "data":data

    }),200

def error_response(status_code,data=None):
    return jsonify({
        "status":status_code,

    })


