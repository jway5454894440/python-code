__author__ = 'guojiewei'

import  functools

# int2 = functools.partial(int, base=2)
# int2('1000000')

int2 = functools.partial(int, base=2);
print(int2('1000000'))