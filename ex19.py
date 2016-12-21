def cheese_and_crackers(cheese_count, amount_of_crackers): #define a function here
    print "You have %d cheeses!" % cheese_count #print out the first vairables
    print "You have %d boxes of crackers!" % amount_of_crackers #print out the second variables
    print "Man that's enough for a party!"
    print "Get a blanket.\n\n" #\n here is to open a new line in print console

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)#directly use two numbers to the function

print "OR, we can use variables from our script:"
amount_of_cheese = 10 #define a new variable
amount_of_crackers = 50 #define a new variable

cheese_and_crackers(amount_of_cheese,amount_of_crackers) #use two new defined variables as paramenters
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)#even we can do math when using the function

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)#we can both use new defined variable and do math inside too


def newfunction(a,b):
    print "a is %d" % a
    print "b is %d" % b
    c = a + b
    print "add together is %d.\n" % c

print "We can just give the function numbers directly:"
newfunction(1,2)

print "we can use variables from our script:"
d = 10
e = 20
newfunction(d,e)

print "We can do math inside"
newfunction(50+50,100+100)

print "We can combine the two, variables and math:"
newfunction(d + 50, e + 100)

print "two variables add together:"
f = 10
g = 20
newfunction(d+f, e+g)
