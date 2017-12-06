from itertools import permutations

#NPR Weekly Challenge #1 8-6-2017
#Not too hard a challenge this week. The word INAUGURATION contains the letters of GNU, GOAT, IGUANA, and AGOUTI, which are all animals. The name of what 9-letter animal can be spelled from the letters of INAUGURATION?

filename = 'animallist.txt'

#read each line in to array
with open (filename) as f:
    array = f.readlines()

array = [x.strip() for x in array]
#print (array)

myString  = 'inauguration'

#simple function
result = []
for x in array:
    if set(myString) >= set(x) and len(x) is 9:
        result.append(x)

print ("\n")
print ("The possible solutions are:")
print (result)

#END
