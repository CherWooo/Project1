#!/usr/bin/env python
# coding: utf-8

import sys
from operator import itemgetter

dict_vtime_count = {}

for line in sys.stdin:
    line = line.strip()
    line = line.split()
    vtime=line[0]
    count=line[-1]
    try:
        count = int(count)
        dict_vtime_count[vtime] = dict_vtime_count.get(vtime, 0) + count
        
    except ValueError:
        pass

print(dict_vtime_count)      
  
sorted_dict_vtime_count = sorted(dict_vtime_count.items(), key=itemgetter(1))[::-1]

for vtime, count in sorted_dict_vtime_count:
    print (vtime, count)
