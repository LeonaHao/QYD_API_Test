# -*- coding:utf-8 -*
"""
 @author 190319L
 date 2018/10/10 11:11
 @Project&file: Qyd_app_API queryRiskAssess.py
"""
from lib.qyd_app_common import *
import json
import unittest
import requests
from Config import url
from lib.log import logger
from lib.generateTestCases import __generateTestCases

class queryRiskAssess(unittest.TestCase):
    u'48.01 查询风险评测等级信息 --- 戴文瀚'
    def setUp(self):
        logger.info('************** [查询风险评测等级信息]接口开始执行 **************')

    def getTest(self, testdata):
        print("入参为： ")
        print(testdata)
        headers = {
            "Content-Type":"application/json",
            "X-Auth-Token":applogin(config.username_dwh,config.passwd_dwh)
        }
        data = {
                "totalAmount":testdata['totalAmount']
                }
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url=url.queryRiskAssess_QA, json=data, headers=headers, verify=False)
        result = r.json()
        # print(result)
        ''' json格式化输出-json.dumps，便于调试及后续定位异常 '''
        result_dump = json.dumps(result, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ':'))
        logger.info(result_dump)

        if result["status"] == 200 and result['successful'] == True and result['data']['update'] == True:
            self.assertEqual(result['code'], 10000)
            self.assertIn(u'或请您重新评估', result['resultCode']['msg'])
            logger.info("查询风险评测等级信息：执行成功！\n" + str(result_dump))
        elif result["status"] == 200 and result['successful'] == True and result['data']['update'] == False:
            self.assertEqual(result['code'], 10000)
            self.assertEqual(result['data']['newType'], 0)
            self.assertEqual(result['data']['interfaceType'], 'QUERY')
            logger.info("查询风险评测等级信息：执行成功！\n" + str(result_dump))
        elif result["status"] == 550 and result['successful'] == False:
            # self.assertEqual(result['resultCode']['code'], 'InParamParseERROR')
            self.assertEqual(result['code'], 0)
            logger.info("查询风险评测等级信息：参数异常符合预期！\n" + str(result_dump))
        else:
            logger.info("查询风险评测等级信息：执行失败！\n" + '其他未知错误' + str(result_dump))

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func

    def tearDown(self):
        logger.info("************** [查询风险评测等级信息]接口执行完毕 ************** ")


"""类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称"""
__generateTestCases(queryRiskAssess, "queryRiskAssess", "APIdata_3.6.3.xlsx", "queryRiskAssess")

if __name__ == "__main__":
    unittest.main(verbosity=1)