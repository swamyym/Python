# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 20:42:59 2017

@author: swamy
"""
# scraping using HTML


import urllib
import bs4 as bs
import simplejson as json
import re
import pandas as pd
import datetime as dt
def bss():

    urlopen = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()

    scraper = bs.BeautifulSoup(urlopen,'lxml')

    urls=[]

    not_urls=[]
    for url in scraper.find_all('a'):
        #print(url.get('href'))
        urls.append(url.get('href'))
    #print(urls)
    for one in urls:
        #print(one)
        if(not(re.findall('^https',one))):
            #print(one)
            #print(urls.index(one))
            not_urls.append(one)
            #print(urls)
    #print(urls)
    urls= list(set(urls)-set(not_urls))
    src=list()
    for url in urls:
        url1 = urllib.request.urlopen(url).read()
        scraper1 = bs.BeautifulSoup(url1,'lxml')


        for img in scraper1.find_all('img'):
            src.append(img.get('src'))

            try:
                name = img.get('src').split('/')[-1]
                urllib.request.urlretrieve(img.get('src'),name)
            except:
                continue

def sitemap():
    urlopen = urllib.request.urlopen("https://pythonprogramming.net/sitemap.xml").read()
    scraper = bs.BeautifulSoup(urlopen,'xml')
    urls = []
    dates=[]



    for one in scraper.find_all('url'):
        #urls.append(one.text)
        #print(url.text,lastmod.text)
        #print(type(url.text))
        #urls[one.findNext("loc").text] = one.findNext("lastmod").text
        urls.append(one.find("loc").text)
        dates.append(one.find("lastmod").text)

    #print(urls)
    return urls,dates

urls,dates= sitemap()
#print(urls)
#keys= pd.Series(urls)
#values = pd.Series(urls.values())

#df = pd.DataFrame("Url23" = keys,"DateModified" = values)

#print(keys)
#print(values)
#keys.index.name = 'Url'
df= pd.DataFrame({'urls':urls,'date':dates})
#df=df.set_index('date')

#df.columns = ['Urls', 'Lost Modified']
#for i in range(len(df)):

#    df['Lost Modified date'] = dt.datetime.strptime(df['Lost Modified'][i],'%Y-%m-%d

df.to_json(orient ='row')

