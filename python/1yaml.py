#!/usr/bin/python
#-*-coding:utf8-*-
import yaml
with open('x.yaml','r')as file:
    data=yaml.load(file,Loader=yaml.FullLoader)

# print(data)
print(data['name'])
print(data['wife']['age'])
print(data['child'][0]['name'])