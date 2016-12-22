# —*- coding: utf-8 -*-
my_name = '陆'
my_name_2 = "Yz"
my_age = 18
my_weight = 10
my_height = 20
my_eyes = 'black'
my_teeth = 'white'
my_hair = 'black'

print "Let's talk about %s." % my_name
print "LET'S TALK ABOUT %s." % my_name_2
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_weight, my_height, my_age + my_weight + my_height)