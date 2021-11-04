#-*- coding:utf-8 -*-

from lib.qyd_app_common import *
import json
import unittest
import requests
from Config import url
from lib.log import logger
from lib.generateTestCases import __generateTestCases

class NwCalculatorInfoShow(unittest.TestCase):
    u'40.6 新月盈、新众盈计算器信息展示接口--曾娟'
    def setUp(self):
        logger.info('************** 新月盈、新众盈计算器信息展示接口开始执行 **************')

    def getTest(self, testdata):
#        print("入参为：" ,testdata)
        headers = {"Content-Type": "application/json"}
        data = {
                "productType":testdata['productType']
                }
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url=url.nwcalculatorinfoshow_QA, json=data, headers=headers, verify=False)
        result = r.json()
        print('信息展示结果为：\n',result)

        if result['successful'] == True :
            if testdata['productType'] == "NWYY":
                if result['data']['NwYyMaxDays'] != "" and result['data']['NwYyExpectSettleRate'] != "" and result['data']['NwYyMinAmount'] != "":
                    logger.info(testdata['productType'] + "计算器信息展示接口：执行成功！")
                    self.assertEqual(str(result['data']['NwYyMaxDays']),str(38))
                else:
                    logger.error(testdata['productType'] + "计算器信息展示接口：执行失败！")
            elif testdata['productType'] == "NWYYOPT":
                if result['data']['NwYyOptMinAmount'] != "" and result['data']['NwYyOptMaxDays'] != "" and result['data']['NwYyOptRemainDays'] != "" and result['data']['NwYyOptDayprofitrate'] != "":
                    logger.info(testdata['productType'] + "计算器信息展示接口：执行成功！")
                    self.assertEqual(str(result['data']['NwYyOptMaxDays']), str(38))
                else:
                    logger.error(testdata['productType'] + "计算器信息展示接口：执行失败！")
            elif testdata['productType'] == "NWZY":
                if result['data']['NwZyMinAmount'] != "":
                    logger.info(testdata['productType'] + "计算器信息展示接口：执行成功！")
                    self.assertEqual(str(result['data']['NwZyMinAmount']), str(100))
                else:
                    logger.error(testdata['productType'] + "计算器信息展示接口：执行失败！")
        else:
            logger.error(testdata['productType'] + "计算器信息展示接口：执行失败！\n" + result['msg'])
    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func

    def tearDown(self):
        logger.info("************** 新月盈、新众盈计算器信息展示接口执行结束 ************** ")


"""类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称"""
__generateTestCases(NwCalculatorInfoShow, "NwCalculatorInfoShow", "APIdata_Nwproduct.xlsx", "NwCalculatorInfoShow")

if __name__ == "__main__":
    unittest.main(verbosity=1)
