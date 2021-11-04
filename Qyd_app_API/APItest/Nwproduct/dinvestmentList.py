# -*- coding:utf-8 -*
"""
 @author 190319L
 date 2018/8/20 11:17
 @Project&file: Qyd_app_API dinvestmentList.py
"""
from lib.qyd_app_common import *
import json
import unittest
import requests
from Config import url
from lib.log import logger
from lib.generateTestCases import __generateTestCases

class dinvestmentList(unittest.TestCase):
    u'40.19 二级市场债权明细(撤资匹配接口) --- 戴文瀚'
    def setUp(self):
        logger.info('************** [二级市场债权明细(撤资匹配接口)]接口开始执行 **************')

    def getTest(self, testdata):
        print("入参为： ")
        print(testdata)
        headers = {
            "Content-Type":"application/json",
            "X-Auth-Token":applogin(config.username_dwh,config.passwd_dwh)
        }
        data = {
                "amount":testdata['amount'],
                "terminal":testdata['terminal'],
                "productType":testdata['productType']
                }
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url=url.dinvestmentList_QA, json=data, headers=headers, verify=False)
        result = r.json()
        # print(result)
        ''' json格式化输出-json.dumps，便于调试及后续定位异常 '''
        result_dump = json.dumps(result, sort_keys=True, indent=4, separators=(',', ':'))
        # logger.info(result_dump)

        if result["status"] == 200 and result['successful'] == True:
            self.assertEqual(result['code'], 10000)
            self.assertEqual(result['msg'], u'成功')
            logger.info("二级市场债权明细(撤资匹配接口)：执行成功！\n" + str(result_dump))
        elif result["status"] == 200 and result['successful'] == False and result['code'] == 50045:
            self.assertEqual(result['msg'], u'账户持有本金不足')
            logger.info("二级市场债权明细(撤资匹配接口)：账户持有本金不足！\n" + "错误原因：" + result['msg'])
        elif result["status"] == 200 and result['successful'] == False and result['code'] == 99999:
            self.assertEqual(result['msg'], u'其他错误')
            logger.info("二级市场债权明细(撤资匹配接口)：参数异常符合预期！\n" + "错误原因：" + result['msg'])
        elif result["status"] == 400 and result['successful'] == False and result['code'] == 50003:
            self.assertIn(u'入参不可为空',result['msg'])
            logger.info("二级市场债权明细(撤资匹配接口)：参数异常符合预期！\n" + "错误原因：" + result['msg'])
        else:
            logger.info("二级市场债权明细(撤资匹配接口)：执行失败！\n" + '其他未知错误' + str(result_dump))

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func

    def tearDown(self):
        logger.info("************** [二级市场债权明细(撤资匹配接口)]接口执行完毕 ************** ")


"""类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称"""
__generateTestCases(dinvestmentList, "dinvestmentList", "APIdata_3.6.3.xlsx", "dinvestmentList")

if __name__ == "__main__":
    unittest.main(verbosity=1)