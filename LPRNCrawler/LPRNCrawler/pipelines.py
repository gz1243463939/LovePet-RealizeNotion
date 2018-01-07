# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo
from datetime import datetime
import threading
client=pymongo.MongoClient(host='127.0.0.1',port=27017)
db=client['scrapy_data']['tianya']

class TYPipeline(object):

    def process_item(self,item ,spider):
        with open('tianya——养宠心情.txt','a') as f:
            f.write(str(item))
            f.write('\n')
