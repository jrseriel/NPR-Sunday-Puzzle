from itertools import permutations

#NPR Weekly Challenge #1 9-3-2017
#This challenge comes from listener Patrick Berry of Jasper, Ala., who had the clever AMERICAN DAD + C = CANDID CAMERA anagram a few weeks ago. This challenge is another anagram. Rearrange the 15 letters of COOL HIT FARE IN L.A. to name a famous song that's appropriate to the given phrase.

filename = 'classicrocksongs.txt'

#read each line in to array
with open (filename) as f:
    array = f.readlines()

array = [x.strip() for x in array]
#print (array)

string = "coolhitfareinla"

nowhitespace = []
for x in array:
    x = x.replace(" ", "")
    nowhitespace.append(x)

print ("\n")
print (nowhitespace)

list = []
for x in nowhitespace:
    if set(string) >= set(x):
        list.append(x)

#debug
print ("\n")
print (list)

result = []
for x in list:
    if len(x) == 15:
        result.append(x)

print ("\n")
print ("The possible solutions are:")
print (result)

#END
