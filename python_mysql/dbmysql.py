#!/usr/bin/env python
#coding:utf8
#author:liangce
import os,re,sys,datetime
import MySQLdb
from getpass import getpass

class dbmg(object):
      def __init__(self,bhost='',bport='',buser='',bpassword='',bdatabase1='',bdatabase2='',bdatabase3=''):
          if not bhost:
              bhost = (input("请输入源库地址：")).strip()
          if not bport:
              while True:
                  try:
                        bport = int(input("请输入源库端口："))
                        break
                  except:
                        print("请输入数字格式")
          if not buser:
              buser = (input("请输入迁移账号：")).strip()
          if not bpassword:
              bpassword = getpass("请输入迁移账号密码: ") 
          if not bdatabase1:
              bdatabase1 = (input("请输入迁移库名1: ")).strip()
          if not bdatabase2:
              bdatabase2 = (input("请输入迁移库名2: ")).strip()
          if not bdatabase3:
              bdatabase3 = (input("请输入迁移库名3: ")).strip()

          self.bhost = bhost
          self.bport = bport
          self.buser = buser
          self.bpassword = bpassword
          self.bdatabase1 = bdatabase1
          self.bdatabase2 = bdatabase2
          self.bdatabase3 = bdatabase3

      def dbrinfo(self,rhost,rport,ruser,rpassword):
          self.rhost=rhost
          self.rport=rport
          self.ruser=ruser
          self.rpassword = rpassword

      def checkmysql(self):
          try:
              conn = MySQLdb.connect(host=self.bhost,port=self.bport,user=self.buser,passwd=self.bpassword)
          except:
              print("源库连接信息错误，退回重填！")
              pass
          cur  = conn.cursor()
          sql = "SELECT information_schema.SCHEMATA.SCHEMA_NAME FROM information_schema.SCHEMATA where SCHEMA_NAME=\'{db}\';".format(db=self.bdatabase1)
          results = cur.execute(sql)
          if not results:
               print('查无此库')
          data = cur.fetchmany(results)
          cur.close()
          conn.commit()
          conn.close()
          for row in data:
             row = row[0] 
             print(row)
             print(self.bdatabase1)
             if row == self.bdatabase1:
                  print('源库名正确')
test = dbmg()
test.checkmysql()
