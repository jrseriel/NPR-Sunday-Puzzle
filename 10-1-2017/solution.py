#NPR Weekly Challenge #1 10-1-2017
#This challenge comes from Steve Baggish of Arlington, Mass. Think of a 4-letter food. Move each letter one space later in the alphabet — so A would become B, B would become C, etc. Insert a U somewhere inside the result. You'll name a 5-letter food. What foods are these?

filename = 'Pleco food list.txt'

#read each line in to array
with open (filename) as f:
    array = f.readlines()

array = [x.strip() for x in array]
#print (array)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z']

list = []
for  x in array:
    string  = ""
    for y in x:
        print (x)
        index = alphabet.index(y)
        nextindex = index + 1
        if len(x) > nextindex:
            string = string + alphabet[nextindex]
    list.append(string+"u")

print (list)

fiveletterfood = []
for x in array:
    if  len(x) == 5:
        fiveletterfood.append(x)

print (fiveletterfood)

result = []
for x in list:
    for y in fiveletterfood:
        if set(y) >= set(x) and set(x) >= set(y):
            result.append(x+", " + y)

print ("\n")
print ("The possible solutions are:")
print (result)

#END
