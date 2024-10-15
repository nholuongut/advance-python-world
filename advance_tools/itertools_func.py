from itertools import accumulate , groupby
from operator import *

# accumulate
a = [1,2,3,4,5]
acc = accumulate( a , func= mul )
print(list(acc))

# group by
def smaller_than_3(x):
    return x < 3

group = groupby( a , key=smaller_than_3 )
for i_key , i_val in  group:
    print(i_key , list(i_val))

# lambda 

group_lambda = groupby(a , key= lambda x : smaller_than_3(x=x))
for i_key , i_val in group_lambda :
    print( i_key , list(i_val) )