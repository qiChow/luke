import sys
sys.path.append("..")
from parameters.configParam import ConfigParam
from parameters.test import Test
import os

version = os.path.dirname(__file__).split("_")[-1]

def get_nameValue():
    configParams = ConfigParam(version)
    return configParams.getNameValue()

def get_userAgentValue():
    configParams = ConfigParam(version)
    return configParams.getUserAgentValue()

def get_testAValue():
    testParams = Test(version)
    return testParams.getAValue()

def get_testBValue():
    testParams = Test(version)
    return testParams.getBValue()

def get_testUrlValue():
    testParams = Test(version)
    return testParams.getUrlValue()

def get_testMethodValue():
    testParams = Test(version)
    return testParams.getMethodValue()