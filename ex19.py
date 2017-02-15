def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
print "We can just give the function numbers directly:"
# cheese_and_crackers function gets passed 20 as cheese_count arg and 30 as boxes_of_crackers arg
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
# create new variables with values
amount_of_cheese = 10
amount_of_crackers = 50
# call the cheese_and_crackers function passing it amount_of_cheese = cheese_count and amount_of_crackers = boxes of crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# using 10 + 20 as cheese_count and 5 + 6 as boxes_of_crackers
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
# combines variables and numbers to pass values into cheese_and_crackers function
print 'And we can combine the two, variables and math:'
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
