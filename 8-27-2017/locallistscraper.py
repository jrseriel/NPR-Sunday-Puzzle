import urllib.request
import re
import string

filename = "dictionary.txt"

#read each line in to array
with open (filename) as f:
    array = f.readlines()

array = [x.strip() for x in array]

newlist = []
for x in array:
    #print (x)
    x = x.encode('ascii', 'ignore').decode('ascii')
    #for x in x.split():
    if len(x.split()) > 0:
        y = x.split()
        for z in y:
            #format string
            myString = z;
            myString = myString.encode(encoding='ascii', errors='strict')
            myString = myString.decode()
            translation = str.maketrans("","", string.punctuation);
            myString = myString.translate(translation);
            myString = myString.lower()
            if '\\' in myString:
                myString = myString.replace('\\', "")

            print (myString)

            #add to new list
            newlist.append(myString)

    else:
        #format string
        myString = x;
        myString = myString.encode(encoding='ascii', errors='strict')
        myString = myString.decode()
        translation = str.maketrans("","", string.punctuation);
        myString = myString.translate(translation);
        myString = myString.lower()
        if '\\' in myString:
            myString = myString.replace('\\', "")

        print (myString)

        #add to new list
        newlist.append(myString)

f.close()

fo = open("dictionary.txt", 'w')

for x in newlist:
    fo.write(x+"\n")

fo.close()
