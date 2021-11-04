# -*- coding:utf-8 -*
"""
 @author 190319L
 date 2018/7/31 17:24
 @Project&file: Qyd_app_API_Zengjuan getZyPossession.py
"""
from lib.qyd_app_common import *
import json
import unittest
import requests
from Config import url
from lib.log import logger
from lib.generateTestCases import __generateTestCases

class getZyPossession(unittest.TestCase):
    u'40.17 获取众盈(升级版)持有中债权列表 --- 戴文瀚'
    def setUp(self):
        logger.info('************** [获取众盈(升级版)持有中债权列表]接口开始执行 **************')

    def getTest(self, testdata):
        print("入参为： ")
        print(testdata)
        headers = {
            "Content-Type":"application/json",
            "X-Auth-Token":applogin(config.username_dwh,config.passwd_dwh)
        }
        data = {
                "page":testdata['page'],
                "size":testdata['size']
                }
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url=url.getZyPossession_QA, json=data, headers=headers, verify=False)
        result = r.json()
        # print(result)
        # ''' json格式化输出-json.dumps '''
        # result_dump = json.dumps(result, sort_keys=True, indent=4, separators=(',', ':'))
        # logger.info(result_dump)
        if result["status"] == 200 and result['successful'] == True:
            self.assertEqual(result['code'], 10000)
            self.assertEqual(result['msg'], u'成功')
            logger.info("获取众盈(升级版)持有中债权列表：执行成功！\n" + str(result))
        elif result["status"] == 400 and result['successful'] == False:
            self.assertEqual(result['resultCode']['code'], 'InParamParseERROR')
            logger.info("获取众盈(升级版)持有中债权列表：参数异常符合预期！\n" +  "错误原因：" + str(result))#result['resultCode']['message'])
        elif result["status"] == 200 and result['successful'] == False and result['code'] == 50002:
            self.assertEqual(result['msg'], u'请求参数不完整')
            logger.info("获取众盈(升级版)持有中债权列表：参数异常符合预期！\n" + "错误原因：" + str(result))#result['msg'])
        else:
            logger.info("获取众盈(升级版)持有中债权列表：执行失败！\n" + str(result))

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func

    def tearDown(self):
        logger.info("************** [获取众盈(升级版)持有中债权列表]接口执行完毕 ************** ")


"""类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称"""
__generateTestCases(getZyPossession, "getZyPossession", "APIdata_3.6.3.xlsx", "getZyPossession")

if __name__ == "__main__":
    unittest.main(verbosity=1)