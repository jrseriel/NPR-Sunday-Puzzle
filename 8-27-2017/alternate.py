from itertools import permutations

#NPR Weekly Challenge #1 8-27-2017
#This week's challenge is a common two-word expression. The expression consists of 8 letters and uses all five vowels — A, E, I, O and U. It has only three consonants, one of which is repeated. The first word in the expression has two letters and the second has six letters. What familiar expression is it?

filename = 'dictionary.txt'

#read each line in to array
with open (filename) as f:
    array = f.readlines()

array = [x.strip() for x in array]
#print (array)

firstword = ['au','la','an', 'do', 'if', 'by', 'ox', 'is','un', 'yo', 'he', 're', 'my', 'am', 'on', 'or', 'ed', 'be', 'in', 'so', 'ex', 'at', 'im', 'of', 'no', 'as', 'it', 'me', 'to', 'we', 'us', 'ah', 'go', 'up',]
#firstword = []
secondword = []
for x in array:
    if (any(str.isdigit(c) for c in x)):
        pass
    elif len(x) == 6:
        secondword.append(x)
    #elif len(x) == 2:
    #    firstword.append(x)

firstword = set(firstword)
secondword = set(secondword)

print (firstword)
print (secondword)

vowels = ['a','e','i','o','u']
containsvowels = []
for x in firstword:
    for y in secondword:
        temp = x+y
        if set(temp) >= set(vowels):
            containsvowels.append(temp)

print ("\n")
print (containsvowels)

consonants = 'bcdfghjklmnpqrstvwxyz'
threeconsonants = []
for x in containsvowels:
    count = 0
    for y in x:
        if y in consonants:
            count += 1
    if count == 3:
        threeconsonants.append(x)

print ("\n")
print (threeconsonants)

formattedconsonants = []
for x in threeconsonants:
    seen = []
    count = 0
    for y in x:
        if y in consonants:
            if y in seen:
                count += 1
            else:
                seen.append(y)
    if count == 1:
        formattedconsonants.append(x)

print ("\n")
print (formattedconsonants)

result = []
for x in formattedconsonants:
    x = x[:2] + ' ' + x[2:]
    result.append(x)

print ("\n")
print ("The possible solutions are:")
print (result)

#au revoir

#END
