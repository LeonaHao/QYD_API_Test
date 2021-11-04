#-*- coding:utf-8 -*-

from lib.qyd_app_common import *
import json
import unittest
import requests
from Config import url
from lib.log import logger
from lib.mysqldb import mysqldb


tel_num = '16871719260'
pwd = 'che001'
#获取众盈持有中债权列表
def getZyPossession():
    headers = {
                "Content-Type": "application/json",
                "X-Auth-Token": applogin(tel_num, pwd)
                }
#   print(headers)
    body = {
            "page": "1",
            "size": "10"
            }
#   print(body)
    requests.packages.urllib3.disable_warnings()
    r = requests.post(url.getZyPossession_QA, json=body, headers=headers, verify=False)
    result = r.json()
#    print(result)
#    print(result['data'])
    if result['code'] == 10000:
        logger.info("获取众盈持有中债权列表成功!")
#        print(result['data'])
        if len(result['data'])!= 0:
            return (result['data'][0]['possessionId'],result['data'][0]['projectNumber'])
        else:
            logger.info("您目前没有持有中的新众盈！")
            return 1
    else:
        logger.error("获取众盈持有中债权列表失败:\n " + result['msg'])
        return 2



class GetZyPossessionDetail(unittest.TestCase):
    u"""40.5获取众盈投资中债权回款明细--曾娟"""

    def setUp(self):
        logger.info("***************获取众盈投资中债权回款明细开始****************")

    def getTest(self):

        headers = {
                "Content-Type": "application/json",
                "X-Auth-Token": applogin(tel_num, pwd)
                    }
#        print(headers)
        body = {
                "possessionId": getZyPossession()[0]
                }
#        print(body)
        if "possessionId" == "1":
            logger.info(("您目前没有持有中的新众盈！"))
        elif "possessionId" == "2":
            logger.error("获取众盈持有中债权列表失败! ")
        else:
            requests.packages.urllib3.disable_warnings()
            r = requests.post(url.getZyPossessionDetail_QA, json=body, headers=headers, verify=False)
            result = r.json()

            if result['code'] == 10000:
                print(result)
                self.assertEqual(str(result['successful']), str(True))
                if len(result['data']) == 0:
                    logger.info("您目前没有持有中的新众盈!")
                else:
                    logger.info("新众盈投资中债权回款明细: ")
                    for i in range(len(result['data']['list'])):
                        print(result['data']['list'][i])

                    sql_userid = 'SELECT id from `user` where tel_num = "' + str(tel_num) + '"'
#                    print(sql_userid)
                    user_id = mysqldb('qydproduction').selectsql(sql_userid)[0]['id']
#                    print('user_id: ', user_id)

                    # 查询数据库中持有中的众盈
                    sql_xzypossession = 'SELECT project_number from mt_possession where user_id = "' + str(
                        user_id) + '" and hold_amount > 0 '
    #                print(sql_xzypossession)
                    sql_result = mysqldb("qydnewproduction").selectsql(sql_xzypossession)
    #                print("sql_result: ", sql_result)
                    project_number_list = []
                    for i in range(len(sql_result)):
                        project_number_list.append(str(sql_result[i]['project_number']))
                    self.assertIn(str(getZyPossession()[1]), project_number_list)
            else:
                logger.error("获取新众盈投资中债权回款明细失败:\n " + result['msg'])

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)

        return func


    def tearDown(self):
        logger.info("***************获取众盈投资中债权回款明细结束****************")

a = GetZyPossessionDetail()
a.getTest()


