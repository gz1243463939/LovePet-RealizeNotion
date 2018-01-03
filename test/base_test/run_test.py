#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__="测试程序运行情况"

from nose.tools import assert_equal, with_setup
import subprocess
import aiohttp
import asyncio


def start():
    """启动程序"""
    subprocess.Popen(
        "pipenv run python /home/linhanqiu/LovePet-RealizeNotion/backend/LovePet-RealizeNotion/__init__.py",
        shell=True)


def end():
    """杀掉程序"""
    subprocess.Popen(
        "kill -9 $(ps -aux|grep pipenv |grep -v grep |awk '{print $2}')",
        shell=True)


@with_setup(start, end)
async def test_run():
    async with aiohttp.request("get", "http://127.0.0.1:8000/") as r:
        assert_equal(200, r.status)
loop = asyncio.get_event_loop()
loop.run_until_complete(test_run())
loop.close()
