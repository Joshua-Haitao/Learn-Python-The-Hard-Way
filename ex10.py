# -*- coding: utf-8 -*-
print "I am 6'2\" tall." #make " in the string normally appear
print 'I am 6\'2" tall.' #make ' in the string normally appear.
tabby_cat = "\tI'm tabbed in." #Horizontal Tab
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "\a"
print "\b"
print "\f"
print "\N{我们}"
print "\r"
print "\t"
print "\v"
print "\ooo"

#while True:
#    for i in ["/","-","|","\\","|"]:
#        print "%s\r" % i,

test = "a \' b"
print "which is better, %r" % test # with ' in both side
print "which is better, %s" % test # without ' in both side
