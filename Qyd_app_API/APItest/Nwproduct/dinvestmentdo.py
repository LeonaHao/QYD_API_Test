#-*- coding:utf-8 -*-

from lib.qyd_app_common import *
import json
import unittest
import requests
from Config import url
from lib.log import logger
from lib.generateTestCases import __generateTestCases

class DinvestmentDo(unittest.TestCase):
    u"""40.12 新月盈、新众盈撤资确认接口--曾娟"""

    def setUp(self):
        logger.info("***************新月盈、新众盈撤资确认接口开始****************")

    def getTest(self,testdata):
        headers = {
                "Content-Type": "application/json",
                "X-Auth-Token": applogin("16871725120","che001")
                    }
        print(headers)
        body = {
                "submitToken": getsubmittoken(),
                "amount": testdata['amount'],
                "terminal": testdata['terminal'],
                "productType": testdata['productType']
                }
        print(body)
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url.dinvestmentdo_QA, headers=headers, json=body, verify=False)
        result = r.json()
        print(testdata['name'], "撤资确认接口信息：\n",result)

        if result['code'] == 10000:
            logger.info(testdata['productType'] + "撤资确认接口成功！")
            self.assertEqual(str(result['successful']), str(True))
        elif result['code'] == 50045:
            logger.info(testdata['productType'] + result['msg'])
            self.assertEqual(str(result['msg']), "账户持有本金不足")
        else:
            logger.info(testdata['productType'] + "撤资确认接口失败！")
            self.assertEqual(str(result['msg']), "失败")


    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)

        return func

    def tearDown(self):
        logger.info("***************新月盈、新众盈撤资确认接口结束****************")

"""类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称"""
__generateTestCases(DinvestmentDo, "DinvestmentDo", "APIdata_Nwproduct.xlsx", "DinvestmentDo")

if __name__ == "__main__":
    unittest.main(verbosity=1)

