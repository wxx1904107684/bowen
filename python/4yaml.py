#!/usr/bin/python
#-*-coding:utf8-*-
import yaml
with open('w.yaml','r') as file:
    wx=yaml.load(file,Loader=yaml.FullLoader)

print(wx)
print(wx['platformVersion'])