# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import ssl
from . import settings
from urllib import request
from scrapy.pipelines.images import ImagesPipeline
ssl._create_default_https_context = ssl._create_unverified_context
# 要使用urllib访问https需要关闭ssl验证

# class CarSpiderPipeline(object):
#     def __init__(self):
#         # 获取当前文件夹的地址
#         self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'images')
#         # 判断当前文件夹地址是否存在
#         if not os.path.exists(self.path):
#             # 不存在则生成新的文件夹
#             os.mkdir(self.path)

#     def process_item(self, item, spider):
#         title = item['title']
#         img_urls = item['urls']

#         dirName = os.path.join(self.path,title)
#         if not os.path.exists(dirName):
#             os.mkdir(dirName)
            
#         for img_url in img_urls:
#             image_names = img_url.split('_')[-1]
#             request.urlretrieve(img_url,os.path.join(dirName,image_names))

#         return item

# 如果使用使用scrapy自带的 ImagesPipeline的方式下载图片具体步骤如下：
# 1、在items中的XxxItem中定义 image_urls 和 images字段
# 2、在spider中将提取出来的图片链接保存到Item的 image_urls 字段中（注意：该字段接收一个可迭代对象，否则报错）
# 3、在settings文件中进行配置，具体配置见 settings.py 文件，IMIMAGES_STORE必须配置,这是用来配置存在的文件夹地址
class BwmPipeline(ImagesPipeline):
    def get_media_requests(self,item,info):
        # 发送请求之前调用，用来发送请求的
        request_objs = super(BwmPipeline,self).get_media_requests(item,info)
        for request_obj in request_objs:
            request_obj.item = item
        return request_objs

    def file_path(self, request, response=None, info=None):
        # 会在被存储之前调用，用来获取图片存储路径
        path = super(BwmPipeline,self).file_path(request,response,info)
        title = request.item.get('title')
        image_store = settings.IMAGES_STORE
        category_path = os.path.join(image_store,title)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        image_name = path.replace("full/",'')
        image_path = os.path.join(title+'/',image_name)
        return image_path