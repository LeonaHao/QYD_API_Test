#-*- coding:utf-8 -*-

from lib.qyd_app_common import *
import json
import unittest
import requests
from Config import url
from lib.log import logger
from lib import mysqldb
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
# print(tel_num)
pwd = 'che001'

class OpenCloseWithAppointment(unittest.TestCase):
    u"""40.3/43.02 开启和关闭预约理财接口【兼容之前的理财产品】--曾娟"""

    def setUp(self):
        logger.info("***************开启和关闭预约理财接口开始****************")

    def getTest(self, testdata):

        headers = {
                "Content-Type": "application/json",
                "X-Auth-Token": applogin(tel_num, pwd)
                    }
#        print(headers)
        body = {
                "submitToken": getsubmittoken(),
                "productType": testdata['productType'],
                "terminalType": testdata['terminalType'],
                "isOpen": testdata['isOpen']
                }
        print(body)
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url.openclosewithappointment_QA,json= body,headers=headers,verify=False)
        result = r.json()
        print(result)

        if result['code'] == 10000:
            self.assertEqual(str(result['successful']), str(True))
            if testdata['isOpen'] == "0":
                logger.info( "开启预约" + testdata['productType'] + ': ' + "成功!")
            elif testdata['isOpen'] == "1":
                logger.info("手动关闭预约" + testdata['productType'] + ': ' + "成功!")
            else:
                logger.info("系统取消预约" + testdata['productType'] + ': ' + "成功!")
        elif result['code'] == 0 and result['status'] == 550:
            self.assertEqual(result['successful'], False)
            # logger.info(result['msg'])
        elif result['code'] == 50054:
            self.assertEqual(result['msg'], 'TOKEN失效')
            logger.info(result['msg'])
        elif result['code'] == 50055:
            self.assertEqual(result['msg'], '终端类型不正确')
            logger.info(result['msg'])
        elif result['code'] == 50011:
            self.assertEqual(result['msg'], '状态位不正确')
            logger.info(result['msg'])
        elif result['code'] == 50057:
            self.assertEqual(result['msg'], '数据重复')
            logger.info(result['msg'])
        elif result['code'] == 50058:
            self.assertEqual(result['msg'], '抱歉！您的账户被冻结，无法预约购买')
            logger.info(result['msg'])
        elif result['code'] == 50059:
            self.assertEqual(result['msg'], '抱歉！您的账户已锁定，无法预约购买')
            logger.info(result['msg'])
        elif result['code'] == 50060:
            self.assertEqual(result['msg'], '抱歉！轻易贷授信用户暂不支持预约购买')
            logger.info(result['msg'])
        elif result['code'] == 50061:
            self.assertIn('开通预约购买，账户余额需大于', result['msg'])
            logger.info(result['msg'])
        elif result['code'] == 50068:
            self.assertEqual(result['msg'], '您存在违约中借款，暂不能开启预约购买！')
            logger.info(result['msg'])
        elif result['code'] == 50069:
            self.assertEqual(result['msg'], '您今天有借款需要还款，暂不能开启预约购买！')
            logger.info(result['msg'])
        else:
            logger.error(testdata['isOpen'] + "预约" + testdata['productType'] + "失败:\n " + result['msg'])

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)

        return func

    def tearDown(self):
        logger.info("***************开启和关闭预约理财接口结束****************")

"""类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称"""
__generateTestCases(OpenCloseWithAppointment, "openclosewithappointment", "APIdata_Nwproduct.xlsx", "openclosewithappointment")

if __name__ == "__main__":
    unittest.main(verbosity=1)


