#coding:utf-8

from app.blackword import blackword
from flask import request,jsonify
from flask_restful import reqparse
from ..db.dao import DB

init_data = {
    "err_code": 0,
    "err_msg": "success",
    "data": {}
}

@blackword.route('', methods=['GET','POST','DELETE'])
def blackword_test():
    if request.method == 'GET':
        parser=reqparse.RequestParser()
        parser.add_argument("keyword", type=str, required=False, help="可选参数")
        tmpdata = {}
        if request.args is None or request.args.get("keyword") is None or request.args.get("keyword") == "":
            db = DB
            db = DB.connetcdb(db)
            tmpdata["blacklist_words"] = DB.querydb(db)
            init_data["data"] = tmpdata
            return jsonify(str(init_data))
        else:
            return jsonify(status='failed', msg='rank not found')
    if request.method == 'POST':
        return jsonify(status='failed', msg='rank not found')
    if request.method == 'DELETE':
        return jsonify(status='failed', msg='rank not found')