#-*- coding:utf-8 -*-

from lib.qyd_app_common import *
import json
import unittest
import requests
from Config import url
from lib.log import logger
from Config import config
from lib.mysqldb import mysqldb
from lib.generateTestCases import __generateTestCases


class getDetailByTransactionIdOd(unittest.TestCase):
    u"""新月盈、新众盈、新手标违约后被创金兜底交易明细接口--曾娟"""

    def setUp(self):
        logger.info("***************新月盈、新众盈、新手标违约后被创金兜底交易明细接口开始****************")

    def getTest(self,testdata):
        headers = {
                "Content-Type": "application/json",
                "X-Auth-Token": applogin(testdata['tel_num'], 'che001')
                    }
#        print(headers)
        body = {
                "transactionId": testdata['transactionId']

                }
        print(body)
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url.getdetailbytransactionid_overdue_QA, headers=headers, json=body, verify=False)
        result = r.json()
        '''json格式化输出-json.dumps，便于调试及后续定位异常，json.dumps()用于将dict类型的数据转成str，
        因为如果直接将dict类型的数据写入json文件中会发生报错，因此在将数据写入时需要用到该函数。 '''
        result_dump = json.dumps(result, indent=4, ensure_ascii=False, separators=(',', ':'))
        logger.info(testdata['describe'] + "接口返回信息：")
        logger.info(result_dump)
        if result['code'] == 50062:
            self.assertEqual(testdata['code'], str(result['code']))
            self.assertEqual(testdata['msg'], result['msg'])
        if result['code'] == 10000:
            self.assertEqual(testdata['msg'], result['msg'])
            self.assertEqual(testdata['projectNumber'], result['data']['transactionList'][0]['projectNumber'])
            self.assertEqual(float(testdata['receiveAmount']), float(result['data']['transactionList'][0]['receiveAmount']))
            self.assertEqual(float(testdata['sellPricipal']), float(result['data']['transactionList'][0]['sellPricipal']))
            self.assertEqual(float(testdata['interest']), float(result['data']['transactionList'][0]['interest']))
            self.assertEqual(float(testdata['serviceFee']), float(result['data']['transactionList'][0]['serviceFee']))
        else:
            logger.error(result['msg'])

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)

        return func

    def tearDown(self):
        logger.info("***************新月盈、新众盈、新手标违约后被创金兜底交易明细接口结束****************")

"""类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称"""
__generateTestCases(getDetailByTransactionIdOd, "getDetailByTransactionIdOd", "APIdata_Nwproduct.xlsx", "getDetailByTransactionIdOd")

if __name__ == "__main__":
    unittest.main(verbosity=1)

