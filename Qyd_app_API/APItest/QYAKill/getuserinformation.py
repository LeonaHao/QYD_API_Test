#-*- coding:utf-8 -*-

from lib.qyd_app_common import *
import json
import unittest
import requests
from Config import url
from lib.log import logger
from lib.mysqldb import mysqldb
import datetime
from lib.generateTestCases import __generateTestCases

tel_num = '16871725120'
pwd = 'che001'
class Getuserinformation(unittest.TestCase):
    u"""44.01 获取首页信息接口——轻盈A秒杀活动信息--曾娟"""

    def setUp(self):
        logger.info("***************获取首页信息接口开始****************")

    def getTest(self, testdata):
        headers = {
                "Content-Type": "application/json",
                "X-Auth-Token": applogin(tel_num, pwd)
                    }
#        print(headers)
        body = {
                "appVersion": testdata['appVersion'],
                "type": testdata['type'],
                "dropVersion": testdata['dropVersion']
                }
#        print(body)
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url.getuserinformation_QA, json=body, headers=headers, verify=False)
        result = r.json()
        QYAKillProductInfo = result['mapData']['QYAKillProductInfo']
        '''json格式化输出-json.dumps，便于调试及后续定位异常，json.dumps()用于将dict类型的数据转成str，
        因为如果直接将dict类型的数据写入json文件中会发生报错，因此在将数据写入时需要用到该函数。 '''
        QYAKillProductInfo_dump = json.dumps(QYAKillProductInfo, indent=4, ensure_ascii=False, separators=(',', ':'))
        logger.info("首页接口返回轻盈A秒杀活动相关信息：" + QYAKillProductInfo_dump)

        #获取数据库中轻盈A秒杀活动配置数据
        sql_QYAKillconfig = 'SELECT * from data_dictionary where classify="qya-Second-Kill"'
#        print(sql_QYAKillconfig)
        QYAKillconfig = mysqldb('qydproduction').selectsql(sql_QYAKillconfig)
        logger.info('数据库中轻盈A秒杀活动配置: ')
        logger.info(QYAKillconfig)
        for i in QYAKillconfig:
            if i['name'] == '预热时间':
                preheatTime_db = i['description']
                logger.info("预热时间：" + preheatTime_db)
            if i['name'] == '下线时间':
                downlineTime_db = i['description']
                logger.info("下线时间："+ downlineTime_db)
            if i['name'] == '上线平台':
                onlinePlatform_db = i['description']
                logger.info("上线平台：" + onlinePlatform_db)

        self.assertEqual(QYAKillProductInfo['reheatTime'], preheatTime_db)
        self.assertEqual(QYAKillProductInfo['downLineTime'], downlineTime_db)

        # 查询数据库中配置的所有活动
        sql_activity_all = 'SELECT * from activity_config  ORDER BY startTime DESC '
        activity_all_list = mysqldb('qydproduction').selectsql(sql_activity_all)
        if len(activity_all_list) > 0:
            logger.info('数据库中数据库中配置的所有活动: ')
            logger.info(activity_all_list)

        #查询数据库中进行中和未开始的活动
        sql_activity = 'SELECT * from activity_config where endTime >= NOW() ORDER BY startTime'
        activity_list = mysqldb('qydproduction').selectsql(sql_activity)
        if len(activity_list) > 0:
            logger.info('数据库中进行中和未开始的活动: ')
            logger.info(activity_list)
            logger.info(activity_list[0])

        #获取当前时间
        currtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') #由日期格式转化为字符串格式
        currtime_d = datetime.datetime.now().strptime(currtime, '%Y-%m-%d %H:%M:%S') #由字符串格式转化为日期格式
#        print("currtime_d: ", currtime_d)
        logger.info("当前时间为：" + currtime)
        if currtime < preheatTime_db:
            logger.info("————————————轻盈A秒杀活动未开始————————————")
            self.assertEqual(QYAKillProductInfo['activityStatus'], 'noShow')
        elif currtime > preheatTime_db and currtime < downlineTime_db:
            logger.info("————————————轻盈A秒杀活动进行中————————————")
            if len(activity_list) == 0:
                if len(activity_all_list) == 0:
                    logger.info("————————当前没有创建任何活动————————")
                else:
                    logger.info("————————已创建的活动都已结束————————")
                    self.assertEqual(QYAKillProductInfo['activityStatus'], 'finish')
                    activity_ended_id = activity_all_list[0]['id']
                    logger.info("数据库中最近一个已结束活动的id为：\n" + activity_ended_id)
                    activity_batchs_sql = 'SELECT id from activity_batch_config where activityId = "' + str(
                        activity_ended_id) + '"'
                    activity_batchs_idlist = mysqldb('qydproduction').selectsql(activity_batchs_sql)
                    activity_batchs_id = []
                    for i in activity_batchs_idlist:
                        activity_batchs_id.append(i['id'])
                    logger.info("数据库中最近一个已结束活动对应的批次为：")
                    logger.info(activity_batchs_id)
                    self.assertEqual(activity_batchs_id, QYAKillProductInfo['bactchInfo']['id'])

            else:
                activity_ing_id = activity_list[0]['id']
                activity_batchs_sql = 'SELECT id from activity_batch_config where activityId = "' + str(
                    activity_ing_id) + '"'
                activity_batchs_idlist = mysqldb('qydproduction').selectsql(activity_batchs_sql)
                activity_batchs_id = []
                for i in activity_batchs_idlist:
                    activity_batchs_id.append(i['id'])
                if currtime_d >= activity_list[0]['startTime'] and currtime_d <= activity_list[0]['endTime']:
                    logger.info("————————当前有进行中的活动————————")
                    self.assertEqual(QYAKillProductInfo['activityStatus'], 'progress')
                    logger.info("数据库中当前进行中活动对应的批次为：")
                    logger.info(activity_batchs_id)
                    for i in QYAKillProductInfo['bactchInfo']:
                        #校验接口返回数据和数据库中是否一致
                        self.assertIn(i['id'], activity_batchs_id)
                else:
                    logger.info("————————当前有倒计时的活动————————")
                    self.assertEqual(QYAKillProductInfo['activityStatus'], 'countDown')
                    logger.info("数据库中倒计时活动对应的批次为：")
                    logger.info(activity_batchs_id)
                    for i in QYAKillProductInfo['bactchInfo']:
                        self.assertIn(i['id'], activity_batchs_id)


        elif currtime > downlineTime_db:
            logger.info("————————————轻盈A秒杀活动已结束————————————")
            self.assertEqual(QYAKillProductInfo['activityStatus'], 'noShow')

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)

        return func

    def tearDown(self):
        logger.info("***************获取首页信息接口结束****************")

"""类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称"""
__generateTestCases(Getuserinformation, "Getuserinformation", "QYAKill.xlsx", "Getuserinformation")

if __name__ == "__main__":
    unittest.main(verbosity=1)

