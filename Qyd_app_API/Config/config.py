# -*- coding:utf-8 -*-
import os
import logging
import pymysql

#已购买新手标
#tel_num ="16871799750"
#tel_num = '16871785205'


#tel_num = '16871736310'

tel_num = '16871725120'
username = '16871725120'
#新注册号码：
#tel_num = '16871733335'

#质押账号
#tel_num = '16820090704'
#tel_num = '16871718310'

#借款账号
#tel_num = '16871766035'


#tel_num = '16871760205'
passwd = 'che001'

#私人账号
username_dwh = '16850000131'
passwd_dwh = 'che009'


"""qydnewproduction"""
qydnewproduction = dict(host='192.168.214.120', user='platform', passwd='platform2018', db='qydnewproduction', charset='utf8', cursorclass=pymysql.cursors.DictCursor)

"""qydproduction"""
qydproduction = dict(host='192.168.214.120', user='platform', passwd='platform2018', db='qydproduction', charset='utf8', cursorclass=pymysql.cursors.DictCursor)


"""邮件配置"""
sender = 'commqa@kaiyuan.net'
receiver = 'zengjuan@kaiyuan.net'
"""登陆邮箱的用户名"""
emailusername = 'commqa@kaiyuan.net'
"""登陆邮箱的授权码"""
emailpassword = '7VF6dCBEmj'

server = 'mail.kaiyuan.net'

"""数据目录"""
datapath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')

"""项目配置"""
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

"""日志配置"""
logpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'log')
# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%y-%m-%d %H:%M',
                    filename=os.path.join(logpath, 'log.txt'),
                    filemode='a')
