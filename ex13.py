# write a script that also accepts arguments
from sys import argv #this is how you add features to your script
#from the Python feature set. argu is short for arguent variables
script, first, second = argv
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "What else?",
Others = raw_input()
