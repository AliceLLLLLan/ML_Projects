#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:26:06 2019

@author: AliceLan
"""

from flask import flask

app = flask(_name_)

#app.route("/hello")
#定义网址url

def hello():
    return "hello world!"
#定义你要run的内容
if _name_ == "_main_":
    app.run()
#当运行主程序的时候，运行app