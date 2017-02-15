name = 'Cyrus Boyce'
age = 25.2
height = 70.2 # inches
weight = 250.5 # lbs 
eyes = 'Brown'
teeth = 'Yellow'
hair = 'Brown'
kilo_weight = weight * 0.453592
metric_height = height * 2.54
print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "He is a little too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

print "This is %s's weight in Kilograms %f" % (name, kilo_weight)
print "This is %s's height in Centimeters %f" % (name, metric_height)
