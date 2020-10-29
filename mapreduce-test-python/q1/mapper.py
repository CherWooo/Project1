# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 01:11:34 2020

@author: Cher
"""
import re
import sys

f = open('test.csv','r',encoding='utf-8')

for line in f:
    line = line.strip()
    vtime = line.split(",")[19]
    
    if vtime != "Violation Time":
        print(vtime,1)
              
    elif vtime == "":
        print("No Record", 1)
        
