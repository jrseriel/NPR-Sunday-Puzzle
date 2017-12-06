from itertools import permutations

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

twowords.sort(key = len)

print (twowords)
print (count)

result = []
for x in twowords:
    y=x+'c'
    #print ("\n"+x+"\n")
    print (y)
    for p in permutations(y):
        p = ''.join(p)
        if set(twowords) & set(p):
            print ("I got the answer!")
            result.append(x)
            result.append(set(y) & set(p))

print ("The answer is... ")
print (result)
