# -*- coding: utf-8 -*
base_new_url = "https://api.tche001.com"
base_old_url = "https://www.tche001.com"
dfb_trade_url = "http://api-yw.local-kaiyuan.com"
dfb_billing_url = "http://dubbo-billing.local-kaiyuan.com"
base_qyd_url = "https://www.localqyd.com/"
base_qyd_urlstg = "https://www.stg-qyd.com/"
base_dfb_url = "http://ult-backend.che001.com"
base_dfb_urlstg = "http://www.kypay.com"

base_url="https://ult-www.qingyidai.com"

##垫付宝PHP重构的base_url
dfb_php_api_url="https://ult-dfb-php-api.dianfubao.com"
"""垫付宝"""
_user = "http://ult-dfb-user-api.dianfubao.com"

"""
ultimate环境：http://dubbo-billing.local-kaiyuan.com
stg环境：http://dubbo-billing.stg-che001.com
"""

"""
ultimate环境：http://api-yw.local-kaiyuan.com
stg环境：http://api-yw.stg-che001.com
"""


host_login = base_new_url + "/user/login/login/?"
host_dfbLogin = base_old_url + "/mobile/user/login/login/?"
host_logout = base_new_url + "/user/login/logout"
host_waybillList = base_new_url + "/vehicle/waybill/bill-list/?"
host_waybillInfo = base_new_url + "/vehicle/waybill/get-info/?"
host_regionList = base_new_url + "/city/region/list?"
host_cityList = base_new_url + "/city/city/list?"
host_provinceList = base_new_url + "/city/province/list/"
host_getCityInfoByName = base_new_url + "/city/city/get-city-info-by-name/?"
# host_reportShipments = base_new_url + "/shipment/info/report-shipments/"
host_reportShipments = base_new_url + "/shipment/info/report-shipments/?"
host_recordShipment = base_new_url + "/shipment/bidrecord/add-bid/?"
host_bidAmount = base_new_url + "/shipment/bidrecord/bidding/?"
host_detailShipment = base_new_url + "/shipment/info/detail/?"
host_callShipment = base_new_url + "/shipment/bidrecord/call/?"
host_listShipment = base_new_url + "/shipment/info/list/?"
host_deleteLine = base_new_url + "/shipment/subscribe/delete?"
host_editLine = base_new_url + "/shipment/subscribe/edit"
host_createLine = base_new_url + "/shipment/subscribe/create"
host_isubscribe = base_new_url + "/shipment/subscribe/operate?"
host_lineInfo = base_new_url + "/shipment/subscribe/info?"
host_shipmentList = base_new_url + "/shipment/subscribe/shipmentlist?"
host_lineList = base_new_url + "/shipment/subscribe/list?"
host_userPermission = base_new_url + "/gasstation/user/get-user-permission/"
host_payMent = base_new_url + "/gasstation/index/payment/"
host_getOtp = base_new_url + "/gasstation/index/get-otp/?"
host_payChannel = base_new_url + "/gasstation/index/get-gasstation-paychannel/?"
host_dfbPayment = base_new_url + "/gasstation/index/payment-paychannel/"
host_deleteMessage = base_new_url + "/message/index/delete?"
host_readMessage = base_new_url + "/message/index/read?"
host_listMessage = base_new_url + "/message/index/list?"
host_infoMessage = base_new_url + "/message/index/info?"
host_salaryPayment = base_new_url + "/salary/pay/payment/"
host_salaryIdentify = base_new_url + "/salary/index/identify/"
host_salaryTopay = base_new_url + "/salary/pay/to-pay/"
host_salaryJudge = base_new_url + "/salary/index/judge/"
host_salaryBindStaff = base_new_url + "/salary/default/bind-staff"
host_salaryOpen = base_new_url + "/salary/index/open/"
host_salaryAddStaff = base_new_url + "/salary/default/add-staff"
host_salaryGetOtp = base_new_url + "/salary/pay/get-otp?"
host_salaryUnbindStaff = base_new_url + "/salary/default/unbind-staff"
host_dfbTrade = dfb_trade_url + "/tx/collection?"
host_billingList = base_new_url + "/payorder/index/list/?"
host_billingDetail = base_new_url + "/payorder/index/list-detail/?"
host_completedTrade = base_new_url + "/dfb/trade/get-completed-trade-list?"
host_uncompletedTrade = base_new_url + "/dfb/trade/get-uncompleted-trade-list?"
host_cashRepay = base_new_url + "/dfb/bill/new-cash-funds-repay?"
host_qydRepay = base_new_url + "/payorder/qyd/cash-repay/?"
host_dfbBilling = dfb_billing_url + "/getBillingList?"
host_dfbBillingDetail = dfb_billing_url + "/getBillingDetail?"
host_dfbRedu = dfb_billing_url + "/getReductionLateFees?"
host_goods = dfb_trade_url + "/tx/staging/getStageOrders?"
host_destCard = dfb_trade_url + "/tx/getTxById/"
host_salaryList = base_new_url + "/salary/index/driver-salary-list"
host_cargo_login = base_new_url + "/user/cargo-login/login"
host_getVerify_code = base_new_url + "/user/cargo-login/get-verify-code"
host_login_history = base_new_url + "/user/cargo-login/device-login-history?"
host_device_list = base_new_url + "/user/cargo-login/device-list?"


"""轻易贷接口自动化测试"""
host_addMore_pledge = base_qyd_url + "entrance/account/wbbatchaddpledgedetail/json"
host_addSingle_pledge = base_qyd_url + "/entrance/account/wbaddpledgedetail/json"
host_addAnLogin_pledge = base_qyd_url + "/entrance/external/syslogin/externalauthorization/json" #登录质押
host_addAnNew_pledge = base_qyd_url + "/entrance/account/wbaddpledgedetail/json" #新建质押
host_addAnNew_pledge_stg = base_qyd_urlstg + "/entrance/account/wbaddpledgedetail/json" #新建质押stg
qydManageLoginUrl="https://www.localqyd.com/entrance/external/syslogin/externalauthorization/json?username=DFBXT&password=987654321" #轻易贷管理台登录
qydManageLoginUrl_stg="https://www.stg-qyd.com/entrance/external/syslogin/externalauthorization/json?username=DFBXT&password=987654321" #stg轻易贷管理台登录
qydSumpledgeAmountUrl = "https://www.localqyd.com/entrance/account/wbqueryuseramountdetail/json" #用户质押总额、总资产、可被质押、可出账金额
qydSumpledgeAmountUrl_stg = "https://www.stg-qyd.com/entrance/account/wbqueryuseramountdetail/json" #stg用户质押总额、总资产、可被质押、可出账金额

"""轻易贷实名注册"""
qydautoregistuserforpcUrl=base_url+"/entrance/register/autoregistuserforpc/json"#其他平台注册{"telNum":"16825564444","phoneCheckNo":"0000","userType":"0","ssoId":"1358794811195489649"}
qydregisterusermobileUrl = base_url+"/register/usermobile/validator"#手机号码唯一性校验====废弃
qydregisterUrl = base_url+"/register"#轻易贷注册
qydregisterSendUrl = base_url+"/register/rest/message"#注册发送验证码(其他平台){"validateKey":83,"type":"2","telNum":"16825564444","autoCode":"0000"}
qydregisterPhotoUrl = base_url+"/entrance/user/getcodeimage/stream?validateKey="#图片验证
qydregisterPhotoUrldoc = "https://ult-www.qingyidai.com/entrance/user/getcodeimage/stream?validateKey="#图片验证
qydPersonIdentificationUrl = base_url+"/entrance/security/pcpersononekeycontract/json"#个人实名认证接口
qydPersonIdentificationUrldoc = "https://ult-www.qingyidai.com/entrance/security/pcpersononekeycontract/json"#个人实名认证接口
qydregisterSendMsgUrl = base_url+"/entrance/qyduser/registerSendMsg/json"#注册发送短信验证码接口

qydcompanyAuthenticationUrl = base_url+"/entrance/user/companyAuthentication/json" #企业实名认证接口


"""垫付宝管理台企业接口"""
dfb_patch="http://www.local-kaiyuan.com/backend-member/authenticate/patch/_/"#企业认证审核下单
dfb_put="http://www.local-kaiyuan.com/backend-member/authenticate/put/_/"#企业认证确认页

"""轻易贷企业实名认证模拟交易网关打款"""
qydcashresultUrl="http://api-kypay.local-kaiyuan.com/kypay/cashresult"#模拟成功
qydcheckandopenaccountUrl=base_url+"/entrance/user/checkandopenaccount/json"#确认打款金额
qydbankresultUrl_QA="https://ult-paycenter-web-api.qingyidai.com/paycenter/bankinfoverify/bankresult"#银行卡模拟成功

"""轻易贷平台借款"""
qydgetcodeimage=base_url+"/entrance/user/getcodeimage/stream?validateKey="#获取绑定垫付宝账户验证码图片
qydkypayaccountstatistics1=base_url+"/entrance/account/kypayaccountstatistics/json"#发送验证码
qydkypayaccountstatistics2=base_url+"/entrance/account/kypayaccountstatistics/json"#绑定成功

host_qyd_front_login="https://ult-www.qingyidai.com/entrance/security/login/json"


"""垫付宝ultimate环境前台登录"""
ucUserLogin = "http://dfb-user.local-kaiyuan.com/dfb/user/login"
ucUserLogin_stg = "http://dfb-user.stg-che001.com/dfb/user/login"

"""轻易贷前台请求url"""
qydFrontLoginUrl11=base_url+"/entrance/security/login/json"#轻易贷前台登录

qydFrontLoginUrl=base_url+"/entrance/qyduser/checkauthorizationlogin/json"#轻易贷前台登录

"""轻易贷获取submitToken请求"""
qydGetsubmitTokenUrl = base_url+"/entrance/mt/getSubmitToken/json"


"""购买标的url"""
qydBuymethodqyUrl = base_url+"m/entrance/mt/buyQY/json" #轻盈月盈

qydBuymethodcheckUrl = base_url+"/entrance/mt/indexinfo/json" #轻盈月盈二级市场剩余金额查询

qydBuymethodqyUrlA = base_url+"/entrance/mt/buyAssignment/json" #轻盈月盈二级市场

qydBuymethodzyUrl = base_url+"/entrance/zy/BuyZY/json" #众盈

qydBuymethodzycheckUrl = base_url+"/entrance/zy/zyRemainCanInvestAmount/json" #众盈剩余金额查询


"""薪资宝转账"""
transferAmountUrl = "http://www.localqyd.com/entrance/payment/flbsplit/json" #企业分账接口
#薪资宝
transferTokenUrl= "https://www.localqyd.com/entrance/external/syslogin/externalauthorization/json?username=JMDXT&password=987654321"
transferTokenUrl_stg= "http://www.stg-qyd.com/entrance/external/syslogin/externalauthorization/json?username=JMDXT&password=987654321"#stg登录
transferAmountUrl_stg = "http://www.stg-qyd.com/entrance/payment/flbsplit/json"#stg分账


"""轻易贷用户资产"""
accounttotalUrl = base_url+"/entrance/account/accounttotalassets/json"#用户总资产情况查询



"""代扣请求url"""
qydwbshouquanUrl = base_qyd_url + "/entrance/account/wbauthorizeplaceorder/json" #外部授权下单

qydwbquerenUrl = base_qyd_url + "/entrance/account/wbauthorizeconfirm/json" #外部授权确认

qydWithholdUrl = base_url+"/entrance/mt/withhold/json" #代扣接口1


"""垫付宝管理台登录接口"""
host_admin_login = base_dfb_url + "/login"
host_admin_login_stg = base_dfb_urlstg + "/login"
"""垫付宝管理台众盈标的挂出接口"""
host_zy_open = base_dfb_url + "/backend-qyd/loan/zy/open"
host_zy_open_stg = base_dfb_urlstg + "/backend-qyd/loan/zy/open"
"""垫付宝管理台月盈标的挂出接口"""
host_yy_open = base_dfb_url + "/backend-qyd/loan/yy/open"
host_yy_open_stg = base_dfb_urlstg + "/backend-qyd/loan/yy/open"
"""轻盈开标：借款申请，获取submitToken值接口"""
host_qy_submit_token = base_qyd_url + "/entrance/mt/getSubmitToken/json"
host_qy_submit_token_stg = base_qyd_urlstg + "/entrance/mt/getSubmitToken/json"
"""轻盈开标：借款申请接口"""
host_qy_open = base_qyd_url + "/entrance/mt/buildLoanApply/json"
host_qy_open_stg = base_qyd_urlstg + "/entrance/mt/buildLoanApply/json"
"""轻盈开标成功后：初审接口"""
host_qy_first_audit = base_dfb_url + "/backend-qyd/audit/firstAudit"
host_qy_first_audit_stg = base_dfb_urlstg + "/backend-qyd/audit/firstAudit"
"""轻盈开标成功后：初审，复审认领接口"""
host_qy_receiveTask = base_dfb_url + "/backend-qyd/receive/receiveTask"
host_qy_receiveTask_stg = base_dfb_urlstg + "/backend-qyd/receive/receiveTask"
"""轻盈开标成功后：复审接口"""
host_qy_secondAudit = base_dfb_url + "/backend-qyd/audit/secondAudit"
host_qy_secondAudit_stg = base_dfb_urlstg + "/backend-qyd/audit/secondAudit"
"""垫付宝管理台众盈标的撤销接口"""
host_zy_revoke = base_dfb_url + "/backend-qyd/loan/zy/revoke"
host_zy_revoke_stg = base_dfb_urlstg + "/backend-qyd/loan/zy/revoke"
"""月盈轻盈理财中金额计算接口"""
host_yy_amount_qy = base_qyd_url + "/entrance/mt/mtpossessioninfo/json"
host_yy_amount_qy_stg= base_qyd_urlstg + "/entrance/mt/mtpossessioninfo/json"
"""垫付宝管理台月盈标的撤销接口"""
host_yy_revoke = base_dfb_url + "/backend-qyd/loan/yy/revoke"
host_yy_revoke_stg = base_dfb_urlstg + "/backend-qyd/loan/yy/revoke"




"""新手标接口"""
xsbRemainCanInvestAmountURl = base_url+"/entrance/xsb/xsbRemainCanInvestAmount/json "#新手标剩余可投金额接口

queryXSBLoanInfoURL = base_url+"/entrance/xsb/queryXSBLoanInfo/json"#借款信息详情

xsbInvestRecordURL = base_url+"/entrance/xsb/xsbInvestRecord/json"#加入记录

transactiondetailURL = base_url+"/entrance/xsb/transactiondetail/json"#新手标交易明细查询接口

qydBuymethodxsbUrl = base_url+"/entrance/xsb/BuyXSB/json"#新手标购买

qydxsbContractDownloadURL = base_url+"/entrance/xsb/xsbContractDownload/json"#借款协议

"""新网企业注册"""
businessLicense_upload= base_url+"/entrance/user/uploadbusinesslicense/upload"#上传图片
zxzccompanyauthenticationUrl= base_url+"/entrance/qyduser/companyauthentication/json"#中信企业注册
xwzclianxirenUrl= base_url+"/entrance/qyduser/companyContactMessageCode/json"#联系人验证码
qydbankresultUrl=""



#查询锁定总金额和可提现金额
getlockamountandfrozenamount_QA = base_url + "/entrance/account/getlockamountandfrozenamount/json"
#账户总览
accountinfo_QA = base_url + "/entrance/account/accountinfo/json"


def md5(strs):
    import hashlib
    m = hashlib.md5()
    m.update(strs.encode(encoding='UTF-8'))
    return m.hexdigest()
