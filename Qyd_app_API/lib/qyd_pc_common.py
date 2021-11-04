# -*- coding:utf-8 -*-
import requests
import base64
import json
import time
from Config import pc_url
from lib.log import logger


def qydManageLogin():
    """轻易贷管理台登录"""
    logger.info("qydManageLogin login is running...")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
        "Content-Type": "application/json; charset=UTF-8",
        "Connection": "keep-alive"
    }
    requests.packages.urllib3.disable_warnings()
    r=requests.get(url.qydManageLoginUrl,headers=headers,verify=False)
    result=r.json()
    return result['data']['token']

def qydFrontLogin(username,passwd):
    # u"""轻易贷前端登录"""#备注，如果不同设备登录的话需要验证码验证登录，这块逻辑复杂暂时没有写
    # headers = {"Content-Type": "application/json"}
    # requests.packages.urllib3.disable_warnings()
    # token = base64.b64encode((username+":"+passwd).encode("utf-8"))
    # data = 'Basic %s' % token
    # data=data.replace("'","").replace("b","")
    # print(data)
    # body={  "loginWay":1,
    #         "channel":1,
    #         "deviceId":"c13a03ae13eefce4abc366dd64784179",
    #         "deviceName":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    #         }
    # body["authorization"]=data
    # data_json = json.dumps(body)
    # r=requests.post(url=url.qydFrontLoginUrl,data=data_json,headers=headers,verify=False)
    # result=r.json()
    # logger.info("轻易贷前端登录获取token..："+str(result['entities'][1]['xAuthToken']))
    # return result['entities'][1]['xAuthToken']
    u"""轻易贷前端登录"""
    headers = {"Content-Type": "application/json"}
    requests.packages.urllib3.disable_warnings()
    token = base64.b64encode((username+":"+passwd).encode("utf-8"))
    data = 'Basic %s' % token
    data=data.replace("'","").replace("b","")
    body={}
    body["authorization"]=data
    data_json = json.dumps(body)
    r=requests.post(url=pc_url.qydFrontLoginUrl11,data=data_json,headers=headers,verify=False)
    result=r.json()
    logger.info("轻易贷前端登录获取token..："+str(result['entities'][0]['xAuthToken']))
    return result['entities'][0]['xAuthToken']


"""垫付宝前台登录"""
def dfblogin(tel_num,pwd):
    u"""会员登录"""
    requests.packages.urllib3.disable_warnings()
    logger.info("会员登录 is running...")

    diction = {"deviceType":"WINDOWS",
                "deviceName":"computer",
                "deviceId":"1234561985",
                "phone":tel_num,
                "passwd":pwd
                }



    a = diction["phone"] + ":" + diction["passwd"]
    auth = base64.b64encode(a.encode(encoding="utf-8")).decode(encoding='utf-8')
    headers = {"Authorization": "Basic " + auth}
    ucUserLogin = url._user + "/dfb/user/login"
    r = requests.get(
        ucUserLogin + "?deviceType=" + diction["deviceType"] + "&deviceName=" + diction["deviceName"] + "&deviceId=" +
        diction["deviceId"], headers=headers)
    result = r.json()
    if result["code"] == 10000:
        return result['code']
    else:
        logger.error('******垫付宝登录失败*********')



"""垫付宝管理台登录"""
def login_backed():
    username = "admin"
    password = "ultche001"
    auth = username + ":" + password
    headers = {"Content-Type": "application/json",
                   "authorization": "Basic " + base64.b64encode(auth.encode(encoding="utf-8")).decode(encoding='utf-8')}
    head = requests.get(url=url.host_admin_login, headers=headers)
    return head.headers['X-Auth-Token']

#qydFrontLogin("16871740965","che001")
