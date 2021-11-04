#-*- coding:utf-8 -*-

from lib.qyd_app_common import *
import json
import unittest
import requests
from Config import url
from lib.log import logger
from lib.generateTestCases import __generateTestCases

class InvestInhand(unittest.TestCase):
    u"""41.1【查询】新手标、新月盈、新众盈投资处理中金额接口--曾娟"""

    def setUp(self):
        logger.info("***************【查询】新手标、新月盈、新众盈投资处理中金额接口开始****************")

    def getTest(self,testdata):
        headers = {
                "Content-Type": "application/json",
                "X-Auth-Token": applogin()
                    }
        print(headers)
        body = {
                "productType": testdata['productType']
                }
        print(body)
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url.investinhand_QA, headers=headers, json=body, verify=False)
        result = r.json()
        print(testdata['describe'] + "投资处理中金额接口信息：\n", result)

        if result['code'] == 10000:
            self.assertEqual(str(result['successful']), str(True))


    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)

        return func

    def tearDown(self):
        logger.info("***************【查询】新手标、新月盈、新众盈投资处理中金额接口结束****************")

"""类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称"""
__generateTestCases(InvestInhand, "InvestInhand", "APIdata_Nwproduct.xlsx", "InvestInhand")

if __name__ == "__main__":
    unittest.main(verbosity=1)

