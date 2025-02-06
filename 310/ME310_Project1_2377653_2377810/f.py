"""
Created on Tue Nov 15 20:28:46 2022

@author: Murat Berk
""" 
import math
import numpy

def f(x):
    return x**2 - (1-x)**5
def fp(x):
    return 2*x + 5*(1-x)**4

####################### By simply deleting """ we can change it to another function
""" 
def f(x):                                 #### funcion 2
    return x*math.exp(x) - 1              #### funcion 2
def fp(x):                                #### funcion 2
    return math.exp(x) + x*math.exp(x)    #### funcion 2
"""
"""
def f(x):                                 #### funcion 3
    return math.cos(x)-x**3               #### funcion 3
def fp(x):                                #### funcion 3
    return -math.sin(x)-3*x**2            #### funcion 3
"""
"""
def f(x):                                 #### funcion 4
    return numpy.log(x)                   #### funcion 4
def fp(x):                                #### funcion 4
    return 1/x                            #### funcion 4
"""
"""
def f(x):                                 #### funcion 5
    return x**3                           #### funcion 5
def fp(x):                                #### funcion 5
    return 3*x**2                         #### funcion 5
"""
"""
def f(x):                                                    #### funcion 6
    return numpy.log(x**2+7*x-30)-1                          #### funcion 6
def fp(x):                                                   #### funcion 6
    return (2*x+7)*numpy.log(x**2+7*x-30)                    #### funcion 6
"""
"""
def f(x):                                                    #### funcion 7
    return x**-1 - numpy.sin(x) + 1                          #### funcion 7
def fp(x):                                                   #### funcion 7
    return -x**-2 - numpy.cos(x)                             #### funcion 7
"""













