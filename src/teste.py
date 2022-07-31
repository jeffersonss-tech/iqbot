

from inspect import _empty

from numpy import empty
from pandas import isnull
from traitlets import Int

investing = 0
while investing < 1 or investing > 10:
    try:
        investing = int(input('digite o valor do investimento:\n'))
        if investing == Int(''):
            break
    except:
        pass
