#app服务地址QA
qyd_base_url_QA="https://ult-mobile-app.qingyidai.com/nw"

#轻易贷app获取token请求url docker
appgetToken_QA=qyd_base_url_QA+"/entrance/apis/account/apptoken/json"

#轻易贷app获取submitToken请求url
appgetsubmittoken_QA=qyd_base_url_QA+"/entrance/apis/mt/getsubmittoken/json"

#轻易贷app登录url docker
applogin_QA=qyd_base_url_QA+"/entrance/apis/device/checkauthorizationlogin/json"

#退出登录并清除token
applogout_QA =qyd_base_url_QA+"/entrance/apis/account/applogout/json"

#一级市场购买
buyloannmt_QA = qyd_base_url_QA + "/entrance/apis/newmt/buyloannmt/json"


#新月盈、新月盈优选计算器接口
newincomecalculator_QA = qyd_base_url_QA+"/entrance/apis/newmt/incomecalculator/json"

#开启和关闭预约理财接口【兼容之前的理财产品】
openclosewithappointment_QA = qyd_base_url_QA+"/entrance/apis/newmt/openclosewithappointment/json"

#【查询】新月盈、新众盈、新月盈优选产品详情
remainamount_QA = qyd_base_url_QA + "/entrance/apis/newmt/remainamount/json"

#查询新月盈、新众盈-预期收益
getAppreciationAmount_QA = qyd_base_url_QA + "/entrance/apis/newmt/getAppreciationAmount/json"

#获取众盈投资中债权回款明细
getZyPossessionDetail_QA = qyd_base_url_QA + "/entrance/apis/newmt/getZyPossessionDetail/json"

#新月盈、新众盈计算器信息展示接口
nwcalculatorinfoshow_QA = qyd_base_url_QA + "/entrance/apis/newmt/nwcalculatorinfoshow/json"

#获取预约理财状态【兼容老版本】
nwgetappointmentstatus_QA = qyd_base_url_QA + "/entrance/apis/newmt/nwgetappointmentstatus/json"

#【合同范本展示】《债权转让协议》《借款协议》《复投服务协议》接口
nwprotocolcontractmodel_QA = qyd_base_url_QA + "/entrance/apis/newmt/nwprotocolcontractmodel/json"

#【新增新众盈、新月盈、新手标】 获取首页信息(接口改造合并，首页置顶)
getuserinformation_QA = qyd_base_url_QA + "/entrance/apis/register/getuserinformation/json"

#新月盈管理、新众盈管理、新手标管理
nwfinancialmanage_QA = qyd_base_url_QA + "/entrance/apis/newmt/nwfinancialmanage/json"

#新众盈转让处理中接口
nwzytransferoutprocessinginfo_QA = qyd_base_url_QA + "/entrance/apis/newzy/nwzytransferoutprocessinginfo/json"

#新月盈、新众盈撤资确认接口
dinvestmentdo_QA = qyd_base_url_QA + "/entrance/apis/newmt/dinvestmentdo/json"

#开启、关闭复投
openclosereinvest_QA = qyd_base_url_QA + "/entrance/apis/newmt/openclosereinvest/json"

#获取众盈所有回款计划列表
getZyBackMoneyPlan_QA = qyd_base_url_QA + "/entrance/apis/newzy/getZyBackMoneyPlan/json"

#获取众盈持有中债权列表
getZyPossession_QA = qyd_base_url_QA + "/entrance/apis/newmt/getZyPossession/json"

#获取可提现金额
withdrawalamount_QA = qyd_base_url_QA + "/entrance/apis/account/withdrawalamount/json"

#【查询】新手标、新月盈、新众盈投资处理中金额
investinhand_QA = qyd_base_url_QA + "/entrance/apis/newmt/investinhand/json"

#新月盈、新众盈、新手标标的组成
nwgetloanlist_QA = qyd_base_url_QA + "/entrance/apis/newmt/nwgetloanlist/json"

#预约理财-立即预约接口
zyBuyZYWithAppointment_QA = qyd_base_url_QA + "/entrance/apis/zy/zyBuyZYWithAppointment/json"

#轻盈A秒杀购买展示页面
secondkillbuyshow_QA = qyd_base_url_QA + "/entrance/apis/miaosha/secondkillbuyshow/json"

#轻盈A秒杀标的组成接口
getqyskloanlist_QA = qyd_base_url_QA + "/entrance/apis/miaosha/getqyskloanlist/json"

#轻盈A秒杀加入记录接口
getactivityjoinrecord_QA = qyd_base_url_QA + "/entrance/apis/miaosha/getactivityjoinrecord/json"

#新月盈、新众盈、新手标加入记录、转让记录接口
nwpossessionorderlist_QA = qyd_base_url_QA + "/entrance/apis/newmt/nwpossessionorderlist/json"

#查询风险评测等级信息接口
queryRiskAssess_QA = qyd_base_url_QA + "/entrance/apis/finder/queryRiskAssess/json"

#自动升级风险评测等级
updateRiskAssess_QA = qyd_base_url_QA + "/entrance/apis/finder/updateRiskAssess/json"

#查询风险评测状态
queryRiskResult_QA = qyd_base_url_QA + "/entrance/apis/finder/queryRiskResult/json"

#保存风险评测结果
saveRiskResult_QA = qyd_base_url_QA + "/entrance/apis/finder/saveRiskResult/json"

#新月盈、新众盈正常还款/提前还款交易明细
queryrepaytransactiondetail_QA = qyd_base_url_QA + "/entrance/apis/account/queryrepaytransactiondetail/json"

#新月盈、新众盈违约还款交易明细
getdetailbytransactionid_overdue_QA = qyd_base_url_QA + "/entrance/apis/newmt/getdetailbytransactionid/json"

#【查询】轻盈交易明细app
getDetailByTransactionId_QA = qyd_base_url_QA + "/entrance/apis/mt/getDetailByTransactionId/json"