# variables are case sensitive
# if u have used same name for variable last value is considered (ex : CARS)
_cars =23
cars = 24

CARS = 25
CARS = 30

number_of_cars =23
kind_of_car = "Ferrari"

print(_cars)
print(cars)
print(CARS)
print(kind_of_car)


name ="Thara Perera"
type_of_car = "BMW"
school = "high school"

print(name+ " works at " +school)

#python string format() method
print("{} works at {} school.".format(name,school))