import numpy as np

def xsqr(x_a):
    return (x_a)**2 - 2*(x_a) + 1

def sinx(x_b):
    return np.sin(x_b) + 5

def lnx(x_c): 
    return np.log((x_c)+1) + (x_c)**2 + x_c

def cosx(x_d):
    return np.cos(x_d) - 5 + (x_d)**3
