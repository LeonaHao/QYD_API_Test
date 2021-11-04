#-*- coding:utf-8 -*-

from lib.qyd_app_common import *
import json
import unittest
import requests
from Config import url
from lib.log import logger
from lib.generateTestCases import __generateTestCases

class GetUserInformation(unittest.TestCase):
    u"""40.9 【新增新众盈、新月盈、新手标】 获取首页信息(接口改造合并，首页置顶)--曾娟"""

    def setUp(self):
        logger.info("***************获取首页信息开始****************")

    def getTest(self, testdata):
        headers = {
                "Content-Type": "application/json",
                "X-Auth-Token": applogin()
                    }
#        print(headers)
        body = {
                "appVersion": testdata['appVersion'],
                "type":testdata['type']
                }
#        print(body)
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url.getuserinformation_QA,json= body,headers=headers,verify=False)
        result = r.json()
        print(result)
        # ''' json格式化输出-json.dumps，便于调试及后续定位异常 '''
        # result_dump = json.dumps(result, indent=4, ensure_ascii=False, separators=(',', ':'))
        # logger.info(result_dump)

        if result['status'] == 200:
            self.assertEqual(str(result['successful']), str(True))


    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)

        return func

    def tearDown(self):
        logger.info("***************获取首页信息结束****************")

"""类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称"""
__generateTestCases(GetUserInformation, "GetUserInformation", "APIdata_Nwproduct.xlsx", "GetUserInformation")

if __name__ == "__main__":
    unittest.main(verbosity=1)


