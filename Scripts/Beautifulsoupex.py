# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 16:13:59 2016

@author: swamy
"""

import urllib
import bs4

link = urllib.request.urlopen('https://docs.python.org/2/library/urllib.html').read()
soup= bs4.BeautifulSoup(link,"lxml")

tags= soup('a')
for tag in tags:
    print(tag.get('href'))
    