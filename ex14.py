from sys import argv
script, user_name, hobby = argv
prompt = ': '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt) #we make a variable prompt that is set
#to the prompt we want, and we give that to raw_input instead of
#typing it over and over. Very handy.
print "Whether %s is your favorate sports?" % hobby
whether = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
Your favorate sports is %r.
You live in %r. Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, whether, lives, computer)
#make sure you understand how I combined
#a """ style multiline string with the % format
#activator as the last pring 
