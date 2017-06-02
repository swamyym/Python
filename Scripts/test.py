# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 00:39:21 2016

@author: swamy
"""

w=  [x for x in range(1,101)]
print(w)

x= [i for i in range(1,101,2)]
print(x)
y = [i for i in x if x.index(i)%2==0]
print(y)
z = [i for i in y if y.index(i)%2==0]
print(z)
a= [i for i in z if z.index(i)%2==1]
print(a)
b= [i for i in a if a.index(i)%2==0]
print(b)
c=[i for i in b if b.index(i)%2==0]
print(c)
