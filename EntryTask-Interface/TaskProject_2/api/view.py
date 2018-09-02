from flask_restful import Resource, reqparse, request

from util import make_result

from code import Code

class Test(Resource):
    def __init__(self):
        self.parse = reqparse.RequestParser()
        self.parse.add_argument('a', type=int, required=True,help="不能为空，且为int型")
        self.parse.add_argument('b', type=str, required=True,help="不能为空,且为string型")
    def get(self):
        req = self.parse.parse_args()
        a = req.get("a")
        b = req.get("b")
        info = request.values.to_dict()
        key = list(info.keys())
        if len(key) <= 2:
            return make_result(reference={'a':a,'b':b})
        return make_result(reference=str(info), code=Code.SYSTEM_ERRCODE)
