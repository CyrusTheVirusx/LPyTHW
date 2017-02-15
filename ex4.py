# initialize the variables with integers
cars = 100
# This number is a floating point number
space_in_a_car = 4.0
drivers = 30
passengers = 90
# Setting a value to the variable cars_not_driven by subtracting cars from drivers
cars_not_driven = cars - drivers
# Setting the value of cars_driven to equal the value of the variable "drivers"
cars_driven = drivers
# Setting the carpool_capacity Value by multiplying the cars_driven and space_in_a_car variables
carpool_capacity = cars_driven * space_in_a_car
# Determining the average_passnegers_per_car by dividing the # of passengers by the # of cars driven 
average_passnegers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passnegers_per_car, "in each car."