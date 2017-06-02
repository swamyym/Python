# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 14:18:51 2016

@author: swamy
"""
import urllib

fhand= urllib.request.urlopen('http://www.data.pr4e.org/intro-short.txt')
for line in fhand:
    print(line.strip()) 