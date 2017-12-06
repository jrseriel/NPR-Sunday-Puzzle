#NPR Weekly Challenge #1 11/12/2017
#This week's challenge comes from listener Steve Baggish of Arlington, Mass. Take the name of a U.S. state capital. Immediately to the right of it write the name of a world capital. If you have the right ones, the name of a U.S. state will be embedded in consecutive letters within that letter string. What three places are these?

#LIST DECLARATIONS

filename = 'usstatecap.txt'

#read each line in to array
with open (filename) as f:
    array = f.readlines()

usstatecap = [x.strip() for x in array]
#print (array)

filename = 'worldcap.txt'

#read each line in to array
with open (filename) as f:
    array = f.readlines()

worldcap = [x.strip() for x in array]
#print (array)

filename = 'usstates.txt'

#read each line in to array
with open (filename) as f:
    array = f.readlines()

usstates = [x.strip() for x in array]
#print (array)

#FUNCTION

#debug
#print (usstatecap)
#print (worldcap)
#print (usstates)

result = []
for x in usstatecap:
    for y in worldcap:
        str = x+y
        for z in usstates:
            if z in str:
                result.append(x+", "+y+", "+z)

print ("\n")
print ("The possible solutions are:")
for x in result:
    print (x)

#END
