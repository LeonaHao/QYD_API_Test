import unittest
import os
import time
import zipfile, os.path
import sys
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)
from lib import HTMLTestRunner3
from lib import send_email


print(basedir)
"""unittest.defaultTestLoader(): defaultTestLoader()类，
通过该类下面的discover()方法可自动根据测试目录start_dir匹配查找测试用例文件（qyd_usermodel*.py），
并将查找到的测试用例组装到测试套件，因此可以直接通过run()方法执行discover"""
suite = unittest.defaultTestLoader.discover(basedir + '/APItest/Nwproduct', pattern='*.py')
filePath = basedir + "/report/Report.html"
fp = open(filePath, 'wb')

"""生成报告的Title,描述"""
runner = HTMLTestRunner3.HTMLTestRunner(stream=fp, title='【QA环境】移动端新产品：接口测试报告', description='测试用例执行结果如下所示')
runner.run(suite)
fp.close()
# unittest.TextTestRunner(verbosity=2).run(suite)


def cr_zip(zfname, fpath):
    """将basedir + '/report/'目录下的文件压缩成.zip格式的文件"""
    filelist = []
    isfp = os.path.basename(fpath)
    if isfp:
        print('%s is not path' % fpath)
        sys.exit(0)
    else:
        for root, subdirs, files in os.walk(fpath):
            for file in files:
                filelist.append(os.path.join(root, file))

    zf = zipfile.ZipFile(zfname, 'w', zipfile.ZIP_DEFLATED)
    for f in filelist:
        zf.write(f)
    zf.close()

cr_zip('Qyd_app_API_Report.zip', basedir + '/report/')
time.sleep(5)
send_email.send_mail_report("【QA环境】移动端新产品：接口测试报告")

