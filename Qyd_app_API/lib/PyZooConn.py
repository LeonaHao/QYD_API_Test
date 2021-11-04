# -*- coding:utf-8 -*-
__author__ = 'zhangmanman'

from kazoo.client import KazooClient


class PyZooConn(object):
    # init function include connection method
    def __init__(self):
        self.zk = KazooClient(hosts='192.168.214.56:9091',timeout=10000)
        self.zk.start()

        # get node data

    def get_data(self, param):
        result = self.zk.get(param)
        print(result)

        # create a node and input a value in this node

    def create_node(self, node, value):
        self.zk.create(node, value)


        # close the connection

    def close(self):
        self.zk.stop()

    ''''' 
    Hypothesis there is a bunch of methods here haha :) 
    '''


if __name__ == '__main__':
    pz = PyZooConn()
    #pz.create_node("/test", "a value")
    pz.get_data("/")
    #pz.close()