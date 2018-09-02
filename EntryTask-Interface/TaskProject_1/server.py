from flask import Flask
from flask import request
from flask import jsonify
server = Flask(__name__)

@server.errorhandler(404)
def page_not_found(error):
        result = {"error_code": 11,
                "error_message": "system error",
                "reference": "The request path is not /shopee/test"
                }
        return jsonify(result)

@server.route('/shopee/test', methods=['GET', 'POST', 'PUT', 'DELETE'])
def test():
    if request.method != 'GET':
        result={"error_code": 11,
                "error_message": "system error",
                "reference": "The request method is not GET!"
               }
        return jsonify(result)
    if request.method == 'GET':
        a = request.values.get('a')
        b = request.values.get('b')
        key = request.values
        info = key.to_dict()
        if len(key) > 2:
            result = {"error_code": 21, "error_message": "empty or wrong params",
                          "reference": "the params number is more than 2!"}
            return jsonify(result)
        if a and b:
            try:
                a = int(a)
            except ValueError:
                result = {"error_code": 21, "error_message": "empty or wrong params",
                          "reference": "the a params type is wrong"}
                return jsonify(result)
            if isinstance(a,int) and isinstance(b,str):
                result={"error_code":0,"error_message":"success","reference":str(info)}
                return jsonify(result)
            else:
                result={"error_code":11,"error_message":"system error","reference":"the a and b params is ok,maybe something wrong in your server"}
                return jsonify(result)
        else:
            if not a:
                result={"error_code":21,"error_message":"empty or wrong params","reference":"the a param is empty"}
                return jsonify(result)
            else:
                result = {"error_code": 21, "error_message": "empty or wrong params",
                          "reference": "the b param is empty"}
                return jsonify(result)

if __name__ == '__main':
    server.run()