from itertools import permutations

#NPR Weekly Challenge #1 8-27-2017
#This week's challenge is a common two-word expression. The expression consists of 8 letters and uses all five vowels — A, E, I, O and U. It has only three consonants, one of which is repeated. The first word in the expression has two letters and the second has six letters. What familiar expression is it?

filename = 'dictionary.txt'

#read each line in to array
with open (filename) as f:
    array = f.readlines()

array = [x.strip() for x in array]
#print (array)

eightletterlist = []
for x in array:
    x = x.replace(' ', '')
    eightletterlist.append(x)

vowels = ['a','e','i','o','u']
doubleformatlist = []
for x in eightletterlist:
    if set(x) >= set(vowels):
        if len(x) == 8:
            doubleformatlist.append(x)

print (doubleformatlist)

print ("\n")
print ("The possible solutions are:")
#print (result)

#END
