#!/usr/bin/python
# encoding:utf-8
import re
# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
# 程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母

week={'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'}
letter=raw_input("first letter:")



