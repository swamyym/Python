# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 01:01:04 2016

@author: swamy
"""
noOfDays= int(input("enternumber:"))

n=0
m=0
r=noOfDays
str=1
part=1
prt2=1
if(20<noOfDays<=1 ):
    print('no')
else:
    while(part<noOfDays):
        while(n<noOfDays):
            while(m<noOfDays+1):
                
                print(' '*r,end="")
                print('*'*str,end="")
                print(' '*r,end="")
                str=str+2
                m=m+1
                r=r-1
                print()
                
            n=n+1
        
        n=2
        if(part==1):
            m=2
        else:
            m=2+(part-1)
        
        str=3
        r=noOfDays-1
        prt2=prt2+1
        part=part+1
        
    print(' '*noOfDays,end="")
    print('*',end="")
    print(' '*noOfDays,end="")
    print()    
    print(' '*noOfDays,end="")
    print('*',end="")
    print(' '*noOfDays,end="")      
    
