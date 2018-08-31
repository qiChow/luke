from flask import Flask, abort, jsonify
import flask_restful
from util import make_result
from code import Code
from api import api

app = Flask(__name__)
app.register_blueprint(api)

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"error_code": 11, "error_message": "system error", "reference": "null"})


def custom_abord(http_status_code, *args, **kwargs):
    # 只要http_status_code 为400， 报参数错误
    if http_status_code == 400:
        return abort(make_result(code=Code.PARAMS_ERRCODE))
    return abort(make_result(code=Code.SYSTEM_ERRCODE))

# 把flask_restful中的abort方法改为我们自己定义的方法
flask_restful.abort = custom_abord


if __name__ == "__main__":
    app.run(debug=True)
