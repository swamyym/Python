# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 14:42:59 2017

@author: swamy
"""
#import pandas as pd
def conver():
    import pandas as pd
    import rpy2.robjects as ro
    import rpy2.robjects.conversion as conversion
    from rpy2.robjects import pandas2ri
    pandas2ri.activate()

    R = ro.r

    df = conversion.ri2py(R['mtcars'])
    print(df.head())
    #return df
conver()

#https://stackoverflow.com/questions/28417293/sample-datasets-in-pandas
