# -*- coding:utf-8 -*-
import requests
import base64
import json
from Config import url
from Config import config
from lib.log import logger
import os
import sys


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
    u"""轻易贷前端登录"""
   # logger.info("qydFrontLogin login is running...")
    headers = {"Content-Type": "application/json"}
    token = base64.b64encode((username+":"+passwd).encode("utf-8"))
    data = 'Basic %s' % token
    data=data.replace("'","").replace("b","")
    body={}
    body["authorization"]=data
    data_json = json.dumps(body)
    r=requests.post(url.qydFrontLoginUrl,data=data_json,headers=headers)
    result=r.json()
    #print(result)
    return result['entities'][0]['xAuthToken']

#qydFrontLogin("16823246661","che001")


def appgetToken():
    u"app获取token"
    headers = {"Content-Type": "application/json"}
    requests.packages.urllib3.disable_warnings()
    r=requests.post(url.appgetToken_QA,headers=headers,verify=False)
    result=r.json()
#    print("token: " + result['mapData']['token'])
    return result['mapData']['token']


def getsubmittoken():
        u"app获取submitToken"
        headers = {"Content-Type": "application/json",
                   "X-Auth-Token":appgetToken()
        }
        requests.packages.urllib3.disable_warnings()
        r = requests.post(url.appgetsubmittoken_QA, headers=headers, verify=False)
        result = r.json()
#        print("submitToken: " + result['mapData']['submitToken'])
        return result['mapData']['submitToken']


def applogin(*args):
    u"app带用户名和密码登录接口"
    logger.info("qyd_app login is running...")
    headers = {"Content-Type": "application/json",
                "X-Auth-Token":appgetToken()}
#    print("headers: ",headers)
    requests.packages.urllib3.disable_warnings()
    #根据传参个数判断所需要登录的账号
    if len([*args]) == 0:
        data = {
            "appversion": "3.6.4",
            "imei": "861463035746799",
            "sysversion": "5.1",
            "appmac": "C8:F2:30:73:C8:51",
            "imsi": "IMSI",
            "height": "1812",
            "width": "1080",
            "system": "ANDROID",
            "loginWay": "1",
            "channel": "2",
            "deviceId": "861463035746799",
            "deviceName": "BLN-AL40",
            "authorization": "Basic " + str(base64.b64encode((config.username + ":" + config.passwd).encode("utf-8")),
                                            'utf-8')
        }
    elif len([*args]) == 2:
        data = {
            "appversion": "3.6.4",
            "imei": "861463035746799",
            "sysversion": "5.1",
            "appmac": "C8:F2:30:73:C8:51",
            "imsi": "IMSI",
            "height": "1812",
            "width": "1080",
            "system": "ANDROID",
            "loginWay": "1",
            "channel": "2",
            "deviceId": "861463035746799",
            "deviceName": "BLN-AL40",
            "authorization": "Basic " + str(base64.b64encode((args[0] + ":" + args[1]).encode("utf-8")),
                                            'utf-8')
        }
    else:
        pass
    r=requests.post(url=url.applogin_QA,json=data,headers=headers,verify=False)
    result=r.json()
#    print("Response headers: ", r.headers)
#    print("登录结果",result)
#    print(result['mapData']['xAuthToken'])
    if result['status'] == 200 and result['successful'] == True:
        logger.info(sys._getframe().f_code.co_name + " is running success!")
        return result['mapData']['xAuthToken']
    else:
        logger.error("applogin is running failure!")
        return result




#print(appgetToken())
#print(getsubmittoken())
# print(applogin())
# print (applogin(config.username_dwh,config.passwd_dwh))



