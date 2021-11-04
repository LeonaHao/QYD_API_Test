import  json
import os,os.path
def params():
    data = {
    "submitToken": "",
    "amount":"200",
    "terminal":"01"
}
    #data1 = data.copy()
    data.pop('submitToken')
    print(data)

    a=os.path.abspath(__file__)
    print("a",a)

    basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print("basedir",basedir)

params()