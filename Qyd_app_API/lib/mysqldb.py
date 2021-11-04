# -*- coding: utf-8 -*-
import pymysql.cursors
import pymysql
from lib.log import logger
from Config import config
import importlib,sys
importlib.reload(sys)


class mysqldb(object):
    def __init__(self, dbName):
        if dbName == "front":
            self.conn = config.front
        elif dbName == "account":
            self.conn = config.account
        elif dbName == "ucenter":
            self.conn = config.ucenter
        elif dbName == "qydproduction":
            self.conn = config.qydproduction
        elif dbName == "qydaccount":
            self.conn = config.qydaccount
        elif dbName == "che001":
            self.conn = config.che001_wl
        elif dbName == "qydnewproduction":
            self.conn = config.qydnewproduction
        else:
            pass

    def selectsql(self, sql):
        con = pymysql.connect(**self.conn)
        cursor = con.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        con.close()
        return data

    def updatesql(self, sql):
        conn = pymysql.connect(**self.conn)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        try:
            cursor.execute(sql)
            # logger.info(sql)
            conn.commit()
        except Exception as e:
            conn.rollback()
            logger.error(e.message)


    def insert(self,sql):
        db = pymysql.connect(**self.conn)

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()


"""以上三种方法足以进行mysql的查询和更新操作---最新框架"""





