from sys import argv
#import argv from sys
script, input_file = argv
#unpack argv?
def print_all(f):
    print f.read()
#define a function to read a file
def rewind(f):
    f.seek(0)
#define a function to rewind file
def print_a_line(line_count, f):
    print line_count, f.readline(),#if you add a comma here, it will avoid adding double \n to every lien
#define a function to read a specific line of a file
current_file = open(input_file)
#open the input file for the following operation
print "First let's print the whole file:\n"
##Name the operation of the following code
print_all(current_file)
#Use function print_all to print the whole input file
print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)
#define current_line to print and use function print_a_line
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
