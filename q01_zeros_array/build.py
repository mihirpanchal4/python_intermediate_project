# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),  '..'  ))
import numpy as np

# Your solution
def array_zeros():
    n1 = np.zeros((3,4,2)).reshape((2,3,4))
    return n1

print array_zeros()
