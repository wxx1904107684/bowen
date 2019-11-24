#!/usr/bin/python
#-*-coding:utf8-*-
# 不限制平台，os本意是操作系统的意思
import os
print(os.name)
#显示nt，代表windows
# 显示当前文件所在路径
# a=os.getcwd()
# print(a)
# delete=os.remove('wxx.py')#或（r'c:\python\b.txt'）删除本目录下路径的文件
# 只能能删除空目录 ，不能是有文件的目录
# delete=os.remove('%.xls')
#（a)或直接括号()或('..')，其中('.'),(),(a)效果一样，显示当前目录下的所有文件
list=os.listdir('.')
#返回指定路劲下的所有文件和目录名，括号里相对路径和文件路径
# print(list)
# for i in list:
#     if i.endswith('.xls'):
#         os.remove(i)
# 删除指定路径下的递归目录
# delete_dir=os.removedirs(r'11\22\33')
# 删除单级目录
# delete_dir=os.remove('qqq')
# dir=os.mkdir('qwe')
# 创建递归目录
# dirs=os.makedirs(r'111\222\333')
# import time
# time.sleep(20)
# delect_dir=os.removedirs(r'111\222\333')
# 判断指定路径下的名称是不是文件，是文件显示True,目录显示False
# a=os.path.isfile('111')
# print(a)
#判断指定路径下的名称是不是目录,是目录显示True,文件显示False
# b=os.path.isdir('111')
# print(b)
# 判断文件或目录是否存在
# bb=os.path.exists('1111')
# print(bb)
# 1将路径分割成路径名和文件名
c=os.path.split(r'C:\Users\wxx\PycharmProjects\untitled\wangxue\111')
print(c)
# 12连接目录与文件名或目录
cc=os.path.join(r'C:\Users\wxx\PycharmProjects\untitled\wangxue','111')
print(cc)
