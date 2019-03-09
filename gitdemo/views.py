#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 19:05
# @Author  : Feeling
# @Email   : 2301270877@qq.com
# @File    : views.py
# @Software: PyCharm
from django.http import HttpResponse


def index_view(request):
    return HttpResponse('hello git!')