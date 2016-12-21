print "How old are you?", #the , here to continue the line instead of start a new line
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
age, height, weight) #python like less than 80 characters
#the input() function will try to convert things you enter
#as if they were python code, but it has security problems
#so you should avoid it 
