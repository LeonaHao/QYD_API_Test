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


class QueryRepayTansactionDetail(unittest.TestCase):
    u"""47.1 正常还款/提前还款交易明细接口--曾娟"""

    def setUp(self):
        logger.info("***************正常还款/提前还款交易明细接口开始****************")

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
        r = requests.post(url.queryrepaytransactiondetail_QA, headers=headers, json=body, verify=False)
        result = r.json()
#        print(result)
        '''json格式化输出-json.dumps，便于调试及后续定位异常，json.dumps()用于将dict类型的数据转成str，
        因为如果直接将dict类型的数据写入json文件中会发生报错，因此在将数据写入时需要用到该函数。 '''
        result_dump = json.dumps(result, indent=4, ensure_ascii=False, separators=(',', ':'))
        logger.info(testdata['describe'] + "接口返回信息：")
        logger.info(result_dump)

        sql_userid = 'SELECT id from `user` where tel_num = "' + str(testdata['tel_num']) + '"'
#        print(sql_userid)
        user_id = mysqldb('qydproduction').selectsql(sql_userid)[0]['id']
#        print('user_id: ', user_id)
        sql_transactiondetail = 'SELECT principal,interest,amount from repay_billing_split where billing_id = (SELECT order_detail_no from repay_transaction ' \
                                'where id = "' + testdata['transactionId'] + '")' + ' and payee_id = "'+ user_id + '";'
#        print('sql_transactiondetail:', sql_transactiondetail)
        transactiondetail = mysqldb('qydnewproduction').selectsql(sql_transactiondetail)
#        print('transactiondetail: ', transactiondetail)
        principal = transactiondetail[0]['principal']
#        print('principal:', principal)
        interest = transactiondetail[0]['interest']
#        print('interest:', interest)
        amount = transactiondetail[0]['amount']
#        print('amount:', amount)

        if result['code'] == 10000:
            logger.info(result['msg'])
            self.assertEqual(float(principal), float(result['data']['transactionList'][0]['principal']))
            self.assertEqual(float(interest), float(result['data']['transactionList'][0]['interest']))
            self.assertEqual(float(amount), float(result['data']['transactionList'][0]['totalAmount']))
        else:
            logger.error(result['msg'])

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)

        return func

    def tearDown(self):
        logger.info("***************正常还款/提前还款交易明细接口结束****************")

"""类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称"""
__generateTestCases(QueryRepayTansactionDetail, "QueryRepayTansactionDetail", "APIdata_Nwproduct.xlsx", "QueryRepayTansactionDetail")

if __name__ == "__main__":
    unittest.main(verbosity=1)

