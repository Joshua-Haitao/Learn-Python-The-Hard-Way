# -*- coding: utf-8 -*-
#define formatter
#%r is used for debugging and inspection.
formatter = "%s %r %r %r"
#print 1,2,3,4
#print formatter % (1, 2, 3, 4)
#print one two three four
print formatter % ("你好", "two", "three", "four")
#Don't add "" for true and false here
#print formatter % (True, False, False, True)
#put the formatter inside the formatter
#print formatter % (formatter, formatter, formatter, formatter)
#you can not ignore the comma between each item
#write down your mistakes, and try not to make
#the same mistakes on the next exercise
#print formatter % (
#    "I had this thing.",
#    "That you could type up right.",
#    "But it didn't sing.",
#    "So I said goodnight."
#)
