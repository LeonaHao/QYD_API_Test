#-*- coding:utf-8 -*-

from lib.qyd_app_common import *
import json
import unittest
import requests
from Config import url
from lib.log import logger
from lib.generateTestCases import __generateTestCases

class GetAppreciationAmount(unittest.TestCase):
    u"""40.5【查询】新月盈、新众盈-预期收益--曾娟"""

    def setUp(self):
        logger.info("***************查询 新月盈、新众盈 预期收益开始****************")

    def getTest(self, testdata):
        headers = {
                "Content-Type": "application/json",
                "X-Auth-Token": applogin()
                    }
#        print(headers)
        body = {
                "productType": testdata['productType']
                }
#        print(body)
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url.getAppreciationAmount_QA,json= body,headers=headers,verify=False)
        result = r.json()
        print(result)

        if result['code'] == 10000:
            logger.info("查询" + testdata['productType'] + '预期收益: ' + "成功!")
        else:
            logger.error("查询" + testdata['productType'] + "预期收益失败:\n " + result['msg'])

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func

    def tearDown(self):
        logger.info("***************查询 新月盈、新众盈 预期收益结束****************")

"""类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称"""
__generateTestCases(GetAppreciationAmount, "getAppreciationAmount", "APIdata_3.6.3.xlsx", "getAppreciationAmount")

if __name__ == "__main__":
    unittest.main(verbosity=1)


