# %%
with open('input.txt') as txt: s=txt.read() 
l = [int(i) for i in s.split()]

# %%
from functools import reduce
reduce(lambda x,y : x*y,[i for i in l if 2020-i in l])
# %%
from itertools import product
set([x*y*z for x,y,z in product(l,l,l) if x+y+z==2020])

#%%