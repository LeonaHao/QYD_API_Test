#-*- coding:utf-8 -*-

from lib.qyd_app_common import *
import json
import unittest
import requests
from Config import url
from lib.log import logger
from lib.generateTestCases import __generateTestCases

class RemainAmount(unittest.TestCase):
    u"""【40.4查询】新月盈、新众盈、新月盈优选产品详情--曾娟"""

    def setUp(self):
        logger.info("***************查询新产品详情开始****************")

    def getTest(self, testdata):
        headers = {
                "Content-Type": "application/json"
#                "X-Auth-Token": applogin()
                    }
#        print(headers)
        body = {
                "productType": testdata['productType']
                }
#        print(body)
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url.remainamount_QA,json= body,headers=headers,verify=False)
        result = r.json()
        print(result)

        if result['code'] == 10000:
            self.assertEqual(str(result['successful']), str(True))
            logger.info("查询" + testdata['productType'] + '产品详情: ' + "成功!")
        else:
            logger.error("查询" + testdata['productType'] + "产品详情失败:\n " + result['msg'])

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)

        return func

    def tearDown(self):
        logger.info("***************查询新产品详情结束****************")

"""类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称"""
__generateTestCases(RemainAmount, "remainamount", "APIdata_Nwproduct.xlsx", "remainamount")

if __name__ == "__main__":
    unittest.main(verbosity=1)


