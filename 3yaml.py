#!/usr/bin/python
#-*-coding:utf8-*-
import yaml
data={
    'platformname':'Android',
    'platformversion':'5.1.1',
    'devicename':'127.0.0.1:62001',
    'appPackage':'com.tal.kaoyan',
    'appActivity':'com.tal.kaoyan.ui.activity.SplashActivity',
    # 'noReset':false
    }
print(yaml.dump(data))