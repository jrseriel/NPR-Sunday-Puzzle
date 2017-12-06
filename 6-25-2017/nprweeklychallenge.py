from itertools import permutations

#NPR Weekly Challenge 6-25-2017
#This week's challenge comes from Kruno Matic, a correspondent of mine in Croatia. Take the name KIM KARDASHIAN. Rearrange the letters to get the last name of a famous actress along with a famous one-named singer. Who are these people?

filename = 'actresslist.txt'

#read each line in to array
with open (filename) as f:
    array = f.readlines()

array = [x.strip() for x in array]
#print (array)

str = 'kimkardashian'

lastname = []
for x in array:
    index = len(x.split())
    x = x.split()[index-1]
    lastname.append(x)

#Format list removing duplicates
seen = set()
unique = []
for x in lastname:
    if x not in seen:
        unique.append(x)
        seen.add(x)

#not a simple algorithm
dict = {}
for x in unique:
    if  set(str)>=set(x):
        newstr = str
        print (x)
        letters = list(x)
        print (letters)
        for y in letters:
            if y in newstr:
                index = newstr.index(y)
                newstr = newstr[:index] +newstr[index+1:]
        dict[x] = newstr

print ("\n")
print (dict)
print ("\n")

filename = 'singerlist.txt'

#read each line in to array
with open (filename) as f:
    array = f.readlines()

array = [x.strip() for x in array]
#print (array)

onename = []
for x in array:
    x = x.split()
    if len(x) is 1:
        x= ''.join(x)
        onename.append(x)

print (onename)

result = []
for key,value in dict.items():
    temp = []
    for x in onename:
        if set(value)<=set(x):
            temp.append(key)
            temp.append(x)
            result.append(temp)

print ("\n")
print ("The possible solutions are:")
print (result)

#END
