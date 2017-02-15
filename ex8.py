 # Formatter is going to turn all objects into strings
formatter = "%r %r %r %r"
 # formatter will print 1, 2, 3, 4
print formatter % (1, 2, 3, 4,)
 # formatter will print one two three four
print formatter % ("one", "two", "three", "four")
 # formatter will print t f f t
print formatter % (True, False, False, True)
 # I think this will print 4 sets of 4 %r
print formatter % (formatter, formatter, formatter, formatter)
print formatter %(
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
	)