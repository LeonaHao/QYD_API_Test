#/entrance/apis/register/newgetuserinformation/json 接口测试

# -*- coding:utf-8 -*-
import unittest
import requests
from Config import url
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from lib.qyd_app_common import applogin,appgetToken

"""接口返回数据取自zk"""
class messagecontext(unittest.TestCase):
    u'40.15 提示弹窗文案接口（新众盈预期年化结算利率等） --- 戴文瀚'
    def setUp(self):
        logger.info("************** [提示弹窗文案]接口开始执行 **************")


    def getTest(self,testdata):
        headers = {
            "Content-Type": "application/json",
            "X-Auth-Token": appgetToken()
        }

        """请求参数"""
        req_data = {"type": "05"}
        req_data['type']=testdata['type']

        respon = requests.post(url=url.messagecontext_QA, json=req_data, headers=headers, verify=False).json()
        print("zk配置key",testdata['key'])
        print("返回",respon['mapData']['context'])
        print("预期",testdata['context'])
        self.assertEqual(respon['mapData']['context'],testdata['context'])

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func
    def tearDown(self):
        logger.info("************** [提示弹窗文案]接口 执行完毕 **************")

#类名称，用例别名，数据文件名，sheet名称
__generateTestCases(messagecontext,"abc","APIdata.xlsx","message")
if __name__ == "__main__":
    unittest.main(verbosity=1)
