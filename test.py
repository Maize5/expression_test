#!/usr/bin/env python3
#-*- coding:utf-8 -*-
days = int(input("Enter days: "))
months = days // 30
days = days % 30
print("Months = {} Days = {}".format(months, days))
