import numpy as np
import pandas as pd

def gameMatrix (A):
    return np.array(A)

def saddlepoint(A):
    #A = np.array(A)
    minmax = (A.min(axis=1))
    maximum = minmax[0]
    for i in minmax:
           if minmax[i] > maximum:
                  maxpos = i
                  print (maxpos)
    print (minmax)


    maxmin = (A.max(axis=0))
    minimum = maxmin[0]
    for i in maxmin:
           if maxmin[i] < minimum:
                  minpos = i
                  print (minpos)

    print (maxmin)

    if minmax==maxmin:
       print ("Saddle Point Present")
    else:
       print("No Saddle Point")

k = [[1,1,-1,1,1,-1],[-1,1,-1,-1,1,-1],[-1,-1,-1,1,1,1]]
#k = [[0.30,0.25,0.20],[0.26,0.33,0.28],[0.28,0.30,0.33]]
k = np.array(k)
k
saddlepoint(k)