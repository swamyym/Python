# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 22:45:00 2017

@author: swamy
"""

import urllib
import bs4 
import re 
sm=0
url  = input("Enter Url-")
html = urllib.request.urlopen(url)

soup = bs4.BeautifulSoup(html,"lxml")

tags= soup('a')
count= int(input("Enter count-"))
position= int(input("Enter Position-"))
i=0
j=0
while(i<count):
    
    for tag in tags:
        j =j+1
        if(j==position):
            print(tag.get('href',None))
            url= tag.get('href',None)
            break
    word= re.findall('.*_by_(.+).html',url)
    print(word)
    j=0        
    html = urllib.request.urlopen(url)
    soup = bs4.BeautifulSoup(html,"lxml")
    tags= soup('a')
    i = i+1     
    
