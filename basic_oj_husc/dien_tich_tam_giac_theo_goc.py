a,b,goca = map(float,input().split())

import math

rad = goca*3.14159/180

S = (1/2)*a*b*math.sin(rad)

print("{:.4f}".format(S))

'''
input:  7 10 25
output: 14.7916
'''