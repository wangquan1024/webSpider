# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter

class SfwSpiderPipeline(object):
    def __init__(self):
        # self.newhouse_fp = open('newhouse.json','wb')
        self.esf_fp = open('esfhouese.json','wb')
        # self.newhouse_exports = JsonLinesItemExporter(self.newhouse_fp,
        # ensure_ascii=False)
        self.esf_exports = JsonLinesItemExporter(self.esf_fp,ensure_ascii=False)

    def process_item(self, item, spider):
        # self.newhouse_exports.export_item(item)
        self.esf_exports.export_item(item)
        return item

    def close_spider(self,spider):
        # self.newhouse_fp.close()
        self.esf_fp.close()
