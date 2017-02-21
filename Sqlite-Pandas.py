# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 01:02:07 2017

@author: swamy
"""

import sqlite3
import pandas as pd
#import json
#import xml.etree.ElementTree as ET


conn = sqlite3.connect('sqlite-pandas.sqlite')
cur = conn.cursor()
cur.execute('''DROP TABLE IF EXISTS Counts''')

df = pd.DataFrame()

cur.execute('''CREATE TABLE Counts(name TEXT,count INTEGER)''')
fname = input('Enter File Name-')
#==============================================================================
# try:
#     fh = open(fname)
#     
# except:
#     
#     print("Enter valid file name")
#==============================================================================
    
        
with open(fname) as f1:
    print(f1.read())
    
    f1.close()
    

