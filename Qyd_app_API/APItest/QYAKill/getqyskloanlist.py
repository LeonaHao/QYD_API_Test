#-*- coding:utf-8 -*-

from lib.qyd_app_common import *
import json
import unittest
import requests
from Config import url
from lib.log import logger
from Config import config
from lib.mysqldb import mysqldb
from lib.generateTestCases import __generateTestCases

tel_num = '16871725120'
pwd = 'che001'

def getactiveId():
    # 查询数据库中配置的所有活动
    sql_activity_all = 'SELECT * from activity_config  ORDER BY startTime DESC '
    activity_all_list = mysqldb('qydproduction').selectsql(sql_activity_all)
    if len(activity_all_list) > 0:
        activity_id = activity_all_list[0]['id']
        return activity_id
    else:
        return 0

def getTest(activeId):
    headers = {
            "Content-Type": "application/json",
            "X-Auth-Token": applogin(tel_num, pwd)
                }
#        print(headers)
    body = {
            "activeId": activeId,
            "pageNumber": 1,
            "pageSize": 1000
            }
    print(body)
    requests.packages.urllib3.disable_warnings()
    r = requests.post(url.getqyskloanlist_QA, json=body, headers=headers, verify=False)
    result = r.json()
    '''json格式化输出-json.dumps，便于调试及后续定位异常，json.dumps()用于将dict类型的数据转成str，
    因为如果直接将dict类型的数据写入json文件中会发生报错，因此在将数据写入时需要用到该函数。 '''
    result_dump = json.dumps(result, indent=4, ensure_ascii=False, separators=(',', ':'))

    if result['code'] == 10000:
        logger.info("————————————————轻盈A秒杀标的组成接口返回成功————————————————")
        logger.info("轻盈A秒杀活动购买页展示接口返回信息：" + result_dump)
        assert(result['msg'] == '成功')
        assert(result['successful'] == True)
        assert(len(result['data']) != 0)#正常情况下，创建活动批次必定会有匹配的标的
    else:
        logger.info("————————————————轻盈A秒杀标的组成接口返回失败————————————————")
        logger.info(result['msg'])

if __name__ == "__main__":
    activity_id = getactiveId()
    if activity_id == 0:
        logger.info("当前没有创建活动")
    else:
        getTest(activity_id)

