# coding:utf-8
# Author: Candy
import os
from lib import readexceldata
datapath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')


"""类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称"""
def __generateTestCases (instanse, inerfaceName, tesDataName, sheetName):
    file = os.path.join(datapath, tesDataName)
    data_list = readexceldata.excel_to_list(file, sheetName)
    num=0
    for i in range(len(data_list)):
        num += 1
        #setattr(instanse, 'test_'+inerfaceName+'_%s' % (str(data_list[i]["tc_num"])), instanse.getTestFunc(data_list[i]))
        setattr(instanse, 'test_'+'_%s' % num,instanse.getTestFunc(data_list[i]))
    #print(data_list)

