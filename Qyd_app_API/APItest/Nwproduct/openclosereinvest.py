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


class OpenCloseReinvest(unittest.TestCase):
    u"""40.13 开启 关闭复投接口--曾娟"""

    def setUp(self):
        logger.info("***************开启 关闭复投接口开始****************")

    def getTest(self,testdata):
        headers = {
                "Content-Type": "application/json",
                "X-Auth-Token": applogin()
                    }
#        print(headers)
        body = {
                "productType": "XYY",
                "operateType": testdata['operateType'],
                "submitToken": getsubmittoken(),
                "type": testdata['type']

                }
#        print(body)
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url.openclosereinvest_QA,json= body,headers=headers, verify=False)
        result = r.json()
#        print(testdata['name'] + testdata['describe'], "接口信息：\n", result)

        sql_userid = 'SELECT id from `user` where tel_num = "' + str(config.tel_num) + '"'
#        print(sql_userid)
        user_id = mysqldb('qydproduction').selectsql(sql_userid)[0]['id']
#        print('user_id: ', user_id)
        #查询数据库中复投状态及复投类型
        sql_reinvestment = 'SELECT `status`,`type` from mt_reinvestment where user_id = "' + str(user_id) + '"'
#        print(sql_reinvestment)
        sql_result = mysqldb("qydnewproduction").selectsql(sql_reinvestment)[0]
#        print("sql_result: ", sql_result)

        if result['code'] == 10000:
            self.assertEqual(str(result['successful']), str(True))
            self.assertEqual(testdata['operateType'], sql_result['status'].upper())
            self.assertEqual(testdata['type'], str(sql_result['type']))

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)

        return func

    def tearDown(self):
        logger.info("***************开启 关闭复投接口结束****************")

"""类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称"""
__generateTestCases(OpenCloseReinvest, "OpenCloseReinvest", "APIdata_Nwproduct.xlsx", "OpenCloseReinvest")

if __name__ == "__main__":
    unittest.main(verbosity=1)

