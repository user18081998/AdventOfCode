# %%
def parse(line):
    numbers=[]
    rest=[]
    letter=""
    i=0
    while(i<len(line) and len(line)>0):
        if line[i].isnumeric():
            number=""
            while(i<len(line) and line[i].isnumeric()):
                number+=line[i]
                i+=1
            numbers.append(number)
        if len(numbers)==2 and letter=="":
            letter=line[i+1]
            rest=line[i+4:]
            break
        i+=1
    numbers=[int(i) for i in numbers]
    return numbers, letter, rest
# %%
with open('input.txt') as txt: s=txt.readlines()
s=[line.strip() for line in s]
parsed = [parse(line) for line in s]
count1 = len([1 for line in parsed if (line[0][0]<=len([i for i in line[2] if i==line[1]])<=line[0][1])])
# %%
print(count1)

#%%
def test(line):
    try:
        return (line[2][line[0][0]-1]==line[1]) != (line[2][line[0][1]-1]==line[1])
    except:
        return False
count2 = len([1 for line in parsed if test(line)])

# %%
