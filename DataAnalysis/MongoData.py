#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__="获取mongodb里的数据"

from motor.motor_asyncio import AsyncIOMotorClient as AIOM


class Init_Mongo:
    """获取mongo连接实例"""
    @staticmethod
    def getCol(doc, col):
        client = AIOM('mongodb://47.94.12.59:27017')
        db = client[doc]
        collection = db[col]
        return collection


async def getData(doc, col):
    """取数返回生成器"""
    c = Init_Mongo.getCol(doc, col)
    r = [''.join(document['title']) async for document in c.find({})]
    return r

