#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__="项目根目录"

from sanic import Sanic
from sanic.response import text

app = Sanic(__name__)


@app.route("/")
def hello(request):
    return text("dog")


if __name__ == "__main__":
    app.run()
