#-*- coding:utf-8 -*-

from lib.qyd_app_common import *
import json
import unittest
import requests
from Config import url
from lib.log import logger
from lib.generateTestCases import __generateTestCases

class NwGetAppointmentStatus(unittest.TestCase):
    u'40.7 获取预约理财状态【兼容老版本】--曾娟'
    def setUp(self):
        logger.info('************** 获取预约理财状态接口开始执行 **************')

    def getTest(self):
        headers = {
                    "Content-Type": "application/json",
                    "X-Auth-Token": applogin()
                    }
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url=url.nwgetappointmentstatus_QA,headers=headers, verify=False)
        result = r.json()
#        print('获取预约理财状态结果为：\n',result)

        if result['code'] == 10000:
            print(result)
            logger.info("获取预约理财状态成功!")
            self.assertEqual(str(result['successful']),str(True))
        else:
            logger.error("获取预约理财状态失败:\n " + result['msg'])
    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func

    def tearDown(self):
        logger.info("************** 获取预约理财状态接口执行完毕 ************** ")

a = NwGetAppointmentStatus()
a.getTest()
