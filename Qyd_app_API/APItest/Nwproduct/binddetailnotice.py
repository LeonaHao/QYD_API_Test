#-*- coding:utf-8 -*-

from lib.qyd_app_common import *
import json
import unittest
import requests
from Config import url
from lib.log import logger
from lib.generateTestCases import __generateTestCases

class Binddetailnotice(unittest.TestCase):

    u"""到期还本付息弹窗----------毛景景"""

    def setUp(self):
        logger.info("***************到期还本付息弹窗开始获取****************")

    def getTest(self,testdata):

        param = {
                 "productType": testdata['productType']
               }

        requests.packages.urllib3.disable_warnings()
        r = requests.post(url=url.binddetailnotice_QA,json= param,verify=False)
        result = r.json()

        if result['code'] == 10000:
            logger.info(testdata['productType'] + ': ' + "到期还本付息弹窗成功")
            print (result)

#        else result['code'] == 50024:
   #         logger.info( testdata['productType'] + ': ' + result['msg'])


    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)

        return func

    def tearDown(self):
        logger.info("***************结束****************")

"""类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称"""
__generateTestCases(Binddetailnotice, "binddetailnotice", "binddetailnotice.xlsx", "binddetailnotice")

if __name__ == "__main__":
    unittest.main(verbosity=1)


