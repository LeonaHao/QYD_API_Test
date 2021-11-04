# -*- coding:utf-8 -*
"""
 @author 190319L
 date 2018/7/19 16:29
 @Project&file: Qyd_app_API_Zengjuan getZyBackMoneyPlan.py
"""
from lib.qyd_app_common import *
import json
import unittest
import requests
from Config import url
from lib.log import logger
from lib.generateTestCases import __generateTestCases

class getZyBackMoneyPlan(unittest.TestCase):
    u'40.14 获取众盈所有回款计划列表 --- 戴文瀚'
    def setUp(self):
        logger.info('************** [获取众盈所有回款计划列表]接口 开始执行 **************')

    def getTest(self, testdata):
        print("入参为： ")
        print(testdata)
        headers = {
            "Content-Type":"application/json",
            "X-Auth-Token":applogin()
        }
        data = {
                "page":testdata['page'],
                "pageSize":testdata['pageSize']
                }
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url=url.getZyBackMoneyPlan_QA, json=data, headers=headers, verify=False)
        result = r.json()
        print(result)

        if result["code"] == 10000 and result['successful'] == True:
            self.assertEqual(result['code'], 10000)
            self.assertEqual(result['msg'], u'成功')
            logger.info("获取众盈升级版回款计划：执行成功！")
        else:
            logger.info("获取众盈升级版回款计划：执行失败！\n" + result['msg'])
        '''待移动服务检查确认为何page和pagesize两个参数可以为空'''
        # elif result["code"] == 400 and result['successful'] == False:
        #     self.assertEqual(result)['code'], 50002)
    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func

    def tearDown(self):
        logger.info("************** [获取众盈升级版回款计划]接口 执行完毕 ************** ")


"""类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称"""
__generateTestCases(getZyBackMoneyPlan, "getZyBackMoneyPlan", "APIdata_3.6.3.xlsx", "getZyBackMoneyPlan")

if __name__ == "__main__":
    unittest.main(verbosity=1)