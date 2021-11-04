#-*- coding:utf-8 -*-

from lib.qyd_app_common import *
import json
import unittest
import requests
from Config import url
from lib.log import logger
from lib.generateTestCases import __generateTestCases
from lib import regex

class NwProtocolContractModel(unittest.TestCase):
    u"""40.8 【合同范本展示】《债权转让协议》《借款协议》《复投服务协议》接口--曾娟"""

    def setUp(self):
        logger.info("***************查询协议接口开始****************")

    def getTest(self, testdata):
        headers = {
                "Content-Type": "application/json"
                    }
#        print(headers)
        body = {
                "type": testdata['type']
                }
#        print(body)
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url.nwprotocolcontractmodel_QA,json= body,headers=headers,verify=False)
        result = r.json()
#        print(result['mapData']['content'])

        if result['status'] == 200:
            self.assertEqual(str(result['successful']),str(True))
            regex_result = regex.regex(testdata['key'], result['mapData']['content'])
#            print(regex_result)
            self.assertEqual(regex_result,1)



    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)

        return func

    def tearDown(self):
        logger.info("***************查询协议接口结束****************")

"""类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称"""
__generateTestCases(NwProtocolContractModel, "NwProtocolContractModel", "APIdata_Nwproduct.xlsx", "NwProtocolContractModel")

if __name__ == "__main__":
    unittest.main(verbosity=1)


