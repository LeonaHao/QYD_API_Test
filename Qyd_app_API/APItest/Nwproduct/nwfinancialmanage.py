#-*- coding:utf-8 -*-

from lib.qyd_app_common import *
import json
import unittest
import requests
from Config import url
from lib.log import logger
from lib.generateTestCases import __generateTestCases

class NwFinancialManage(unittest.TestCase):
    u"""40.10 新月盈管理、新众盈管理、新手标管理--曾娟"""

    def setUp(self):
        logger.info("***************获取管理页信息开始****************")

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
        r = requests.post(url.nwfinancialmanage_QA,json= body,headers=headers,verify=False)
        result = r.json()
        print("查询", testdata['name'], ":\n ", result)

        if result['code'] == 10000:
            self.assertEqual(str(result['successful']), str(True))


    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)

        return func

    def tearDown(self):
        logger.info("***************获取管理页信息结束****************")

"""类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称"""
__generateTestCases(NwFinancialManage, "NwFinancialManage", "APIdata_Nwproduct.xlsx", "NwFinancialManage")

if __name__ == "__main__":
    unittest.main(verbosity=1)


