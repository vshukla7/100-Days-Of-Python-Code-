# day 44
import math
math.floor(4.5)

result = math.sqrt(9) #square root of 9
print(result)

# also we can use from math import sqrt

from math import sqrt
result = sqrt(9)
print(result)

# also we can use from math import *
# isse sare functions ko import krenge
# but it is not a good practice because it import everything in the code or script 


# as keyword 
# help to keep the code clean and use function in simple way  

from math import pi as p
print(p)

# how to check all functions using the dir function 
# it help us to check the all keywords in a module

import math
print(dir(math))

# output 
# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']