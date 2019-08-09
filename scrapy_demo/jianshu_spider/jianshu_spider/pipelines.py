# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
# 导入twisted的异步插入数据库的模块
from twisted.enterprise import adbapi
from pymysql import cursors


class JianshuSpiderPipeline(object):
    def __init__(self):
        dbparams = {
            'host': '127.0.0.1',
            'port': int('3306'),
            'user': 'root',
            'password': '',
            # 填写数据库密码
            'database': 'jianshu',
            'charset': 'utf8'
        }
        # 创建一个数据库连接
        self.conn = pymysql.connect(**dbparams)
        # 获取游标
        print("12345")
        self.cursor = self.conn.cursor()
        self._sql = None
        print("45677")

    def process_item(self, item, spider):
        self.cursor.execute(self.sql, (item['title'], item['content'], item['author'],
                                       item['avatar'], item['pub_time'], item['origin_url'], item['article_id']))
        # 涉及写的操作需要提交
        self.conn.commit()
        return item

    @property
    def sql(self):
        # 要执行的sql语句
        if not self._sql:
            self._sql = """
            insert into article(id,title,content,author,avatar,pub_time,origin_url,article_id) 
            values(null,%s,%s,%s,%s,%s,%s,%s)
            """
            return self._sql
        return self._sql


class JianshuTwistedPipeline(object):
    def __init__(self):
        dbparams = {
            'host': '127.0.0.1',
            'port': int('3306'),
            'user': 'root',
            'password': '102442klklkl',
            'database': 'jianshu',
            'charset': 'utf8',
            # 提供一个游标
            'cursorclass': cursors.DictCursor
        }
        # 通过Twisted框架提供的容器连接数据库
        self.dbpool = adbapi.ConnectionPool('pymysql', **dbparams)
        self._sql = None

    @property
    def sql(self):
        # 要执行的sql语句
        if not self._sql:
            self._sql = """
                insert into article(id,title,content,author,avatar,pub_time,origin_url,article_id) 
                values(null,%s,%s,%s,%s,%s,%s,%s)
                """
            return self._sql
        return self._sql

    def process_item(self,item,spider):
        # 使用twisted方法runInteraction来异步导入数据库
        defer = self.dbpool.runInteraction(self.insert_item,item)
        defer.addErrback(self.handle_error,item,spider)
    
    def insert_item(self,cursor,item):
        # ajaxh获得的字段没有存储，简单的添加一下就行了
        cursor.execute(self.sql, (item['title'], item['content'], item['author'],
        item['avatar'], item['pub_time'], item['origin_url'], item['article_id']))
    
    def handle_error(self,error,item,spider):
        print("***"*30)
        print(error)
        print("***"*30)