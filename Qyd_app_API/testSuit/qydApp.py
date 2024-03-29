# -*- coding: utf-8 -*-
import unittest
import os
import time
from lib import HTMLTestRunner3
#from lib import send_email
import zipfile, os.path
import sys
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#E:\\Pycharmfile\\Qyd_app_API
sys.path.append(basedir)


"""unittest.defaultTestLoader(): defaultTestLoader()类，
通过该类下面的discover()方法可自动根据测试目录start_dir匹配查找测试用例文件（test*.py），
并将查找到的测试用例组装到测试套件，因此可以直接通过run()方法执行discover"""
suite = unittest.defaultTestLoader.discover(basedir + '/APItest', pattern='*.py')
filePath = basedir + "/report/Report.html"
fp = open(filePath, 'wb')

"""生成报告的Title,描述"""
runner = HTMLTestRunner3.HTMLTestRunner(stream=fp, title='轻易贷app需求调整相关接口【QA环境】接口测试报告', description='测试用例执行结果如下所示')
runner.run(suite)
fp.close()
#unittest.TextTestRunner(verbosity=2).run(suite)