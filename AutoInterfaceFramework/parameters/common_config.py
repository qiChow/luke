"""
读取配置文件的方法

"""

import configparser
import os

class CommonConfig:
    def __init__(self, version):
        """
        读取配置文件
        """
        #实例化configParser对象
        self.cf = configparser.ConfigParser()

        #获取当前文件夹的父目录绝对路径
        self.path = os.path.dirname(os.path.dirname(__file__))

        #获取config文件下各版本中的ini文件，如需读取test_data.ini文件
        self.file_path = os.path.join(self.path, 'config/${version}', 'test_data.ini')

        #读取ini文件
        self.cf.read(self.file_path, encoding="utf-8")