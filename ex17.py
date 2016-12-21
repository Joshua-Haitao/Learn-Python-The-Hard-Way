from sys import argv #use import is a way to get tons of free code
from os.path import exists #export exists from

script, from_file, to_file = argv

#print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line, how?
#infile = open(from_file) #make from_file readable
#indata = infile.read() #output the contents of infile to indata

#print "The input file is %d bytes long" % len(indata)

#print "Does the output file exists? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()#user click ENTER or CTRL-C
#open command and 'w' to make to_file writable
#out_file = open(to_file, 'w')
#out_file.write(indata) # write indata to out_file

#print "Alright, all done."

#out_file.close()
#infile.close()

#One line code
out_file = open(to_file,'w').write(open(from_file).read())

#some notes
#1. if .read without () then error message is:
##TypeError: expected a character buffer object
#2. if use out_file.close() to line 27, the error message is:
##AttributeError: 'NoneType' object has no attribute 'close'
#3. if you forgot to end a string properly with a quote, the error m is:
##Syntax:EOL while scanning string literal


############Exercise17: More Files##################
