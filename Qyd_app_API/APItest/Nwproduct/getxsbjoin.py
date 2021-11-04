# -*- coding:utf-8 -*
"""
 @author 190319L
 date 2018/8/24 14:57
 @Project&file: Qyd_app_API getxsbjoin.py
"""
from lib.qyd_app_common import *
import json
import unittest
import requests
from Config import url
from lib.log import logger
from lib.generateTestCases import __generateTestCases

class getxsbjoin(unittest.TestCase):
    u'41.04 新手专享参与人数查询 --- 戴文瀚'
    def setUp(self):
        logger.info('************** [新手专享参与人数查询]接口开始执行 **************')

    def getTest(self,testdata):
        print("入参为： ")
        print(testdata)
        headers = {
            "Content-Type":"application/json",
            "X-Auth-Token":applogin(config.username_dwh,config.passwd_dwh)
        }
        data = {
                "productType":testdata['productType']
                }
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url=url.getxsbjoin_QA, json=data, headers=headers, verify=False)
        result = r.json()
        # print(result)
        ''' json格式化输出-json.dumps，便于调试及后续定位异常 '''
        result_dump = json.dumps(result, sort_keys=True, indent=4, separators=(',', ':'))
        logger.info(result_dump)

        if result["status"] == 200 and result['successful'] == True:
            self.assertEqual(result['code'], 10000)
            self.assertEqual(result['msg'], u'成功')
            logger.info("新手专享参与人数查询：执行成功！\n" + str(result))
        elif result["status"] == 400 and result['successful'] == False:
            self.assertEqual(result['resultCode']['code'], 'InParamParseERROR')
            self.assertIn(u'入参不可为空',result['resultCode']['message'])
            logger.info("新手专享参与人数查询：参数异常符合预期！\n" + "错误原因：" + result['resultCode']['message'])
        else:
            logger.info("新手专享参与人数查询：执行失败！\n" + '其他未知错误' + str(result_dump))

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func

    def tearDown(self):
        logger.info("************** [新手专享参与人数查询]接口执行完毕 ************** ")


"""类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称"""
__generateTestCases(getxsbjoin, "getxsbjoin", "APIdata_3.6.3.xlsx", "getxsbjoin")

if __name__ == "__main__":
    unittest.main(verbosity=1)