#if you don not understand something now, you will later as you complete more exercises. Write down what you do not understand, and keep going.
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
#if you choose to use formatter, then you should not
#write comma after the ""
#and also remember that use % not %s or %d or other after
#the "" , just use %.
print "Here are the days: %s" % days
print "Here are the months: %s" % months
#you have to writh like """, no spaces between each one

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
