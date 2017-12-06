import urllib.request
import re
import string

name = 'foods'

#IO
fo = open(name+".txt", "w")

#substrings deliminitor
preindex = '<a href="'
postindex = '</a>'

url = 'ttp://www.thefoodcoach.com.au/food/?Alpha=%5BA-Z%5D'

#url of wiki page
setup = str(urllib.request.urlopen(url).read())

#debug
#print (setup)

#function to get all list items
index = 0
for match in re.finditer(preindex, setup):
    myString = str(setup[setup.find(preindex,index)+ len(preindex): setup.find(postindex,setup.find(preindex,index))])
    if len(myString.split()) > 2:
        myString = myString.split()[2]
        myString = myString[4:]
    #    myString =  myString.split()[0]

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

    #write to file
    fo.write(myString+"\n")

#close file
fo.close()
