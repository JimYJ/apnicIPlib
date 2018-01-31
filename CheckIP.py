#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2018-1-30

@author: jim
'''

from WriteFile import * 
from Mysql import * 

class CheckIP:
    
    CN = 0
    overseas = 0
    writefile = WriteFile()
    MaxCount = 0
    
    def __call__(self): 
        self.CheckIP()
        
        
    def CheckIP(self):
        images = open("delegated-apnic-latest.txt")
        for line in images.readlines():
            list = line.split("|")
            if list[2] =="ipv4":
                if int(list[4])>self.MaxCount:
                    self.MaxCount = int(list[4])
                    print self.MaxCount
                self.getAllIP(list[4], list[3], list[1]+"-IP", list[1], list[6],mysql)
#                 if list[1] !="CN":
#                     temp = list[3]+"-"+list[4]+"-"+list[1]+"-"+list[6]
#                     self.getAllIP(list[4], list[3], "overseas-IP", list[1], list[6])
            print list
        images.close()
        print self.MaxCount
        
    def getAllIP(self,count,startIP,filename,area,status,mysql):
        d = int(count)/256
        i = 0
        iparr = startIP.split('.')
        tempB = iparr[2]
        while(i < d):
            iparr[2]=str(i + int(tempB))
            if int(iparr[2])>255:
                iparr[1] = str(int(iparr[1]) + 1)
                if iparr[1] >255:
                    iparr[0] = str(int(iparr[0]) + 1)
                    iparr[1] = "0" 
                iparr[2] = "0" 
                tempB = "0" 
                i = 0
                d  = d - 256
            print iparr
            startIP = '.'.join(iparr)
            iparr[3]="255"
            endIP = '.'.join(iparr)
            temp = startIP+"-"+endIP+"-"+area+"-"+status
            self.writefile.append(filename, temp)
			#如果需要写入数据库，可在这里插入
            iparr[3]="0"
            i += 1
            
           
cI = CheckIP()
cI()
        
