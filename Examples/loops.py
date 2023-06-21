#for loops
fruits = ["apple", "orange", "grapes", "pears"]

for i in fruits:
    print("Would you like {} ?".format(i))

#for loops and continue
for number in range (1, 11):
    if number == 7:
        print("Number {}".format(number))
        continue
    print("Number {}".format(number))

#for loops and pass
for number in range (1, 11):
    if number == 3:
        pass
    else:
     print("Number {}".format(number))

#while loops and breaks
temp_f = 40
while temp_f > 32:
    print("degree is {}".format(temp_f))
    temp_f -= 1
    if temp_f == 33:
        break

