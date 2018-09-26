# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 01:03:20 2017

@author: swamy
"""
#importing random library to generate random coordintes and matplotlib to visualize the data
import random
#import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Taking the input from keyboard number of dots
number_of_points = int(input("Enter Number of dots: "))

#generating random coordinates
x_coordinates = [random.random() for _ in range(0,number_of_points)]
y_coordinates = [random.random() for _ in range(0,number_of_points)]
count_in_circle= 0
colors = []

#calculating if th epoint lies in the circle or out of the circle
# (0,0) is considered as the cennter and distance from center to any point in the circle is less than the radius
#if the distance is less than 1 then the number of points in the circle is increased by 1
#for plotting color list is used in circle in Red and out of circle in Green

for i in range(number_of_points):
    if ((x_coordinates[i])**2+(y_coordinates[i])**2) <= 1:
        count_in_circle += 1
        colors.append('Red')
    else:
        colors.append('Green')

#Monte carlo simulation gives (area of quarter circle (pi*r**2/4))/(area of square(l=r)**2)= number of points in circle/total number of points in square
value_of_pi = (4*count_in_circle)/number_of_points


print("\nValue of Pi based on Monte carlo simulation for %d dots is "%number_of_points,value_of_pi)
#Code to note down all the values of Pi
#Code to record the values of different values of pi for differnet values of input
try:
    df = pd.read_pickle('df.pickle')
    #print(df)
except :
    df = pd.DataFrame(columns = ['Number of dots','Pi Value'])
     #print(df)
df2= pd.DataFrame({'Number of dots':number_of_points,'Pi Value':value_of_pi},index =[0])
df = pd.concat([df,df2], ignore_index = True)
print("\n\n")
print(df)
df.to_pickle('df.pickle')
df.to_csv('df.csv')

#plotting the values  using matplotlib
plt.scatter(x_coordinates,y_coordinates, color= colors)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel("circle of radius R = 1")
plt.ylabel("Square of length L = 1")
plt.title(("Value of pi based on Monte carlo simulation for %d dots is %f"%(number_of_points,value_of_pi)))
plt.show()
