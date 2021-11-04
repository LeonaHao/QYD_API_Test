# -*- coding:utf-8 -*-
import unittest
import requests
from Config import config
from Config import url
from lib.log import logger
from lib import qyd_app_common
from lib.generateTestCases import __generateTestCases

class IncomeCalculator(unittest.TestCase):
    u'40.2 收益计算器计算接口 --曾娟'
    def setUp(self):
        logger.info('************** 收益计算器计算接口开始执行 **************')

    def getTest(self, testdata):
        print("入参为： ",testdata)
        headers = {"Content-Type": "application/json"}
        data = {
                "amount":testdata['amount'],
                "product":testdata['product'],
                "totalDays":testdata['totalDays'],
                "remainDays":testdata['remainDays']
                }
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url=url.newincomecalculator_QA, json=data, headers=headers, verify=False)
        result = r.json()
        print('计算结果为：\n',result)

        if result['code'] == 10000:
            logger.info(testdata['product'] + "收益计算器：执行成功！")
            self.assertEqual(str(result['data']['amount']), str(testdata['amount1']))
            self.assertEqual(str(result['data']['profit']), str(testdata['profit']))
        else:
            logger.info(testdata['product'] + "收益计算器：执行失败！")



    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func

    def tearDown(self):
        logger.info("************** 收益计算器计算接口执行完毕 ************** ")


"""类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称"""
__generateTestCases(IncomeCalculator, "incomecalculator", "APIdata_Nwproduct.xlsx", "incomecalculator")

if __name__ == "__main__":
    unittest.main(verbosity=1)

