#-*- coding:utf-8 -*-

from lib.qyd_app_common import *
import json
import unittest
import requests
from Config import url
from lib.log import logger
from lib.generateTestCases import __generateTestCases
import random

'''
16871725120  --正常用户
借款用户：
16871714765  --轻盈违约
16855328255  --新众盈违约
16816770011  --账户被冻结
16820090055  --当天还款日且还款金额 > 0
16871766820  --可用余额小于预约限额
'''
tel_num_list = ['16871725120', '16871714765', '16855328255', '16816770011', '16820090055', '16871766820']
i = random.randint(0, len(tel_num_list))
# print(i)
tel_num = tel_num_list[i]
print(tel_num)
pwd = 'che001'

'''老产品 + 新产品立即预约接口'''
class zyBuyZYWithAppointment(unittest.TestCase):
    u"""43.02 预约理财-立即预约接口--曾娟"""

    def setUp(self):
        logger.info("***************预约理财-立即预约接口****************")

    def getTest(self, testdata):
        headers = {
                "Content-Type": "application/json",
                "X-Auth-Token": applogin(tel_num, pwd)
                    }
#        print(headers)
        body = {
                "submitToken": getsubmittoken(),
                "productType": testdata['productType'],
                "terminalType": testdata['terminalType']
                }
#        print(body)
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url.zyBuyZYWithAppointment_QA, json=body, headers=headers, verify=False)
        result = r.json()
        print(result)

        if result['successful'] == True:
            self.assertEqual(result['status'], 200)
            logger.info("立即预约成功！")
        else:
            logger.info("立即预约失败：" + result['resultCode']['message'])
            if result['resultCode']['code'] == 'PRODUCTTYPE_IS_ERROR':
                self.assertEqual(result['resultCode']['message'], '产品类型不正确')
            elif result['resultCode']['code'] == 'TOKEN_EXPIRE':
                self.assertEqual(result['resultCode']['message'], 'TOKEN失效')
            elif result['resultCode']['code'] == 'TERMINAL_ERROR':
                self.assertEqual(result['resultCode']['message'], '终端类型不正确')
            elif result['resultCode']['code'] == 'STATUS_ERROR':
                self.assertEqual(result['resultCode']['message'], '状态位不正确')
            elif result['resultCode']['code'] == 'DATA_DUPLICATION':
                self.assertEqual(result['resultCode']['message'], '数据重复')
            elif result['resultCode']['code'] == 'ACCOUNT_SUSPENDED':
                self.assertEqual(result['resultCode']['message'], '抱歉！您的账户被冻结，无法预约购买')
            elif result['resultCode']['code'] == 'ACCOUNT_LOCKED':
                self.assertEqual(result['resultCode']['message'], '抱歉！您的账户已锁定，无法预约购买')
            elif result['resultCode']['code'] == 'ACCOUNT_IS_BORROWER':
                self.assertEqual(result['resultCode']['message'], '抱歉！轻易贷授信用户暂不支持预约购买')
            elif result['resultCode']['code'] == 'AVAILABLE_LESS_LIMIT':
                self.assertIn('开通预约购买，账户余额需大于', result['resultCode']['message'])
            elif result['resultCode']['code'] == '0001':
                self.assertIn('密码错误', result['resultCode']['message'])
            elif result['resultCode']['code'] == '0002':
                self.assertIn('密码锁定', result['resultCode']['message'])



    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)

        return func

    def tearDown(self):
        logger.info("***************预约理财-立即预约接口****************")

"""类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称"""
__generateTestCases(zyBuyZYWithAppointment, "zyBuyZYWithAppointment", "APIdata_Nwproduct.xlsx", "zyBuyZYWithAppointment")

if __name__ == "__main__":
    unittest.main(verbosity=1)
