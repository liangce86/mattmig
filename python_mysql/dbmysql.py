#!/usr/bin/env python
#coding:utf8
#author:liangce
import os,re,sys,datetime
import MySQLdb

class dbmg(object):
      def dbsinfo(self,bhost,bport,buser,bpassword,bdatabase1,bdatabase2,bdatabase3):
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
          conn = MySQLdb.connect(host=self.bhost,port=self.bport,user=self.buser,passwd=self.bpassword,db=self.bdatabase1)
          cur  = conn.cursor()
          sql = "select * from product"
          results = cur.execute(sql)
          #aa = cur.fetchmany(results)
          cur.close()
          conn.commit()
          conn.close()
          print(results)
          #for data in aa:
          #     print(data)

test = dbmg()
test.dbsinfo('192.168.0.82',3306,'ccc','jys#123','mmm','test','video')
test.checkmysql()
