import urllib.request
import re
import string

name = 'collectivegroups'

#IO
fo = open(name+".txt", "w")

#substrings deliminitor
preindex = '<td>'
postindex = '</td>'

url = 'http://www.collectivenouns.biz/list-of-collective-nouns/collective-nouns-people/'

#url of wiki page
setup = str(urllib.request.urlopen(url).read())

#debug
#print (setup)

#function to get all list items
index = 0
for match in re.finditer(preindex, setup):
    myString = str(setup[setup.find(preindex,index)+ len(preindex): setup.find(postindex,setup.find(preindex,index))])
    if len(myString.split()) > 1:
        secondString = myString.split()[2]
        myString =  myString.split()[0]

    index = setup.index(preindex,index+1)

    #format string
    myString = myString.encode(encoding='ascii', errors='strict')
    myString = myString.decode()
    translation = str.maketrans("","", string.punctuation);
    myString = myString.translate(translation);
    myString = myString.lower()
    if '\\' in myString:
        myString = myString.replace('\\', "")
    if 'amp' in myString:
        myString = myString.replace('amp', 'and')

    #debug
    print (myString)

    #format string
    secondString = secondString.encode(encoding='ascii', errors='strict')
    secondString = secondString.decode()
    translation = str.maketrans("","", string.punctuation);
    secondString = secondString.translate(translation);
    secondString = secondString.lower()
    if '\\' in secondString:
        secondString = secondString.replace('\\', "")
    if 'amp' in secondString:
        secondString = secondString.replace('amp', 'and')

    #debug
    print (secondString)

    #write to file
    fo.write(secondString+"\n")

#close file
fo.close()
