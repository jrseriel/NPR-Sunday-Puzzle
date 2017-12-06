import urllib.request
import re
import string

#IO
fo = open("socialgroups.txt", "w")

#substrings deliminitor
preindex = '<td><a'
postindex = '</a>'

url = 'https://en.wikipedia.org/wiki/List_of_contemporary_ethnic_groups'

#url of wiki page
setup = str(urllib.request.urlopen(url).read())

#function to get all list items
index = 0
for match in re.finditer(preindex, setup):
    myString = str(setup[setup.find(preindex,index)+ len(preindex): setup.find(postindex,setup.find(preindex,index))])
    if len(myString.split()) > 1:
        myString = myString.split('">',1)[1]
    index = setup.index(preindex,index+1)

    #format string
    myString = myString.encode(encoding='ascii', errors='strict')
    myString = myString.decode()
    translation = str.maketrans("","", string.punctuation);
    myString = myString.translate(translation);
    myString = myString.lower()
    if '\\' in myString:
        myString = myString.replace('\\', "")
    if 'sxc3xa1bado' in myString:
        myString = myString.replace('sxc3xa1bado', 'sabado')
    #if 'amp;' in myString:
    #        myString = myString.replace('amp;', '')
    if 'amp' in myString:
        myString = myString.replace('amp', 'and')
    if 'xc2xa1despierta amxc3xa9rica' in myString:
        myString = myString.replace('xc2xa1despierta amxc3xa9rica', 'despierta america')

    #debug
    print (myString)

    #write to file
    fo.write(myString+"\n")

#close file
fo.close()
