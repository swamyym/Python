# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 12:25:11 2017

@author: 503001041
"""

import sys
import math

if __name__ == "__main__":
    n = int(input().strip())
    m = int(input().strip())
    vol_loc=[]
    vol_pow=[]
    power_list=[]
    for a0 in range(m):
        x, y, w = input().strip().split(' ')
        x, y, w = [int(x), int(y), int(w)]
        vol_loc.append([x,y])
        vol_pow.append(w)
    for x in range(n):
        for y in range(n):
            if [x,y] in vol_loc:
                power_list.append(vol_pow[vol_loc.index([x,y])])
            else:
                power_list.append(0)
    power_list = [power_list[i:i+n] for i in range(0,len(power_list),n)]
    
    
    
    
    
    
    for i in range(len(vol_pow)):
        x,y = vol_loc[i]
        
        a= 0
        for powchange in range(vol_pow[i]-1,0,-1):
        
            a=a+1 
            if a>= math.log(n,2):
                break
            for j in range(-a,a+1):
                for k in range(-a,a+1):
                    if j == a or k == a or j == -a or k == -a:
                        try:
                            power_list[x+j][y+k]= power_list[x+j][y+k]+powchange
                        except:
                            continue
                    else:                        
                        continue
                            
            