# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# import json

# class JokespiderPipeline(object):
#     def __init__(self):
#         self.fp = open("joke.json",'w',encoding='utf-8')

#     def open_spider(self,spider):
#         print("开始爬取")

#     def process_item(self, item, spider):
#         item_json = json.dumps(dict(item),ensure_ascii=False)
#         self.fp.write(item_json+'\n')
#         return item
    
#     def close_spider(self,spider):
#         self.fp.close()
#         print("结束爬取")

# scrapy自带的导出器
# from scrapy.exporters import JsonItemExporter
# class JokespiderPipeline(object):
#     def __init__(self):
#         self.fp = open("joke.json",'wb')
#         self.exporters = JsonItemExporter(self.fp,ensure_ascii=False,encoding="utf-8")
#         self.exporters.start_exporting()

#     def open_spider(self,spider):
#         print("开始爬取")

#     def process_item(self, item, spider):
#         self.exporters.export_item(item)
#         return item
    
#     def close_spider(self,spider):
#         # JsonItemExporter先将数据写在内存中，当调用finish_exporting方法后才将数据一次性写入json中
#         self.exporters.finish_exporting()
#         self.fp.close()
#         print("结束爬取")

# JsonLinesItemExporter时一行一行的写入
from scrapy.exporters import JsonLinesItemExporter
class JokespiderPipeline(object):
    def __init__(self):
        self.fp = open("joke.json",'wb')
        self.exporters = JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding="utf-8")

    def open_spider(self,spider):
        print("开始爬取")

    def process_item(self, item, spider):
        self.exporters.export_item(item)
        return item
    
    def close_spider(self,spider):
        self.fp.close()
        print("结束爬取")


