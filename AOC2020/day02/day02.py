# %%
with open('input.txt') as txt: s=txt.read()
c=0
for line in s:
    min,max,letter = int(line[0]), int(line[2]), line[4]
    print(min,max,letter)
    if (min<=len([x for x in line[7:] if x ==letter])<=max): c+=1
print(c)
# %%
def parse(line):
    numbers=[]
    rest=[]
    letter=""
    i=0
    while(i<len(line) and len(line)>0):
        if line[i].isnumeric():
            number=""
            while(line[i].isnumeric()):
                number+=line[i]
                i+=1
            numbers.append(number)
        if len(numbers) and letter=="":
            letter=line[i+1]
            rest=line[i+4:]
            break
    return numbers, letter, rest
# %%
