# import math
# hoặc dùng from math import *
from math import *
x1 , y1 , x2, y2 = map(float, input().split())
print('%.4f' % (sqrt(pow(x2-x1,2)+pow(y2-y1,2))))
