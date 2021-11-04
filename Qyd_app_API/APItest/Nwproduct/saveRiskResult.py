# -*- coding:utf-8 -*
"""
 @author 190319L
 date 2018/10/15 16:16
 @Project&file: Qyd_app_API saveRiskResult.py
"""
from lib.qyd_app_common import *
import json
import unittest
import requests
from Config import url
from lib.log import logger
from lib.generateTestCases import __generateTestCases

class saveRiskResult(unittest.TestCase):
    u'48.04 保存风险评测结果 --- 戴文瀚'
    def setUp(self):
        logger.info('************** [保存风险评测结果]接口开始执行 **************')

    def getTest(self, testdata):
        print("入参为： ")
        print(testdata)
        headers = {
            "Content-Type":"application/json",
            "X-Auth-Token":applogin(config.username_dwh,config.passwd_dwh)
        }
        data = {
                "type":testdata['type'],
                "question1":testdata['question1'],
                "question2":testdata['question2'],
                "question3":testdata['question3'],
                "question4":testdata['question4'],
                "question5":testdata['question5'],
                "question6":testdata['question6'],
                "question7":testdata['question7'],
                "question8":testdata['question8'],
                "question9":testdata['question9'],
                "question10":testdata['question10'],
                "question11":testdata['question11']
                }
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url=url.saveRiskResult_QA, json=data, headers=headers, verify=False)
        result = r.json()
        # print(result)
        ''' json格式化输出-json.dumps，便于调试及后续定位异常 '''
        result_dump = json.dumps(result, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ':'))
        logger.info(result_dump)

        if result["status"] == 200 and result['successful'] == True:
            self.assertEqual(result['code'], 10000)
            self.assertEqual(result['msg'], u'成功')
            logger.info("保存风险评测结果：执行成功！\n" + str(result_dump))
        '''接口服务层未针对异常参数进行判断，导致数据库可能存入非法数值，从而出现前端无法解析的问题，待优化及后续跟进'''
        # elif result["status"] == 400 and result['successful'] == False:
        #     self.assertEqual(result['resultCode']['code'], 'InParamParseERROR')
        #     self.assertEqual(result['resultCode']['message'], 'Failed to de-serialize record')
        #     logger.info("保存风险评测结果：参数缺失或异常，结果符合预期！\n" + str(result_dump))
        else:
            logger.info("保存风险评测结果：执行失败！\n" + '其他未知错误' + str(result_dump))

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func

    def tearDown(self):
        logger.info("************** [保存风险评测结果]接口执行完毕 ************** ")


"""类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称"""
__generateTestCases(saveRiskResult, "saveRiskResult", "APIdata_3.6.3.xlsx", "saveRiskResult")

if __name__ == "__main__":
    unittest.main(verbosity=1)