#NPR Weekly Challenge #1 10-29-2017
#This week's challenge sounds easy, but it's a little tricky. Name a well-known nationality. Drop a letter, and the remaining letters in order will name a metal — one of the elements on the periodic table. What is it?
#I went on to solve this not programmitically

filename = 'metals.txt'

#read each line in to array
with open (filename) as f:
    array = f.readlines()

array = [x.strip() for x in array]
#print (array)

#format list
metals = []
for x in array:
        metals.append(x.lower())
print (metals)

filename = 'nationalities.txt'

#read each line in to array
with open (filename) as f:
    array = f.readlines()

array = [x.strip() for x in array]
#print (array)

nats = []
for x in array:
    count = 0
    for y in x:
        nats.append(x[:count] + x[count + 1:])
        count = count + 1
print (nats)

result = []
for x in metals:
    for y in nats:
        if x == y:
            result.append(x+', '+y)

print ("\n")
print ("The possible solutions are:")
print (result)

#END
