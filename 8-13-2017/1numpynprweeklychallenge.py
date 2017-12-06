from itertools import permutations
import numpy as np

#NPR Weekly Challenge #1 8/15/2017

filename = 'tvlist.txt'

#read each line in to array
with open (filename) as f:
    array = f.readlines()

array = [x.strip() for x in array]
#print (array)

#Check array for two words (not really tuples)
twowords = []
count = 0
for x in array:
    if len(x.split()) == 2:
        x=x.replace(" ", "")
        twowords.append(x)
        count = count +1

#Numpy array usage
twowords= np.array(twowords)

print (twowords)
print (count)

result = []
for x in twowords:
    x=x+'c'
    #print ("\n"+x+"\n")
    print (x)
    for p in permutations(x):
        p = ''.join(p)
        #print (p)
        if  p in twowords:
            result.append(x)
            result.append(p)

print ("The answer is... ")
print (result)
