#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017-11-22

@author: jim
'''
class WriteFile:
    
    def append(self,filename,content):
        try:
            f=open("ip\\"+filename+'.txt','a')
            f.write(content)
#             f.write('|')
#             f.write('\n')
        finally:
            f.close()
        
        
    def cover(self,filename,content):
        try:
            f=open(filename+'.txt','w')
            f.write(content)
#             f.write('\n')
        finally:
            f.close()