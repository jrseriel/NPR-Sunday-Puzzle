from itertools import permutations

#NPR Weekly Challenge #1 8/15/2017

filename = 'tvlist.txt'

#read each line in to array
with open (filename) as f:
    array = f.readlines()

array = [x.strip() for x in array]
#print (array)

#Check array for two words (not really tuples)
twowords = set([])
count = 0
for x in array:
    if len(x.split()) == 2:
        x=x.replace(" ", "")
        twowords.add(x)
        count = count +1

print (twowords)
print (count)

result = []
for x in twowords:
    y=x+'c'
    #print ("\n"+x+"\n")
    print (y)
    if set(twowords) & set(''.join(z) for z in permutations(y)):
        print ("I got the answer!")
        result.append(x)
        result.append(set(y) & set(''.join(z) for z in permutations(y)))


print ("\n")
print ("The answer is... ")
print (result)
