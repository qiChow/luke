# coding:utf-8

'''
创建蓝图
'''

from flask import Blueprint

rank = Blueprint('rank', __name__)

from app.rank import views