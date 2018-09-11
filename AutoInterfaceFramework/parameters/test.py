from parameters.common_config import CommonConfig

class Test(CommonConfig):

    def getAValue(self):
        return self.cf.get("test", "a")

    def getBValue(self):
        return self.cf.get("test", "b")

    def getUrlValue(self):
        return self.cf.get("test", "url")

    def getMethodValue(self):
        return self.cf.get("test", "method")