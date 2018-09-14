# coding:utf-8

'''
创建蓝图
'''

from flask import Blueprint

blackword = Blueprint('blackword', __name__)

from app.blackword import views