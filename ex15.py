from sys import argv
# arguments are script and filename
script, filename = argv 
# txt will create a file object that is passed into the filename variable 
txt = open(filename)
# will tell you the filename and print its contents using print txt.read()
print "Here's your file %r" % filename
print txt.read()
txt.close()
# uses raw input to change the argv variable filename
print "Type the filename again:"
file_again = raw_input ("> ")
# opens the new file given by the user
txt_again = open(file_again)
#prints the new files contents
print txt_again.read()
txt_again.close()