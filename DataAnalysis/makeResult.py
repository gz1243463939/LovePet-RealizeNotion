#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__="聚合数据，分析结果"

from DataAnalysis.MongoData import getData

import asyncio
l = asyncio.get_event_loop()
r = l.run_until_complete(getData('tianya', 'chongmixuetang'))
print(r)

class Meta(type):
    def __new__(cls, name, bases, attrs):
        try:
            import uvloop
            asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
        except Exception as e:
            print(e)
        attrs['loop'] = asyncio.get_event_loop()
        return type.__new__(cls, name, bases, attrs)

class MakeResult(metaclass=Meta):
    """取出数据 -》 数据分词 -》
    1.统计言论中词频
    2.统计提到动物的词的数量
    """
    def __init__(self, **kw):
        pass
    @classmethod
    def p(cls):
        print(cls.loop)
MakeResult.p()