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
              bport = int(input("请输入源库端口："))     
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
          #print(self.bhost)
          #print(self.bport)
          #print(self.buser)
          #print(self.bpassword)
          conn = MySQLdb.connect(host=self.bhost,port=self.bport,user=self.buser,passwd=self.bpassword,db=self.bdatabase1)
          cur  = conn.cursor()
          sql = "select * from usertb"
          results = cur.execute(sql)
          #aa = cur.fetchmany(results)
          cur.close()
          conn.commit()
          conn.close()
          print(results)
          #for data in aa:
          #     print(data)
test = dbmg()
test.checkmysql()
