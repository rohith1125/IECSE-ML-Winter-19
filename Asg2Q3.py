import numpy as np
def match(a,b):
    '''
    Inputs:
      a, b: numpy arrays of same shape of 1 dimension
    Outputs:
      list containing indices where both arrays have same elements
    '''

    n = a.shape[0]
    arrt = np.array([])
    arrn = np.array([])
    for i in range(n):
    	if a[i] == b[i]:
    		arrt = i;
    		arrn = np.hstack([arrn,arrt])
    return arrn

"""Test for match"""
assert np.any(match(np.array([1,2,3,2,3,4,3,4,5,6]),np.array([7,2,10,2,7,4,9,4,9,8])) == [1,3,5,7])
print("Sample Tests passed", '\U0001F44D')