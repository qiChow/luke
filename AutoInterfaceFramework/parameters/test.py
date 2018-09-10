'''
按照ini的分组命名参数文件，继承common_config类
'''

from parameters.common_config import CommonConfig

class Test(CommonConfig):

    def getNamevaule(self):
        return self.cf.get("test", "name")

    def getAValue(self):
        return self.cf.get("test", "a")

    def getBValue(self):
        return self.cf.get("test", "b")

    def getUrlValue(self):
        return self.cf.get("test", "url")

    def getMethodValue(self):
        return self.cf.get("test", "method")