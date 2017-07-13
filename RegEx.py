# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 18:01:44 2016

@author: swamy
"""

import re
def nondot():
    ln = "From: swamy.ymln@gmail.com Sub: RegEx"

    y = re.findall('^From: .*@([^.]*)',ln)

    print(y)

nondot()

def anychar():
    ln = "From: swamy.ymln@gmail.com Sub: RegEx"

    y = re.findall('^From: .*@(.*)',ln)

    print(y)
#anychar()

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
#print(y)

def sumn():
    total=0
    txtfile = open("regex_sum_236830.txt")
    numlist = list()
    for line in txtfile:
        line= line.rstrip()
        numadtn = re.findall('[0-9]+',line)
        if len(numadtn)>0:
            numlist.append(numadtn)
    #sumnm = sum(numlist)
    #print(len(numlist))
    for i in numlist:
        i= list(map(int,i))
        ls = sum(i)
        total=total+ls
    print(total)

#sumn()
#noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
#print(noprimes)
#anychar()
#nondot()

