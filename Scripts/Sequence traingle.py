# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n1= 6
n2= 28
n3= 66
m1 = n2-n1
m2 = n3-n2
diff = m2-m1

noOfRows= 4
print(n1)
print(n2,' ',n3)
numberRow = 10


n=0
noOfitemsInRow =0
previousRowItems = 2
while(noOfitemsInRow<numberRow):
    
    m3=m2+16    
    nNext=n3+m3
    print(nNext,end="")
    print(' ',end="")
    
    n3=nNext
    m2=m3
    n=n+1
    noOfitemsInRow = noOfitemsInRow+1
    
    if(previousRowItems<noOfitemsInRow):
        print('')
        previousRowItems=noOfitemsInRow
        if(noOfitemsInRow==numberRow):
            break
        noOfitemsInRow= 0
        
        
#==============================================================================
# 
# n=2
# for i in range(0,20):
#     
#     m=n*(2*n-1)
#     print(m)
#     n=n+2
#     
# 
#==============================================================================

    
        