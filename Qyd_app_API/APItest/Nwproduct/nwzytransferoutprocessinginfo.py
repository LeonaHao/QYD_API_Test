#-*- coding:utf-8 -*-

from lib.qyd_app_common import *
import json
import unittest
import requests
from Config import url
from lib.log import logger
from lib.generateTestCases import __generateTestCases

class NwZyTransferoutProcessingInfo(unittest.TestCase):
    u"""40.11 新众盈转让处理中接口--曾娟"""

    def setUp(self):
        logger.info("***************获取新众盈转让处理中信息开始****************")

    def getTest(self):
        headers = {
                "Content-Type": "application/json",
                "X-Auth-Token": applogin()
                    }
#        print(headers)

        requests.packages.urllib3.disable_warnings()
        r = requests.post(url.nwzytransferoutprocessinginfo_QA,headers=headers,verify=False)
        result = r.json()
        print("获取新众盈转让处理中信息：\n",result)

        if result['code'] == 10000:
            self.assertEqual(str(result['successful']), str(True))

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)

        return func

    def tearDown(self):
        logger.info("***************获取新众盈转让处理中信息结束****************")


if __name__ == "__main__":
    unittest.main(verbosity=1)

a = NwZyTransferoutProcessingInfo()
a.getTest()
