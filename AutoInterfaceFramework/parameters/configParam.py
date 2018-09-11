from parameters.common_config import CommonConfig

class ConfigParam(CommonConfig):
    def getNameValue(self):
        name = self.cf.get("configParam", "name")
        return name

    def getUserAgentValue(self):
        UserAgent = self.cf.get("configParam", "User-Agent")
        return UserAgent