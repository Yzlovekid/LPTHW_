###here is the question:
##Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
##If the number is a multiple of 4, print out a different message.
##Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num = int(raw_input('enter a number'))


if num % 4 == 0:
   print '%r is a multiple of 4.' %num
elif num % 2 == 0:
   print '%r is a even' %num
else:
   print "%r is a odd" %num

check = int(raw_input('enter a check number'))
if num % check == 0:
   print "%r can divide %r" %(num, check)
else:
   print "%r cannot divide %r" %(num, check) #如何调用两个变量
