'''
按照ini的分组命名参数文件，继承common_config类
'''

from parameters.common_config import CommonConfig

class Section(CommonConfig):
    def key(self):
        return self.cf.get("TestSuitName", "key")