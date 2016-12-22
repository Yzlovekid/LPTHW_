x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who konw %s and whose who %s."

print x
#print y
print y % (binary, do_not)

print "I said: %r." % x
print "I also said: '%s'." % y % (binary, do_not)

hilarious = True
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e