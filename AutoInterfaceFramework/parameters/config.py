'''
按照ini的分组命名参数文件，继承common_config类
'''

from parameters.common_config import CommonConfig

class Config(CommonConfig):
    def getNamevaule(self):
        return self.cf.get("config", "name")

    def getUserAgentvaule(self):
        return self.cf.get("config", "User-Agent")