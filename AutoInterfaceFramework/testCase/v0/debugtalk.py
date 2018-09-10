from parameters.config import Config
from parameters.test import Test
import os

version = os.path.dirname(__file__).split("/")[-1]
print("version=====", version)

configParams = Config(version)
testParams = Test(version)

def get_nameValue():
    return configParams.getNamevaule()

def get_userAgentValue():
    return configParams.getUserAgentvaule()

def get_testNameValue():
    return  testParams.getNamevaule()

def get_testAValue():
    return testParams.getAValue()

def get_testBValue():
    return testParams.getBValue()

def get_testUrlValue():
    return testParams.getUrlValue()

def get_testMethodValue():
    return testParams.getMethodValue()