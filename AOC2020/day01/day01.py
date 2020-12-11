#%%
import itertools 
def part1(l):
    for i in l:
        if 2020-i in l : return i
    return 0
def part2(l):
    for i,j,k in itertools.product(l,l,l): 
        if i+j+k==2020: 
            return i*j*k
    return 0
# %%
with open('input.txt') as txt: s=txt.read() 
l = [int(i) for i in s.split()]
# %%
print(part1(l))
print(part2(l))