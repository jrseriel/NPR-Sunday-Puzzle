from itertools import permutations

#NPR Weekly Challenge #1 8/15/2017
#This week's challenge comes from listener Patrick Berry of Jasper, Ala. Name a long-running TV show in two words. Add a C and rearrange the result to name another long-running TV show also in two words. What shows are these? And here's a hint: Both shows are currently on the air, although the second one was most popular the past.

filename = 'tvlist2.txt'

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

#print (twowords)

containsc = []
for x in twowords:
    #print (x)
    if 'c' in x:
        #print ('yes')
        containsc.append(x)

#print (containsc)

result = {}
for x in containsc:
    temp =[]
    for y in twowords:
        if len(x)-1 == len(y):
            temp.append(y)
    result[x] = temp

print (result)
print ("\n")

final = []
for key,value in result.items():
    noc = key.replace('c', '', 1)
    #print (set(value))
    for x in value:
        if  set(noc)>=set(x) and set(x)>=set(noc):
            print (set(key) & set(x))
            final.append(key)
            final.append(x)

#format final list

print ("\n")
print ("The possible solutions are:")
temp = []
for x in final:
    if len(final) > 2:
        temp = [final[0], final[1]]
        print (temp)
        final.pop(0)
        final.pop(0)
    else:
        print (final)

#END
