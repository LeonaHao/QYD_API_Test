# -*- coding:utf-8 -*
"""
 @author 190319L
 date 2018/7/31 17:35
 @Project&file: Qyd_app_API_Zengjuan getfinanceproductinfo.py
"""
from lib.qyd_app_common import *
import json
import unittest
import requests
from Config import url
from lib.log import logger
from lib.generateTestCases import __generateTestCases

class getfinanceproductinfo(unittest.TestCase):
    u'40.16  获取理财页信息接口(理财页置顶) --- 戴文瀚'
    def setUp(self):
        logger.info('************** [获取理财页信息]接口 开始执行 **************')

    def getTest(self, testdata):
        print("入参为： ")
        print(testdata)
        headers = {
            "Content-Type":"application/json"
        }
        data = {
            "type" : testdata['type']
                }
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url=url.getfinanceproductinfo_QA, json=data, headers=headers, verify=False)
        result = r.json()
        #json格式化输出-json.dumps
        result_dump = json.dumps(result, sort_keys=True, indent=4, separators=(',', ':'))
        logger.info(result_dump)
        # print(result)

        if result["status"] == 200 and result['successful'] == True:
            self.assertEqual(result['mapData']['QYProductMsg']['yearYieldRate'], '8.62')
            self.assertEqual(result['mapData']['QYTransferMsg']['yearYieldRate'], '8.62')
            self.assertEqual(result['mapData']['XXSBProductInfo']['XXSBBasicsProfit'], '8.1')
            self.assertEqual(result['mapData']['XXSBProductInfo']['XXSBRewardProfit'], '6.9')
            self.assertEqual(result['mapData']['XYYOPTProductInfo']['highestRate'], '10.08')
            self.assertEqual(result['mapData']['XYYProductInfo']['NwYyExpectSettleRate'], '8.10')
            self.assertEqual(result['mapData']['XZYProductInfo']['NwZyMaxExpectRate'], '9.02')
            self.assertEqual(result['mapData']['YYProductMsg']['actualYearProfitRate'], '7.61')
            self.assertEqual(result['mapData']['YYTransferMsg']['yearYieldRate'], '8.10')
            self.assertEqual(result['mapData']['ZYProductInfo']['yearExpectProfit'], '9.02')
            logger.info("获取理财页信息：执行成功！")
        else:
            logger.info("获取理财页信息：执行失败！\n" + result['msg'])

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func

    def tearDown(self):
        logger.info("************** [获取理财页信息]接口 执行完毕 ************** ")


"""类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称"""
__generateTestCases(getfinanceproductinfo, "getfinanceproductinfo", "APIdata_3.6.3.xlsx", "getfinanceproductinfo")

if __name__ == "__main__":
    unittest.main(verbosity=1)