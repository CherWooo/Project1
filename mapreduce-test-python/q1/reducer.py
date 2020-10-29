#!/usr/bin/env python
# coding: utf-8

import sys
from operator import itemgetter


with open("test.txt", "r") as f:  
    data = f.read()
#print(data)
   
dict_vtime_count = {}

for line in data:
    line = line.strip()
    print(line)
    vtime, count = line.split()
    try:
        count = int(count)
        dict_vtime_count[vtime] = dict_vtime_count.get(vtime, 0) + count
        
    except ValueError:
        pass

print(dict_vtime_count)      
  
sorted_dict_vtime_count = sorted(dict_vtime_count.items(), key=itemgetter(1))[::-1]

for vtime, count in sorted_dict_vtime_count:
    print (vtime, count)