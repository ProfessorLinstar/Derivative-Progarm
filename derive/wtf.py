from functions.callFunctions import *
count=[0,1]
oldCount=count
del count[-1]
count[0]=1
print("After:\ncount:",count,"oldCount:",oldCount)

