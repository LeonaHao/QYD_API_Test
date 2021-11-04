#-*- coding:utf-8 -*-

from lib.qyd_app_common import *
import json
import requests
from Config import url
from lib.log import logger
from lib.mysqldb import mysqldb


def getbatch():
    # 查询数据库中配置的所有活动
    sql_activity_all = 'SELECT * from activity_config  ORDER BY startTime DESC '
    activity_all_list = mysqldb('qydproduction').selectsql(sql_activity_all)
    if len(activity_all_list) > 0:
        activity_id = activity_all_list[0]['id']
        logger.info('数据库中数据库中配置的所有活动: ')
        logger.info(activity_all_list)
        activity_batchs_sql = 'SELECT id from activity_batch_config where activityId = "' + str(activity_id) + '"'
        activity_batchs_id = mysqldb('qydproduction').selectsql(activity_batchs_sql)[0]['id']
        print(activity_batchs_id)
        return activity_batchs_id
    else:
        return 0

def getTest(batch_id):
    headers = {
            "Content-Type": "application/json",
            "X-Auth-Token": applogin()
                }
#        print(headers)
    body = {
            "batchId": batch_id
            }
#        print(body)
    requests.packages.urllib3.disable_warnings()
    r = requests.post(url.secondkillbuyshow_QA, json=body, headers=headers, verify=False)
    result = r.json()
    print(result)

    '''json格式化输出-json.dumps，便于调试及后续定位异常，json.dumps()用于将dict类型的数据转成str，
    因为如果直接将dict类型的数据写入json文件中会发生报错，因此在将数据写入时需要用到该函数。 '''
    result_dump = json.dumps(result, indent=4, ensure_ascii=False, separators=(',', ':'))

    if result['code'] == 10000:
        logger.info("————————————————轻盈A秒杀活动购买页展示接口返回成功————————————————")
        logger.info("轻盈A秒杀活动购买页展示接口返回信息：" + result_dump)
        assert(result['msg'] == '成功')
        assert (result['successful'] == True)
    else:
        logger.info("————————————————轻盈A秒杀活动购买页展示接口返回失败————————————————")
        logger.info(result['msg'])

if __name__ == "__main__":
    batch_id = getbatch()
    if batch_id == 0:
        logger.info("当前没有创建活动批次")
    else:
        getTest(batch_id)


