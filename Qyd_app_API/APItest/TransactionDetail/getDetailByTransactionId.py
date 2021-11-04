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


class getDetailByTransactionId(unittest.TestCase):
    u"""49【查询】轻盈交易明细app接口--曾娟"""

    def setUp(self):
        logger.info("***************【查询】轻盈交易明细app接口开始****************")

    def getTest(self,testdata):getdetailbytransactionid_overdue.py
        headers = {
                "Content-Type": "application/json",
                # "X-Auth-Token": applogin(testdata['tel_num'], 'che001')
                    }
#        print(headers)
        body = {
                "transactionId": testdata['transactionId']
                # "pageNumber": testdata['pageNumber'],
                # "pageSize": testdata['pageSize']
                }
        print(body)
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url.getDetailByTransactionId_QA, headers=headers, json=body, verify=False)
        result = r.json()
        '''json格式化输出-json.dumps，便于调试及后续定位异常，json.dumps()用于将dict类型的数据转成str，
        因为如果直接将dict类型的数据写入json文件中会发生报错，因此在将数据写入时需要用到该函数。 '''
        result_dump = json.dumps(result, indent=4, ensure_ascii=False, separators=(',', ':'))
        logger.info(testdata['describe'] + "接口返回信息：")
        logger.info(result_dump)

        if testdata['type'] == '购买':
            if result['code'] == 60018:
                self.assertEqual(result['msg'], "交易记录不存在！")
            if result['code'] == 10000:
                # 投资查询成功共计
                sql_tz_success = 'SELECT (sum(actual_amount) + sum(reward_amount))/10000 as tz_success from mt_possession_order where transaction_id = "' + \
                                 testdata['transactionId'] + '"' + ' and `status` = 1;'
                print('sql_tz_success:', sql_tz_success)
                tz_success = mysqldb('qydproduction').selectsql(sql_tz_success)[0]['tz_success']
                print(tz_success)
                # 投资查询失败共计
                sql_tz_fail = 'SELECT sum(actual_amount)/10000 as tz_fail from mt_possession_order where transaction_id = "' + \
                              testdata['transactionId'] + '"' + ' and `status` = 3;'
                print('sql_tz_fail:', sql_tz_fail)
                tz_fail = mysqldb('qydproduction').selectsql(sql_tz_fail)[0]['tz_fail']
                print(tz_fail)
                self.assertEqual(float(tz_success), float(result['data']['tansactionGather']['successAmount']))
                self.assertEqual(float(tz_fail), float(result['data']['tansactionGather']['failAmount']))
            else:
                logger.error(result['msg'])
        if testdata['type'] == '转让':
            if result['code'] == 10000:
                sql_userid = 'SELECT id from `user` where tel_num = "' + testdata['tel_num'] + '"'
                print(sql_userid)
                user_id = mysqldb('qydproduction').selectsql(sql_userid)[0]['id']
                print('user_id: ', user_id)
                sql_bj_bxgj = 'SELECT amount,actual_amount from mt_possession_order where loan_id =(SELECT loan_id from mt_assignment where transaction_id = "' \
                           + testdata['transactionId'] + '") and seller_id = "' + user_id + '" and `status` = 1;'
                print(sql_bj_bxgj)
                bj = mysqldb('qydproduction').selectsql(sql_bj_bxgj)[0]['amount']/10000
                print('本金：', bj)
                bxgj = mysqldb('qydproduction').selectsql(sql_bj_bxgj)[0]['actual_amount']/10000
                print('本息共计：', bxgj)
                self.assertEqual(float(bj), float(result['data']['tansactionGather']['sellPricipal']))
                self.assertEqual(float(bxgj), float(result['data']['tansactionGather']['successAmount']))
            else:
                logger.error(result['msg'])
        if testdata['type'] == '到期还款':
            if result['code'] == 10000:
                # 到期还款
                sql_bj = 'SELECT amount from mt_loan where id = (SELECT order_no from `transaction` where id = "' + \
                         testdata['transactionId'] + '");'
                print(sql_bj)
                bj = mysqldb('qydproduction').selectsql(sql_bj)[0]['amount']/10000
                print('本金：', bj)
                sql_bxgj = 'SELECT amount from mt_loan_split where loan_id = (SELECT order_no from `transaction` where id = "' + \
                           testdata['transactionId'] + '");'
                print(sql_bxgj)
                bxgj = mysqldb('qydproduction').selectsql(sql_bxgj)[0]['amount']/10000
                print('本息共计：', bxgj)
                self.assertEqual(float(bj), float(result['data']['tansactionGather']['sellPricipal']))
                self.assertEqual(float(bxgj), float(result['data']['tansactionGather']['successAmount']))
            else:
                logger.error(result['msg'])
        if testdata['type'] == '违约还款':
            if result['code'] == 10000:
                #违约后被创金兜底
                sql_bj_sy = 'SELECT principal,interest from mt_loan_billing where loan_id = (SELECT loan_id from mt_assignment where transaction_id = "' + testdata['transactionId'] + '");'
                print(sql_bj_sy)
                bj = mysqldb('qydproduction').selectsql(sql_bj_sy)[0]['principal']/10000
                print('本金：', bj)
                sy = mysqldb('qydproduction').selectsql(sql_bj_sy)[0]['interest']/10000
                print('收益：', sy)
                self.assertEqual(float(bj), float(result['data']['tansactionGather']['sellPricipal']))
                self.assertEqual(float(sy), float(result['data']['tansactionGather']['totalInterest']))
            else:
                logger.error(result['msg'])

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)

        return func

    def tearDown(self):
        logger.info("***************【查询】轻盈交易明细app接口结束****************")

"""类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称"""
__generateTestCases(getDetailByTransactionId, "getDetailByTransactionId", "APIdata_Nwproduct.xlsx", "getDetailByTransactionId")

if __name__ == "__main__":
    unittest.main(verbosity=1)

