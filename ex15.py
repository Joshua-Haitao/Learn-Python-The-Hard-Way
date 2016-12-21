#import modules of argv from sys
from sys import argv
#Use argv to get a filename
script, filename = argv
#use open to open the file
txt = open(filename)
#A little message and use .read() to print file out
print "Here's your file %r:" % filename
print txt.read() #we call a function on txt named read.
#A little message and name the ex15_sample.txt to file_again
#print "Type the filename again:"
txt.close()


file_again = raw_input("> ")#get the name from raw input filename
#After enter, open file_again
txt_again = open(file_again) #open filename again
#print txt_again out
print txt_again.read()
txt_again.close()#It's important to close files when you are done with them


###############Reading files####################
