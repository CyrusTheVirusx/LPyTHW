
x = 6
def loop_print(num):
	i = 0 
	numbers = []
	while i < num:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

loop_print(x)		
	
print "The numbers: "

for num in numbers:
	print num
