#-*- coding:utf-8 -*-

from lib.qyd_app_common import *
import json
import unittest
import requests
from Config import url
from lib.log import logger
from lib.generateTestCases import __generateTestCases

class BuyLoannmt(unittest.TestCase):
    u"""40.1一级市场购买--曾娟"""

    def setUp(self):
        logger.info("***************一级市场购买开始****************")

    def getTest(self, testdata):
        headers = {
                "Content-Type": "application/json",
                "X-Auth-Token": applogin()
                    }
#        print(headers)
        body = {
                "amount": testdata['amount'],
                "terminal": testdata['terminal'],
                "productType": testdata['productType'],
                "submitToken": getsubmittoken()
                }
#        print(body)
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url.buyloannmt_QA,json= body,headers=headers,verify=False)
        result = r.json()
        print(result)

        if result['code'] == 50044:
            logger.info("购买" + testdata['productType'] + ': ' + result['msg'])
            self.assertEqual(result['msg'], "平台剩余可投金额为0!")
        elif result['code'] == 10000:
            logger.info("购买" + testdata['productType'] + ': ' + "成功!")
            self.assertEqual(result['msg'], "成功")
        else:
            logger.info("购买" + testdata['productType'] + '失败: \n' + result['msg'])
            self.assertEqual(str(result['msg']), "失败")
    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)

        return func

    def tearDown(self):
        logger.info("***************一级市场购买结束****************")

"""类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称"""
__generateTestCases(BuyLoannmt, "buyloanmt", "APIdata_Nwproduct.xlsx", "buyloanmt")

if __name__ == "__main__":
    unittest.main(verbosity=1)


