#coding:utf-8

from app.rank import rank
from flask import jsonify

rank_data = [
    [{"event_id": 1},
    {
        "err_code":0,
        "err_msg":"",
        "payload":{
            "rank": [
                {"order": 1, "user_name":"zhangsan", "coins": 1223 },
                {"order": 2, "user_name": "lisi", "coins": 1223}
            ]
        }
    }]
]
@rank.route('/<int:event_id>', methods=['GET','POST'])
def get(event_id):
    i = 0
    rank_data_row_0 = [x[0] for x in rank_data]
    for rank_key in rank_data_row_0:
        i +=1
        if int(rank_key['event_id']) == event_id:
            return jsonify(rank_data[i-1][1])
    return jsonify(status='failed', msg='rank not found')