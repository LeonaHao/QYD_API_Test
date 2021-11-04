#-*- coding:utf-8 -*-

from lib.qyd_app_common import *
import json
import unittest
import requests
from Config import url,pc_url
from Config import config
from lib.qyd_pc_common import *
from lib.log import logger


pc_token = qydFrontLogin(config.tel_num, config.passwd)
print(pc_token)

#APP端获取可提现金额:http://wiki.ky.com/pages/viewpage.action?pageId=15999392
#withdrawalAmount:可提现金额
#pledgeAmount：质押金额
#processingAmount：处理中金额
#lockAmount：锁定金额
def app_getwithdrawalamount():
    print('\n\n****************APP端获取可提现金额****************')
    headers = {
            "Content-Type": "application/json",
            "X-Auth-Token": applogin()
                }
#    print(headers)

    requests.packages.urllib3.disable_warnings()
    r = requests.post(url.withdrawalamount_QA, headers=headers, verify=False)
    result = r.json()
    print(result['mapData'])
    print("APP可提现金额：", result['mapData']['withdrawalAmount'])
    print("APP提现处理中金额：", result['mapData']['processingAmount'])
    print("APP中锁定金额：", result['mapData']['lockAmount'])
    print("APP中质押金额：", result['mapData']['pledgeAmount'])
    return result['mapData']

#PC端【前台】账户总览---累计结算收益、可用余额、处理中金额、余额接口
# http://wiki.ky.com/pages/viewpage.action?pageId=5523693
#balance：余额
#availableAmount：可用余额
#handlingAmount：处理中金额
#transferingInAmount：投资处理中
#handlingWithoutTransferIn：不包含投资处理中的处理中金额
#pledgeAmount：质押金额
def getaccountinfo():
    print("\n\n****************PC端【前台】账户总览---累计结算收益、可用余额、处理中金额、余额接口****************")
    headers = {
            "Content-Type": "application/json",
            "X-Auth-Token": pc_token
                }
#    print(headers)

    requests.packages.urllib3.disable_warnings()
    r = requests.post(pc_url.accountinfo_QA, headers=headers, verify=False)
    result = r.json()
    print("PC账户总览:")
    print("entity:",result['entity'])
    return result['entity']


#PC端6.0.4查询锁定总金额和可提现金额（前台）http://wiki.ky.com/pages/viewpage.action?pageId=5523744
#lockAmount:锁定金额
#availableAmount：可用余额
#frozenAmount：质押总额
#outAccountAmount：可提现、可转账、可代扣金额
def getlockamountandfrozenamount():
    print('\n\n****************PC端6.0.4查询锁定总金额和可提现金额****************')
    headers = {
            "Content-Type": "application/json",
            "X-Auth-Token": pc_token
                }
#    print(headers)
    requests.packages.urllib3.disable_warnings()
    r = requests.post(pc_url.getlockamountandfrozenamount_QA, headers=headers, verify=False)
    result = r.json()
    print("PC锁定总金额和可提现金额：\n", result['entity'])
    return result['entity']

app_withdraw = app_getwithdrawalamount()
pc_accountinfo = getaccountinfo()
pc_lockamountandfrozenamount = getlockamountandfrozenamount()


print("*************************************************************************")
if app_withdraw['withdrawalAmount'] == pc_lockamountandfrozenamount['outAccountAmount']:
    print("APP可提现金额与PC一致")
else:
    print("APP可提现金额与PC不一致")

if app_withdraw['processingAmount'] == pc_accountinfo['handlingWithoutTransferIn']:
    print("APP提现处理中金额与PC一致")
else:
    print("APP提现处理中金额与PC不一致")

if app_withdraw['lockAmount'] == pc_lockamountandfrozenamount['frozenAmount']:
    print("APP锁定金额与PC一致")
else:
    print("APP锁定金额与PC不一致")

if app_withdraw['pledgeAmount'] == pc_accountinfo['pledgeAmount']:
    print("APP质押金额与PC一致")
else:
    print("APP质押金额与PC不一致")


