#print_vars() #for python2
print(vars())
a=10
print("%s"%vars())

import math
print(math.cos(a))

from math import cos
print(cos(a))

from math import cos as cos_V1
print(cos_V1(a))

from math import *
print(cos(a))
