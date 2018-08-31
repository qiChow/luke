from flask import jsonify
from code import Code


def make_result(reference=None, code=Code.SUCCESS_CODE):
    return jsonify({"error_code": code, "error_message": Code.msg[code], "reference": reference})
