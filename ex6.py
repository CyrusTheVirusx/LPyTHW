 # String variable using %d to call the # 10
x = "There are %d types of people." % 10
 # String variables
binary = "binary"
do_not = "don't"
 # String variable calling the string values of binary and do_not
y = "Those who know %s and those who %s." % (binary, do_not)
 # Prints the strings x and y
print x
print y 
 # Repeats the bad joke. calling the string variables x and y 
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False 
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e