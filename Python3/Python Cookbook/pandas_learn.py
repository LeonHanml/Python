import pandas as pd
from pandas import  Series,DataFrame
import numpy as np
obj = Series([4,7,-5,3],index=['a','b','c','d'])
obj2 = Series([4,7,-5,3],index=['a','b','c','d'])
print(obj)
print(obj.index)
print(obj.values)
# Series  取值类似于数组
print(obj[1])
print(obj['b'])
print(obj[['a','c']])
obj[obj>0]

df = DataFrame(np.arange(9).reshape((3,3)),columns=list('bcd'),
               index=['O','T','C']
               )

