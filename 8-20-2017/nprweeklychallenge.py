from itertools import permutations

#NPR Weekly Challenge #1 8-20-2017
#This week's challenge comes from listener Steve Baggish of Arlington, Mass. Think of two synonyms — one in 5 letters, the other in 4. The 5-letter word starts with S. The 4-letter word contains an S. Change one of these S's to an A. You can rearrange the result to name a group of people, in 9 letters, that ideally have those two adjectives describe them. What group is it?

filename = 'sadjectiveslist.txt'

#read each line in to array
with open (filename) as f:
    array = f.readlines()

array = [x.strip() for x in array]
#print (array)

startswithslist = []
for x in array:
    if x.startswith('s'):
        if x.endswith('t'):
            startswithslist.append(x)

print ("\n")
print (startswithslist)

fiveletteradjectiveslist = []
for x in startswithslist:
    if len(x) == 5:
        fiveletteradjectiveslist.append(x)

print ("\n")
print (fiveletteradjectiveslist)

filename = 'all.txt'

#read each line in to array
with open (filename) as f:
    array = f.readlines()

array = [x.strip() for x in array]
#print (array)

containsslist = []
for x in array:
    if 's' in x:
        if x.endswith('t'):
            if len(x) == 4:
                containsslist.append(x)

print ("\n")
print (containsslist)

filename = 'groups.txt'

#read each line in to array
with open (filename) as f:
    array = f.readlines()

array = [x.strip() for x in array]
#print (array)

ninelettergroups = []
for x in array:
    if len(x) is 9:
        if 's' in x:
            ninelettergroups.append(x)

print ("\n")
print (ninelettergroups)

combined = []
for x in fiveletteradjectiveslist:
    for y in containsslist:
        str = (x+y)
        str = str.replace('s', 'a', 1)
        combined.append(str)

print ("\n")
print (combined)
print ("\n")

#print ("The possible solutions are:")
result = []
for x in ninelettergroups:
    print (x)
    for y in combined:
        if set(x) >= set(y) and set(y) >= set(x):
            result.append(x + ', ' + y.replace('a','s',1))
            #result.append(x+ ', ' +y)
            #result.append(y.replace('a','s',1))
            #print (result)

print ("\n")
print ("The Possible Solutions Are:")
result = list(set(result))
for x in result:
    print (x)

#print ("\n")
#print ("The possible solutions are:")
#print (result)

#END
